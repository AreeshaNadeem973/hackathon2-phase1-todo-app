# Quickstart Guide: Todo Console Application

## Prerequisites
- Python 3.11 or higher
- No additional dependencies required

## Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure Python 3.11+ is installed and accessible from command line

## Running the Application
```bash
cd todo-app
python src/main.py
```

## Basic Usage
1. The application starts with an empty task list
2. A menu will be displayed with available options:
   - Add a new task
   - View all tasks
   - Update a task
   - Delete a task
   - Mark task as complete/incomplete
   - Exit the application
3. Follow the on-screen prompts to perform operations
4. Enter the required information when prompted

## Example Workflow
1. Select "Add Task" from the menu
2. Enter the task title when prompted
3. The task will be added with a unique ID and "incomplete" status
4. Select "View Tasks" to see all tasks with their status
5. Use other menu options to manage your tasks

## Testing
To run the tests:
```bash
cd todo-app
python -m pytest tests/
```