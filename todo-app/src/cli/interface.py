"""
Console interface for the Todo application.
"""

from typing import Optional
from ..services.task_manager import TaskManager
from ..models.task import Task


class ConsoleInterface:
    """
    Handles user interaction through the console.
    """
    
    def __init__(self, task_manager: TaskManager):
        """
        Initialize the console interface with a task manager.
        
        Args:
            task_manager: The TaskManager instance to use
        """
        self.task_manager = task_manager

    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\n--- Todo Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print("------------------------")

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.
        
        Returns:
            The user's choice as a string
        """
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting application...")
            return "6"  # Return exit option

    def handle_add_task(self):
        """
        Handle the add task functionality.
        """
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                return

            task = self.task_manager.add_task(title)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_view_tasks(self):
        """
        Handle the view tasks functionality.
        """
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
        
        print("\n--- Task List ---")
        print(f"{'ID':<3} | {'Title':<30} | {'Status':<10}")
        print("-" * 48)
        
        for task in tasks:
            status = "Complete" if task.completed else "Pending"
            print(f"{task.id:<3} | {task.title[:28]:<30} | {status:<10}")
        print("------------------")

    def handle_update_task(self):
        """
        Handle the update task functionality.
        """
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        new_title = input(f"Enter new title for task {task_id} (current: '{task.title}'): ").strip()
        if not new_title:
            print("Error: Task title cannot be empty.")
            return
        
        try:
            updated = self.task_manager.update_task_title(task_id, new_title)
            if updated:
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Error: Could not update task {task_id}.")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_delete_task(self):
        """
        Handle the delete task functionality.
        """
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        deleted = self.task_manager.delete_task(task_id)
        if deleted:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")

    def handle_mark_task(self):
        """
        Handle the mark task complete/incomplete functionality.
        """
        try:
            task_id = int(input("Enter task ID to mark: "))
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        current_status = "complete" if task.completed else "incomplete"
        target_status = input(f"Mark task as (c)omplete or (i)ncomplete? Current: {current_status} ").strip().lower()
        
        if target_status in ['c', 'complete']:
            success = self.task_manager.mark_task_complete(task_id)
            if success:
                print(f"Task {task_id} marked as complete.")
        elif target_status in ['i', 'incomplete']:
            success = self.task_manager.mark_task_incomplete(task_id)
            if success:
                print(f"Task {task_id} marked as incomplete.")
        else:
            print("Invalid choice. Please enter 'c' for complete or 'i' for incomplete.")

    def run(self):
        """
        Run the main application loop.
        """
        print("Welcome to the Todo Console Application!")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                self.handle_add_task()
            elif choice == "2":
                self.handle_view_tasks()
            elif choice == "3":
                self.handle_update_task()
            elif choice == "4":
                self.handle_delete_task()
            elif choice == "5":
                self.handle_mark_task()
            elif choice == "6":
                print("Thank you for using the Todo Console Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")