from flask import Blueprint, jsonify, request
from models import db, Tasks, Category, task_categories
from utils import format_task_data
from datetime import datetime

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Tasks.query.all()
    formatted_tasks = [format_task_data(task) for task in tasks]
    return jsonify(formatted_tasks)

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority', 0)
    due_date_str = data.get('due_date')
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d %H:%M:%S') if due_date_str else None
    category_names = data.get('categories', [])
    
    if title is None or title == "":
        return jsonify({'message': 'Title is required.'}), 400
    task = Tasks(title=title, description=description, priority=priority, due_date=due_date)
    
    for category_name in category_names:
        category = Category.query.filter_by(name=category_name).first()
        if category is None:
            category = Category(name=category_name)
            db.session.add(category)
        task.categories.append(category)
    
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully.'}), 201


@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Tasks.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task Not Found.'}), 404
    return jsonify(format_task_data(task))

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Tasks.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task Not Found.'}), 404
    data = request.get_json()
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
    return jsonify({'message': 'Task updated successfully.'})

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task Not Found.'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully.'})

@tasks_bp.route('/tasks/category/<category_name>', methods=['GET'])
def get_tasks_by_category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    if category is None:
        return jsonify({'message': f'Category {category_name} Not Found.'}), 404
    tasks = category.tasks.all()
    formatted_tasks = [format_task_data(task) for task in tasks]
    return jsonify(formatted_tasks)
