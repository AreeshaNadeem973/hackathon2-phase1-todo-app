# Data Model: Todo Console Application

## Task Entity

### Attributes
- **id**: Integer
  - Unique identifier for the task
  - Auto-incremented when new tasks are created
  - Required field

- **title**: String
  - Text description of the task
  - Required field
  - Must not be empty

- **completed**: Boolean
  - Indicates whether the task is completed or pending
  - Default value: False (incomplete)
  - Required field

### Validations
- Title must be a non-empty string
- ID must be unique within the task collection
- Completed status must be a boolean value

### State Transitions
- New task: `completed = False` (default)
- Task completion: `completed = False` → `completed = True`
- Task reversion: `completed = True` → `completed = False`

## Task Collection

### Structure
- In-memory storage using Python list/dictionary
- Maintains all tasks during application runtime
- Tasks are lost when application exits (as per requirements)

### Operations
- Add new task to collection
- Retrieve task by ID
- Update task by ID
- Delete task by ID
- List all tasks
- Filter tasks by completion status