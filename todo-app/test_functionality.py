"""
Simple test script to verify the Todo Console Application functionality.
"""

from src.services.task_manager import TaskManager
from src.models.task import Task


def test_task_creation():
    """Test creating a task."""
    task = Task(id=1, title="Test task", completed=False)
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed == False
    print("PASS: Task creation works")


def test_task_manager_add_task():
    """Test adding a task."""
    manager = TaskManager()
    task = manager.add_task("Test task")
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed == False
    print("PASS: TaskManager add_task works")


def test_task_manager_get_all_tasks():
    """Test getting all tasks."""
    manager = TaskManager()
    manager.add_task("First task")
    manager.add_task("Second task")
    
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "First task"
    assert tasks[1].title == "Second task"
    print("PASS: TaskManager get_all_tasks works")


def test_task_manager_update_task():
    """Test updating a task."""
    manager = TaskManager()
    task = manager.add_task("Original task")
    
    success = manager.update_task_title(task.id, "Updated task")
    assert success == True
    assert task.title == "Updated task"
    print("PASS: TaskManager update_task_title works")


def test_task_manager_mark_task():
    """Test marking a task complete/incomplete."""
    manager = TaskManager()
    task = manager.add_task("Test task")
    
    # Mark as complete
    success = manager.mark_task_complete(task.id)
    assert success == True
    assert task.completed == True
    
    # Mark as incomplete
    success = manager.mark_task_incomplete(task.id)
    assert success == True
    assert task.completed == False
    print("PASS: TaskManager mark_task_complete/incomplete works")


def test_task_manager_delete_task():
    """Test deleting a task."""
    manager = TaskManager()
    task = manager.add_task("Test task")
    
    success = manager.delete_task(task.id)
    assert success == True
    assert len(manager.get_all_tasks()) == 0
    print("PASS: TaskManager delete_task works")


def main():
    """Run all tests."""
    print("Running functionality tests...")
    
    test_task_creation()
    test_task_manager_add_task()
    test_task_manager_get_all_tasks()
    test_task_manager_update_task()
    test_task_manager_mark_task()
    test_task_manager_delete_task()
    
    print("\nAll functionality tests passed!")
    print("The Todo Console Application is working correctly.")


if __name__ == "__main__":
    main()