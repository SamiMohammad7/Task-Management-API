from models import db, Tasks, Category
from datetime import datetime

class TaskDBAccess:
    @staticmethod
    def get_all_tasks():
        return Tasks.query.all()

    @staticmethod
    def create_task(title, description, priority, due_date, category_names):
        task = Tasks(title=title, description=description, priority=priority, due_date=due_date)

        for category_name in category_names:
            category = Category.query.filter_by(name=category_name).first()
            if category is None:
                category = Category(name=category_name)
                db.session.add(category)
            task.categories.append(category)

        db.session.add(task)
        db.session.commit()

    @staticmethod
    def get_task_by_id(task_id):
        return Tasks.query.get(task_id)

    @staticmethod
    def update_task(task, data):
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'completed' in data:
            task.completed = data['completed']
        if 'priority' in data:
            task.priority = data['priority']
        if 'due_date' in data:
            due_date_str = data['due_date']
            task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d %H:%M:%S') if due_date_str else None

        category_names = data.get('categories', [])
        task.categories = []
        for category_name in category_names:
            category = Category.query.filter_by(name=category_name).first()
            if category is None:
                category = Category(name=category_name)
                db.session.add(category)
            task.categories.append(category)

        db.session.commit()

    @staticmethod
    def delete_task(task):
        db.session.delete(task)
        db.session.commit()

    @staticmethod
    def get_tasks_by_category(category_name):
        category = Category.query.filter_by(name=category_name).first()
        if category:
            return category.tasks.all()
        return []