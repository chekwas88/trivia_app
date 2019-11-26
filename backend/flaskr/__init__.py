import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
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

    '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''
    @app.route('/api/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
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
    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''

    @app.route('/api/questions', methods=['POST'])
    def create_question():
        try:
            body = request.get_json()
            search_term = body.get('searchTerm', None)
            if search_term is not None:
                questions_selection = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
                # category = db.session.query(Category).first()
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


    '''
    @TODO: 
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''


    '''
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''

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
    