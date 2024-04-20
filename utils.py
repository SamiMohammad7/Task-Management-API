def format_task_data(task):
    formatted_task = {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'priority': task.priority,
        'due_date': task.due_date.strftime('%Y-%m-%d %H:%M:%S') if task.due_date else None,
        'categories': [category.name for category in task.categories]
    }
    return formatted_task