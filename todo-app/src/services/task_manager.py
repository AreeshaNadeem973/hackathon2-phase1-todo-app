"""
TaskManager service for managing tasks in memory.
"""

from typing import List, Optional
from ..models.task import Task


class TaskManager:
    """
    Manages tasks in memory with functionality to add, update, delete, and mark tasks.
    """
    
    def __init__(self):
        """
        Initialize the TaskManager with an empty task list and ID counter.
        """
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        """
        Add a new task with the given title.
        
        Args:
            title: The title of the task
            
        Returns:
            The newly created Task object
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(id=self._next_id, title=title.strip(), completed=False)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List of all Task objects
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task_title(self, task_id: int, new_title: str) -> bool:
        """
        Update the title of a task.
        
        Args:
            task_id: The ID of the task to update
            new_title: The new title for the task
            
        Returns:
            True if the task was updated, False if task was not found
        """
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = self.get_task_by_id(task_id)
        if task:
            task.title = new_title.strip()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        
        Args:
            task_id: The ID of the task to mark as complete
            
        Returns:
            True if the task was marked as complete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.
        
        Args:
            task_id: The ID of the task to mark as incomplete
            
        Returns:
            True if the task was marked as incomplete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False