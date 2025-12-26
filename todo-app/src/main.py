"""
Main entry point for the Todo Console Application.
"""

from src.services.task_manager import TaskManager
from src.cli.interface import ConsoleInterface


def main():
    """
    Main function to run the Todo Console Application.
    """
    # Initialize the task manager
    task_manager = TaskManager()
    
    # Initialize the console interface
    interface = ConsoleInterface(task_manager)
    
    # Run the application
    interface.run()


if __name__ == "__main__":
    main()