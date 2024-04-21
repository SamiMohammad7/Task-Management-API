from flask import Flask
from models import db
from routes import tasks_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    app.run(debug=True)