"""
Task entity representing a single todo item.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo task with id, title, and completion status.
    """
    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """
        Validate the task attributes after initialization.
        """
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if not isinstance(self.id, int):
            raise TypeError("Task ID must be an integer")
        if not isinstance(self.completed, bool):
            raise TypeError("Task completion status must be a boolean")