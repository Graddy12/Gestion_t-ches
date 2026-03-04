# Personal Task Manager (To-Do List) API

A premium Flask API for personal task management, built with OOP principles, Pydantic validation, and SQLite storage.

## Features
- **Create Tasks**: Add new tasks with title, description, priority, and due date.
- **Manage Status**: Mark tasks as completed or pending.
- **Categorization**: Classify tasks by priority (Low, Medium, High).
- **Sorting**: list tasks sorted by date or priority.
- **Validation**: Strict data validation using Pydantic.
- **Clean Architecture**: Repository pattern for data persistence.

## Project Structure
- `app/`: Main application package.
  - `database.py`: Database configuration.
  - `models.py`: SQLAlchemy and Pydantic models.
  - `persistence.py`: Data access layer (OOP).
  - `routes.py`: API endpoints.
- `main.py`: Application entry point.

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **API Endpoints**:
   - `GET /api/tasks`: List all tasks (use `?sort=priority` or `?sort=due_date` for sorting).
   - `POST /api/tasks`: Create a new task.
   - `GET /api/tasks/<id>`: Get task details.
   - `PUT /api/tasks/<id>`: Update a task.
   - `DELETE /api/tasks/<id>`: Remove a task.

## Example Request (Create Task)
```json
POST /api/tasks
{
  "title": "Acheter du pain",
  "description": "Aller à la boulangerie avant 19h",
  "priority": "high",
  "due_date": "2024-03-05T18:00:00"
}
```
