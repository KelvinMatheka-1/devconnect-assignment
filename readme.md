Flask Todo App
This is a simple Todo list application built using Flask and PostgreSQL.

Features
Add new tasks
View existing tasks
Update tasks
Delete tasks
Mark tasks as completed
Prerequisites
Before running this application, ensure you have the following installed:

Python 3.x
PostgreSQL
Flask
Flask-SQLAlchemy
Installation

Clone this repository:

git clone <repository_url>

Navigate into the project directory:

cd <project_directory>

Install the required Python dependencies:

pip install -r requirements.txt
Set up the PostgreSQL database:

Create a new database named test_database.
Update the database URI in config.py with your PostgreSQL username and password.

Run the Flask application:

python app.py
Access the application in your web browser at http://localhost:5000.

Usage
To add a new task, enter the task content in the input field and click "Add Task".
To delete a task, click the "Delete" link next to the task.
To update a task, click the "Update" link next to the task and enter the new content.

Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please submit an issue or open a pull request.

