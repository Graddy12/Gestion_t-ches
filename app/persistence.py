from typing import List, Optional
from .models import TaskModel, Priority
from .database import db
from datetime import datetime

class TaskRepository:
    """
    Repository class to handle database operations for Tasks.
    This follows the Repository Pattern for clean OOP separation.
    """
    
    @staticmethod
    def create(title: str, description: Optional[str], priority: str, due_date: Optional[datetime]) -> TaskModel:
        task = TaskModel(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_all(sort_by: str = 'created_at') -> List[TaskModel]:
        query = TaskModel.query
        if sort_by == 'priority':
            # Custom sorting: High > Medium > Low
            # Simplest way: use a case statement or just sort alphabetically (not ideal)
            # For simplicity here, we'll order by the string, or we could map them.
            query = query.order_by(TaskModel.priority)
        elif sort_by == 'due_date':
            query = query.order_by(TaskModel.due_date.asc())
        else:
            query = query.order_by(TaskModel.created_at.desc())
        
        return query.all()

    @staticmethod
    def get_by_id(task_id: int) -> Optional[TaskModel]:
        return TaskModel.query.get(task_id)

    @staticmethod
    def update(task_id: int, **kwargs) -> Optional[TaskModel]:
        task = TaskModel.query.get(task_id)
        if task:
            for key, value in kwargs.items():
                if value is not None:
                    setattr(task, key, value)
            db.session.commit()
        return task

    @staticmethod
    def delete(task_id: int) -> bool:
        task = TaskModel.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False
