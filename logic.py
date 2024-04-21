from db_access import TaskDBAccess
from utils import format_task_data
from datetime import datetime

class TaskLogic:
    @staticmethod
    def get_all_tasks():
        tasks = TaskDBAccess.get_all_tasks()
        return [format_task_data(task) for task in tasks]

    @staticmethod
    def create_task(data):
        title = data.get('title')
        description = data.get('description')
        priority = data.get('priority', 0)
        due_date_str = data.get('due_date')
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d %H:%M:%S') if due_date_str else None
        category_names = data.get('categories', [])

        if title is None or title == "":
            raise ValueError('Title is required.')

        TaskDBAccess.create_task(title, description, priority, due_date, category_names)

    @staticmethod
    def get_task(task_id):
        task = TaskDBAccess.get_task_by_id(task_id)
        if not task:
            raise ValueError('Task Not Found.')
        return format_task_data(task)

    @staticmethod
    def update_task(task_id, data):
        task = TaskDBAccess.get_task_by_id(task_id)
        if not task:
            raise ValueError('Task Not Found.')
        TaskDBAccess.update_task(task, data)

    @staticmethod
    def delete_task(task_id):
        task = TaskDBAccess.get_task_by_id(task_id)
        if not task:
            raise ValueError('Task Not Found.')
        TaskDBAccess.delete_task(task)

    @staticmethod
    def get_tasks_by_category(category_name):
        tasks = TaskDBAccess.get_tasks_by_category(category_name)
        return [format_task_data(task) for task in tasks]