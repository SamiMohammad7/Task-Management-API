# TASK MANAGEMENT API

RESTful Task Management API, that allows users to manage
tasks, created using Flask, SQLAlchemy, and PostgreSQL.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)


## Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/SamiMohammad7/Task-Management-API.git
    ```

2. **Navigate to the project directory:**

    ```
    cd Task-Management-API
    ```

3. **Setup a virtual environment:**

    ```
    # Using venv module
    python -m venv venv

    # Activate virtual environment
    source venv/bin/activate
    #Or
    venv/Scripts/activate
    ```

4. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

    Make sure you have Python and pip installed.

5. **Setup PostgreSQL Database:**

    - Install PostgreSQL if not already installed.
    - Create a new database:

        ```
        create database flask_db;
        ```
    - Create "tasks" table:

        ```
        CREATE TABLE tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN
            priority INTEGER DEFAULT 0,
            due_date TIMESTAMP
        );
        ```
    - Create "category" table:

        ```
        CREATE TABLE category (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL UNIQUE
        );
        ```
    - Create "task_categories" table:

        ```
        CREATE TABLE task_categories (
            task_id INTEGER REFERENCES tasks(id),
            category_id INTEGER REFERENCES category(id),
            PRIMARY KEY (task_id, category_id)
        );
        ```

    - Edit `config.py` to configure database URI. Replace `SQLALCHEMY_DATABASE_URI` with your PostgreSQL URI.


## Usage

1. **Run the application:**

    ```
    python main.py
    ```

2. **Access the application:**

    Open a web browser and go to `http://localhost:5000` 

3. **Testing with Postman:**

    - Launch Postman and create a new request.
    - Set the request type (GET, POST, PUT, DELETE) and enter the appropriate URL (e.g., `http://localhost:5000/tasks`).
    - Add any necessary headers or request body parameters.
    - Send the request to interact with the application's API endpoints.

4. **API Endpoints:**

    - `GET /tasks`: Get all tasks.
    - `POST /tasks`: Create a new task.
    - `GET /tasks/<task_id>`: Get details of a specific task.
    - `PUT /tasks/<task_id>`: Update a specific task.
    - `DELETE /tasks/<task_id>`: Delete a specific task.
    - `GET /tasks/category/<category_name>`: Get tasks by category.
