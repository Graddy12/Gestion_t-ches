from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from .models import TaskCreate, TaskUpdate, TaskResponse
from .persistence import TaskRepository

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        task_data = TaskCreate(**data)
        
        task = TaskRepository.create(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority.value,
            due_date=task_data.due_date
        )
        
        return jsonify(TaskResponse.model_validate(task).model_dump()), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    sort_by = request.args.get('sort', 'created_at')
    tasks = TaskRepository.get_all(sort_by=sort_by)
    return jsonify([TaskResponse.model_validate(t).model_dump() for t in tasks]), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = TaskRepository.get_by_id(task_id)
    if task:
        return jsonify(TaskResponse.model_validate(task).model_dump()), 200
    return jsonify({"error": "Task not found"}), 404

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):
    try:
        data = request.get_json()
        task_update = TaskUpdate(**data)
        
        updated_task = TaskRepository.update(
            task_id,
            **task_update.model_dump(exclude_unset=True)
        )
        
        if updated_task:
            return jsonify(TaskResponse.model_validate(updated_task).model_dump()), 200
        return jsonify({"error": "Task not found"}), 404
    except ValidationError as e:
        return jsonify(e.errors()), 400

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if TaskRepository.delete(task_id):
        return '', 204
    return jsonify({"error": "Task not found"}), 404
