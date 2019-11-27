import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    '''
    paginate questions to return in 
    groups of 10 at a time
    '''
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r'/api/*': {'origins': '*'}})
    
    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
        return response

    '''
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''
    #get all categories
    @app.route('/api/categories')
    def retrieve_categories():
        try:
            categories = Category.query.all()
            formatted_categories = [category.format() for category in categories]
            return jsonify({
                'success': True,
                'categories': formatted_categories,
                'total_categories': len(Category.query.all())
            }), 200
        except:
            abort(422)

    # get all questions from db
    @app.route('/api/questions')
    def retrieve_questions():
        try:
            questions_selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, questions_selection)
            categories = Category.query.all()
            formatted_categories = [category.format() for category in categories]

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(Question.query.all()),
                'categories': formatted_categories,
                'current_category': categories[0].format()
            }), 200
        except:
            abort(422)


    @app.route('/api/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        '''
        deletes the specified question from the db
        '''
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            question.delete()

            return jsonify({
                'success': True,
                'deleted': question_id,
                'total_questions': len(Question.query.all())
            }), 200

        except:
            abort(404)
   

    @app.route('/api/questions', methods=['POST'])
    def create_question():
        try:
            body = request.get_json()
            search_term = body.get('searchTerm', None)
            if search_term is not None:
                '''
                return a list of questions that corresponds
                to the serch term
                '''
                questions_selection = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
                current_questions = paginate_questions(request, questions_selection)
                categories = Category.query.all()
                formatted_categories = [category.format() for category in categories]
                return jsonify({
                   'success': True,
                    'questions': current_questions,
                    'total_questions': len(Question.query.all()),
                    'categories': formatted_categories,
                    'current_category': categories[0].format()
                }), 200
            else:
                '''
                create a new question using the request params 
                '''
                question = body.get('question', None)
                answer = body.get('answer', None)
                difficulty = body.get('difficulty', None)
                category = body.get('category', None)
                new_question = Question(question=question, answer=answer, difficulty=difficulty, category=category)
                new_question.insert()

                return jsonify({
                    'success': True,
                    'created': new_question.id,
                    'total_questions': len(Question.query.all())
                }), 201

        except:
            abort(422)


    @app.route('/api/categories/<int:category_id>/questions')
    def get_questions_based_on_category(category_id):
        '''
        return a list of questions that corresponse
        to the specified category
        '''
        category = Category.query.get(category_id)
        if category is None:
            abort(404)
        try:
            questions_selection = Question.query.filter(Question.category == str(category.id)).all()
            current_questions = paginate_questions(request, questions_selection)
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions_selection),
                'current_category': category.format()
            }), 200
        except:
            abort(422)

    @app.route('/api/quizzes', methods=['POST'])
    def get_quizzes():
        '''
        return questions based on the specified category if applicable.
        questions returned previously are not repeated.
        The questions are returned one at a time.
        '''
        try:
            body = request.get_json()
            questions = Question.query.filter_by(
                category=body.get("quiz_category")["id"]
            ).filter(Question.id.notin_(body.get("previous_questions"))).all()

            if body.get("quiz_category")["id"] == 0:
                questions = Question.query.filter(
                    Question.id.notin_(body.get("previous_questions"))).all()

            question = None

            if questions:
                question = random.choice(questions).format()

            return jsonify({
                "success": True,
                "question": question
            }), 200
        except:
            abort(404)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        "success": False, 
        "error": 404,
        "message": "Resource not found"
        }), 404
        
    return app
    