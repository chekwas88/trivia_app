# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

The application runs on ```http://127.0.0.1:5000/```

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 



### Frontend
From the frontend folder run the following command:
```npm install or yarn install``` to install the packages in package.json file.
To run the application run ```npm start or yarn start```
The application runs on ```http://127.0.0.1:3000/```

### Tests
To run tests navigate to backend folder and run the following commands:
```
    createdb trivia_test
    python test_flaskr.py
```

## API Reference
The base url for this API is ```http://127.0.0.1:5000/``` which serves as a proxy to the frontend. Currently the API is not hosted.

No Authentication or API key is needed.

### Error handling
Errors are returned in the following format:
```
{
    "success": False,
    "error": 404/422/400,
    "message": "error message"
}
```
### Endpoints

***GET /api/categories***

This returns a list of all categories.

**sample return**
```
{
    "success": True,
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "History"
        },
        {
            "id": 4,
            "type": "Sport"
        },
        ...
    ],
    "total_categories": 5
}
```

***GET /api/questions***

This returns a list of questions stored in the database. The results are paginated in groups of 10.

**Sample Return**

```
    {
    "success": True,
    "questions": [
        {
            "id": 1,
            "question": "La Giaconda is better known as what?",
            "answer": "Mona Lisa",
            "category": "2",
            "difficulty": 2
        },
        {
            "id": 2,
            "question": "What is the heaviest organ in the human body?",
            "answer": "The Liver",
            "category": "1",
            difficulty: 3
        },
        {
            "id": 3,
            "question": "Who is the best Soccer player of all time?",
            "answer": "Ronaldo de Lima",
            "category": "4",
            difficulty: 3
        },
        ...
    ],
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "History"
        },
        {
            "id": 4,
            "type": "Sport"
        },
        ...
    ],
    "current_category": "Science", 
    "total_questions": 30
}
```
***GET /api/categories/<<int:category_id>>/questions***

This returns a list of questions based on the specified category from the database. The results are paginated in groups of 10.

**Sample Return**

```
    {
    "success": True,
    "questions": [
        {
            "id": 1,
            "question": "La Giaconda is better known as what?",
            "answer": "Mona Lisa",
            "category": "2",
            "difficulty": 2
        },
        {
            "id": 2,
            "question": "What is the heaviest organ in the human body?",
            "answer": "The Liver",
            "category": "1",
            difficulty: 3
        },
        {
            "id": 3,
            "question": "Who is the best Soccer player of all time?",
            "answer": "Ronaldo de Lima",
            "category": "4",
            difficulty: 3
        },
        ...
    ],
    "current_category": "Science", 
    "total_questions": 30
}
```
***GET /api/questions/<<int:question_id>>***

This deletes the specified question from the database.

**Sample Return**
```
{
    "success": True,
    "deleted": 2
    "total_questions": 29
}
```

***POST /api/questions***

This creates a new question in the database.

**Request Parameters**

```
    {
        "question": "Which genre of music does coldplay perform?",
        "answer": "alternative",
        "category": "Entertainment",
        "difficulty": 2,
    }
```

**Sample Return**
```
{
    "success": True,
    "created": 31,
    "total_question": 30

}

```
***POST /api/quizzes***

This creates a quiz and returns each question one at a time.

**Sample Return**
```
{
    "success": True,
    "question": "What is the heaviest organ in the human body?"

}

```

### Deployment N/A

### Authors
  Chisom Onwuchekwa

### Acknowledgements

Coach Caryn and the Udacity team.
