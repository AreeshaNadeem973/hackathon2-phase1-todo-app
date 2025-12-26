# CLI Contract: Todo Console Application

## Overview
The Todo Console Application provides a command-line interface for managing tasks. The application runs interactively, presenting users with a menu of available operations.

## Command Structure
The application runs as a single executable that presents an interactive menu:
```
python src/main.py
```

## Menu Options
The main menu presents the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

## Input/Output Protocol

### Add Task
- **Input**: Task title as string
- **Output**: Confirmation message with assigned task ID
- **Error Cases**: 
  - Empty title → Error message prompting for valid title

### View Tasks
- **Input**: None required
- **Output**: List of all tasks with ID, title, and completion status
- **Format**: 
```
ID | Title | Status
1  | Buy groceries | Pending
2  | Call dentist | Complete
```

### Update Task
- **Input**: Task ID and new title
- **Output**: Confirmation message
- **Error Cases**:
  - Invalid ID → Error message
  - Empty title → Error message

### Delete Task
- **Input**: Task ID
- **Output**: Confirmation message
- **Error Cases**:
  - Invalid ID → Error message

### Mark Task Complete/Incomplete
- **Input**: Task ID and completion status (complete/incomplete)
- **Output**: Confirmation message
- **Error Cases**:
  - Invalid ID → Error message

## Error Handling
All error messages will be user-friendly and descriptive:
- Invalid inputs will result in a clear error message and return to main menu
- Invalid task IDs will result in "Task not found" message
- Empty titles will result in "Title cannot be empty" message

## Exit Condition
The application exits cleanly when the user selects the "Exit" option from the main menu.