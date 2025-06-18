# 🍕 Pizza API

A simple RESTful API for managing restaurants, pizzas, and their associations.

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge

2. Set Up Virtual Environment Using Pipenv
pipenv install
pipenv shell

3. Set Environment Variables
export FLASK_APP=app
export FLASK_ENV=development

4. Initialize and Migrate the Database
flask db init         # Run only once
flask db migrate -m "Initial migration"
flask db upgrade

5. Seed the Database
Inside seed.py, add your seed data, then run:
python seed.py

6. Run the Server
flask run

records

📫 Postman Usage Instructions
Open Postman.

Start the Flask server: flask run

Use http://127.0.0.1:5000 as the base URL.

Use the method/endpoint combos above to test:

Set method (GET, POST, DELETE)

Provide JSON body for POST

Set Content-Type: application/json in headers

