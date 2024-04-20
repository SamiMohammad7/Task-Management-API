# TASK MANAGEMENT API

Brief description or introduction of your application.

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
    python3 -m venv venv

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

    - Edit `config.py` to configure your database URI. Replace `postgresql://username:password@localhost/database_name` with your PostgreSQL URI:

        ```python
        SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/your_database_name'
        ```

## Usage

1. **Run the application:**

    ```
    python app.py
    ```

2. **Access the application:**

    Open a web browser and go to `http://localhost:5000` (or the appropriate address/port if configured differently).

3. **API Endpoints:**

    - `GET /tasks`: Get all tasks.
    - `POST /tasks`: Create a new task.
    - `GET /tasks/<task_id>`: Get details of a specific task.
    - `PUT /tasks/<task_id>`: Update a specific task.
    - `DELETE /tasks/<task_id>`: Delete a specific task.
    - `GET /tasks/category/<category_name>`: Get tasks by category.

## Configuration

You may need to configure certain settings before running the application. This can include database configurations, environment variables, or any other settings specific to your application.

1. **Database Configuration:**

    - Edit `config.py` to configure your database URI.

2. **Environment Variables:**

    - You can use environment variables to store sensitive information or configuration settings. Refer to the documentation for details on which variables to set and their values.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## License

Include license information for your project here.