"""
Unit tests for the Task entity.
"""

import pytest
from src.models.task import Task


def test_task_creation():
    """Test creating a new task with valid attributes."""
    task = Task(id=1, title="Test task", completed=False)
    
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed == False


def test_task_creation_defaults():
    """Test creating a task with default completion status."""
    task = Task(id=1, title="Test task")
    
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed == False  # Default value


def test_task_title_cannot_be_empty():
    """Test that creating a task with an empty title raises an error."""
    with pytest.raises(ValueError):
        Task(id=1, title="", completed=False)
    
    with pytest.raises(ValueError):
        Task(id=1, title="   ", completed=False)  # Only whitespace


def test_task_id_must_be_integer():
    """Test that creating a task with a non-integer ID raises an error."""
    with pytest.raises(TypeError):
        Task(id="1", title="Test task", completed=False)


def test_task_completed_must_be_boolean():
    """Test that creating a task with a non-boolean completion status raises an error."""
    with pytest.raises(TypeError):
        Task(id=1, title="Test task", completed="false")