"""
Contract tests for the TaskManager add_task, view tasks, mark task, update task, and delete task functionality.
"""

import pytest
from src.services.task_manager import TaskManager


def test_add_task_creates_new_task():
    """Test that add_task creates a new task with correct attributes."""
    manager = TaskManager()

    task = manager.add_task("Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed == False


def test_add_task_assigns_unique_ids():
    """Test that add_task assigns unique IDs to each task."""
    manager = TaskManager()

    task1 = manager.add_task("First task")
    task2 = manager.add_task("Second task")

    assert task1.id == 1
    assert task2.id == 2
    assert task1.id != task2.id


def test_add_task_defaults_to_incomplete():
    """Test that newly added tasks are marked as incomplete by default."""
    manager = TaskManager()

    task = manager.add_task("Test task")

    assert task.completed == False


def test_add_task_stores_in_manager():
    """Test that add_task stores the task in the manager."""
    manager = TaskManager()

    task = manager.add_task("Test task")
    all_tasks = manager.get_all_tasks()

    assert len(all_tasks) == 1
    assert all_tasks[0] == task


def test_add_task_with_empty_title_raises_error():
    """Test that adding a task with an empty title raises an error."""
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task("")

    with pytest.raises(ValueError):
        manager.add_task("   ")  # Only whitespace


def test_get_all_tasks_returns_empty_list_initially():
    """Test that get_all_tasks returns an empty list when no tasks exist."""
    manager = TaskManager()

    tasks = manager.get_all_tasks()

    assert len(tasks) == 0


def test_get_all_tasks_returns_all_tasks():
    """Test that get_all_tasks returns all added tasks."""
    manager = TaskManager()

    manager.add_task("First task")
    manager.add_task("Second task")
    manager.add_task("Third task")

    tasks = manager.get_all_tasks()

    assert len(tasks) == 3
    assert tasks[0].title == "First task"
    assert tasks[1].title == "Second task"
    assert tasks[2].title == "Third task"


def test_get_all_tasks_returns_copy_not_original():
    """Test that get_all_tasks returns a copy of the internal list."""
    manager = TaskManager()

    manager.add_task("Test task")
    tasks = manager.get_all_tasks()

    # Modify the returned list
    tasks.append("Fake task")

    # Original list should remain unchanged
    original_tasks = manager.get_all_tasks()
    assert len(original_tasks) == 1
    assert original_tasks[0].title == "Test task"
    assert len([t for t in original_tasks if t.title == "Fake task"]) == 0


def test_get_all_tasks_preserves_task_attributes():
    """Test that get_all_tasks preserves all task attributes."""
    manager = TaskManager()

    # Add a task and mark it as complete
    task = manager.add_task("Test task")
    manager.mark_task_complete(task.id)

    tasks = manager.get_all_tasks()

    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].title == "Test task"
    assert tasks[0].completed == True


def test_mark_task_complete():
    """Test that mark_task_complete marks a task as complete."""
    manager = TaskManager()

    # Add a task
    task = manager.add_task("Test task")
    assert task.completed == False  # Initially incomplete

    # Mark as complete
    success = manager.mark_task_complete(task.id)

    assert success == True
    assert task.completed == True


def test_mark_task_incomplete():
    """Test that mark_task_incomplete marks a task as incomplete."""
    manager = TaskManager()

    # Add a task and mark it as complete
    task = manager.add_task("Test task")
    manager.mark_task_complete(task.id)
    assert task.completed == True  # Now complete

    # Mark as incomplete
    success = manager.mark_task_incomplete(task.id)

    assert success == True
    assert task.completed == False


def test_mark_task_complete_returns_false_for_invalid_id():
    """Test that mark_task_complete returns False for invalid task ID."""
    manager = TaskManager()

    success = manager.mark_task_complete(999)  # Non-existent ID

    assert success == False


def test_mark_task_incomplete_returns_false_for_invalid_id():
    """Test that mark_task_incomplete returns False for invalid task ID."""
    manager = TaskManager()

    success = manager.mark_task_incomplete(999)  # Non-existent ID

    assert success == False


def test_mark_task_complete_preserves_other_attributes():
    """Test that marking a task complete preserves other attributes."""
    manager = TaskManager()

    task = manager.add_task("Test task")
    original_id = task.id
    original_title = task.title

    manager.mark_task_complete(task.id)

    assert task.id == original_id
    assert task.title == original_title
    assert task.completed == True


def test_mark_task_incomplete_preserves_other_attributes():
    """Test that marking a task incomplete preserves other attributes."""
    manager = TaskManager()

    # Add task and mark as complete
    task = manager.add_task("Test task")
    manager.mark_task_complete(task.id)

    original_id = task.id
    original_title = task.title

    # Mark as incomplete
    manager.mark_task_incomplete(task.id)

    assert task.id == original_id
    assert task.title == original_title
    assert task.completed == False


def test_update_task_title():
    """Test that update_task_title updates the title of a task."""
    manager = TaskManager()

    # Add a task
    task = manager.add_task("Original title")
    original_id = task.id

    # Update the title
    success = manager.update_task_title(task.id, "New title")

    assert success == True
    assert task.title == "New title"
    assert task.id == original_id  # ID should remain the same


def test_update_task_title_returns_false_for_invalid_id():
    """Test that update_task_title returns False for invalid task ID."""
    manager = TaskManager()

    success = manager.update_task_title(999, "New title")  # Non-existent ID

    assert success == False


def test_update_task_title_preserves_completion_status():
    """Test that updating a task title preserves its completion status."""
    manager = TaskManager()

    # Add a task and mark it as complete
    task = manager.add_task("Original title")
    manager.mark_task_complete(task.id)
    assert task.completed == True

    # Update the title
    manager.update_task_title(task.id, "New title")

    assert task.title == "New title"
    assert task.completed == True  # Completion status should be preserved


def test_update_task_title_with_empty_string_raises_error():
    """Test that updating a task with an empty title raises an error."""
    manager = TaskManager()

    # Add a task
    task = manager.add_task("Original title")

    # Try to update with empty title
    with pytest.raises(ValueError):
        manager.update_task_title(task.id, "")

    # Try to update with whitespace-only title
    with pytest.raises(ValueError):
        manager.update_task_title(task.id, "   ")


def test_update_task_title_allows_same_title():
    """Test that updating a task with the same title works."""
    manager = TaskManager()

    # Add a task
    task = manager.add_task("Same title")

    # Update with the same title
    success = manager.update_task_title(task.id, "Same title")

    assert success == True
    assert task.title == "Same title"


def test_update_task_title_allows_partial_changes():
    """Test that updating a task title with partial changes works."""
    manager = TaskManager()

    # Add a task
    task = manager.add_task("Original title")

    # Update with a similar title
    success = manager.update_task_title(task.id, "Original title updated")

    assert success == True
    assert task.title == "Original title updated"


def test_delete_task():
    """Test that delete_task removes a task from the manager."""
    manager = TaskManager()

    # Add some tasks
    task1 = manager.add_task("First task")
    task2 = manager.add_task("Second task")
    task3 = manager.add_task("Third task")

    # Verify all tasks exist
    assert len(manager.get_all_tasks()) == 3

    # Delete one task
    success = manager.delete_task(task2.id)

    assert success == True
    assert len(manager.get_all_tasks()) == 2

    # Verify the correct task was deleted
    remaining_tasks = manager.get_all_tasks()
    task_ids = [task.id for task in remaining_tasks]
    assert task1.id in task_ids
    assert task3.id in task_ids
    assert task2.id not in task_ids


def test_delete_task_returns_false_for_invalid_id():
    """Test that delete_task returns False for invalid task ID."""
    manager = TaskManager()

    # Add a task
    task = manager.add_task("Test task")

    # Try to delete a non-existent task
    success = manager.delete_task(999)

    assert success == False
    # Original task should still exist
    assert len(manager.get_all_tasks()) == 1
    assert manager.get_task_by_id(task.id) is not None


def test_delete_task_with_multiple_tasks():
    """Test that delete_task works correctly with multiple tasks."""
    manager = TaskManager()

    # Add multiple tasks
    tasks = []
    for i in range(5):
        tasks.append(manager.add_task(f"Task {i+1}"))

    assert len(manager.get_all_tasks()) == 5

    # Delete the middle task
    success = manager.delete_task(tasks[2].id)  # Task 3

    assert success == True
    assert len(manager.get_all_tasks()) == 4

    # Verify the correct task was deleted
    remaining_tasks = manager.get_all_tasks()
    remaining_ids = [task.id for task in remaining_tasks]
    assert tasks[2].id not in remaining_ids  # Task 3 should be gone
    for i in [0, 1, 3, 4]:  # Other tasks should remain
        assert tasks[i].id in remaining_ids


def test_delete_task_preserves_other_task_attributes():
    """Test that deleting a task doesn't affect other tasks' attributes."""
    manager = TaskManager()

    # Add tasks with different completion statuses
    task1 = manager.add_task("Incomplete task")
    task2 = manager.add_task("Complete task")
    manager.mark_task_complete(task2.id)

    # Delete the first task
    manager.delete_task(task1.id)

    # Verify the remaining task still has its correct attributes
    remaining_tasks = manager.get_all_tasks()
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0].id == task2.id
    assert remaining_tasks[0].title == "Complete task"
    assert remaining_tasks[0].completed == True


def test_delete_all_tasks():
    """Test that deleting all tasks results in an empty manager."""
    manager = TaskManager()

    # Add some tasks
    manager.add_task("First task")
    manager.add_task("Second task")

    assert len(manager.get_all_tasks()) == 2

    # Delete all tasks one by one
    all_tasks = manager.get_all_tasks()
    for task in all_tasks:
        success = manager.delete_task(task.id)
        assert success == True

    # Verify manager is empty
    assert len(manager.get_all_tasks()) == 0