from flask import Flask
from models import db
from routes import tasks_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:592001@localhost:5432/flask_db'

# Initialize the database
db.init_app(app)

# Register routes
app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    app.run(debug=True)