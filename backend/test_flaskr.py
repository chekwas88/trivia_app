import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('princ', 'password', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

            category1 = Category(type='Science')
            category2 = Category(type='Art')
            self.db.session.add_all([category1, category2])
            self.db.session.commit()

            science_category = self.db.session.query(Category).filter(Category.type == 'Science').first()
            art_category = self.db.session.query(Category).filter(Category.type == 'Art').first()

            question1 = Question(
                question="La Giaconda is better known as what?",
                answer="Mona Lisa",
                category=str(art_category.id),
                difficulty=2
            )

            question2 = Question(
                question="What is the heaviest organ in the human body?",
                answer="The Liver",
                category=str(science_category.id),
                difficulty=3
            )
            self.db.session.add_all([question1, question2])
            self.db.session.commit()
    
    def tearDown(self):
        """Executed after each test"""
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            categories = self.db.session.query(Category).all()
            for category in categories:
                self.db.session.delete(category)

            questions = self.db.session.query(Question).all()
            for question in questions:
                self.db.session.delete(question)
            self.db.session.commit()


    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_retrieve_categories(self):
        res = self.client().get('/api/categories')
        payload = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(payload['success'], True)
        self.assertTrue(payload['categories'])
        self.assertTrue(payload['total_categories'])

    
    def test_retrieve_questions(self):
        res = self.client().get('/api/questions')
        payload = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(payload['success'], True)
        self.assertTrue(payload['questions'])
        self.assertTrue(payload['current_category'])
        self.assertTrue(payload['categories'])
        self.assertTrue(payload['total_questions'])

    def test_create_question(self):
        res = self.client().post('/api/questions',  json={
            'question': 'Which genre does coldplay perform?',
            'answer': 'alternative',
            'category': '4',
            'difficulty': 4
        })
        payload = json.loads(res.data)
        
        self.assertEqual(res.status_code, 201)
        self.assertEqual(payload['success'], True)
        self.assertTrue(payload['created'])
        self.assertTrue(payload['total_questions'])

    def test_delete_question(self):
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            question = self.db.session.query(Question).first()


        res = self.client().delete('/api/questions/{}'.format(question.id))
        payload = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(payload['deleted'])
        self.assertEqual(payload['success'], True)
        self.assertTrue(payload['total_questions'])

    def test_delete_question_error(self):
       
        res = self.client().delete('/api/questions/100000000')
        payload = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(payload['success'], False)
        self.assertEqual(payload['error'], 404)
        self.assertEqual(payload['message'], 'Resource not found')

    def test_search_questions(self):
        res = self.client().post('/api/questions', json={'searchTerm': 'heaviest'})
        payload = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(payload['success'], True)
        self.assertTrue(payload['total_questions'])
        self.assertTrue(payload['questions'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()