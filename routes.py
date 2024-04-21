from flask import Blueprint, jsonify, request
from logic import TaskLogic

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = TaskLogic.get_all_tasks()
        return jsonify(tasks)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        TaskLogic.create_task(data)
        return jsonify({'message': 'Task created successfully.'}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = TaskLogic.get_task(task_id)
        return jsonify(task)
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.get_json()
        TaskLogic.update_task(task_id, data)
        return jsonify({'message': 'Task updated successfully.'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        TaskLogic.delete_task(task_id)
        return jsonify({'message': 'Task deleted successfully.'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@tasks_bp.route('/tasks/category/<category_name>', methods=['GET'])
def get_tasks_by_category(category_name):
    try:
        tasks = TaskLogic.get_tasks_by_category(category_name)
        return jsonify(tasks)
    except Exception as e:
        return jsonify({'message': str(e)}), 500