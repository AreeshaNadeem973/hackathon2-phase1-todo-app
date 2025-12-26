"""
Tests for displaying tasks with correct format in the CLI interface.
"""

from io import StringIO
import sys
from unittest.mock import patch
from src.services.task_manager import TaskManager
from src.cli.interface import ConsoleInterface


def test_display_tasks_with_empty_list():
    """Test that displaying tasks shows appropriate message when list is empty."""
    manager = TaskManager()
    interface = ConsoleInterface(manager)
    
    # Capture the output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    interface.handle_view_tasks()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert "No tasks found." in output


def test_display_tasks_shows_all_tasks():
    """Test that displaying tasks shows all tasks with correct format."""
    manager = TaskManager()
    interface = ConsoleInterface(manager)
    
    # Add some tasks
    manager.add_task("First task")
    manager.add_task("Second task")
    task3 = manager.add_task("Third task")
    manager.mark_task_complete(task3.id)  # Mark one as complete
    
    # Capture the output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    interface.handle_view_tasks()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    
    # Check that all tasks are displayed
    assert "First task" in output
    assert "Second task" in output
    assert "Third task" in output
    
    # Check that the format is correct
    assert "ID" in output
    assert "Title" in output
    assert "Status" in output
    
    # Check that completion status is shown correctly
    assert "Pending" in output  # For incomplete tasks
    assert "Complete" in output  # For complete tasks


def test_display_tasks_format_consistency():
    """Test that the display format is consistent."""
    manager = TaskManager()
    interface = ConsoleInterface(manager)
    
    # Add a task
    manager.add_task("Test task")
    
    # Capture the output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    interface.handle_view_tasks()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    
    # Check that the table structure is present
    lines = output.split('\n')
    header_line_found = False
    separator_line_found = False
    
    for line in lines:
        if "ID" in line and "Title" in line and "Status" in line:
            header_line_found = True
        if "-" * 48 in line:  # The separator line
            separator_line_found = True
    
    assert header_line_found, "Header line with ID, Title, Status not found"
    assert separator_line_found, "Separator line not found"