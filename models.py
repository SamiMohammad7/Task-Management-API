from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

task_categories = db.Table('task_categories',
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.Integer, default=0)
    due_date = db.Column(db.DateTime, nullable=True)
    categories = db.relationship('Category', secondary=task_categories, backref=db.backref('tasks', lazy='dynamic'))

    def __repr__(self):
        return f'<Task {self.id}>'

