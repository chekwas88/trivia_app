# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

## Getting Started
### Pre-requisites and Local Development
This project requires the installation of python3, pip, node and npm/yarn.

### Backend
Navigate to the backend folder and run ```pip install requirements.txt```.
To run the application run the following command:
``` 
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask run
```
The application runs on ```http://127.0.0.1:5000/```

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


