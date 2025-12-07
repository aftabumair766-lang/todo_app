#!/usr/bin/env python3
"""
Add Task Agent - Handles task creation operations.

This agent is responsible for creating and adding new tasks to the storage.
"""

try:
    from .base_agent import BaseAgent
    from ..models import Task
except ImportError:
    from agents.base_agent import BaseAgent
    from models import Task


class AddTaskAgent(BaseAgent):
    """
    Agent responsible for adding new tasks.

    This agent validates input, creates Task objects, and adds them to storage.
    """

    def validate_input(self, title, description=""):
        """
        Validate task creation input.

        Args:
            title (str): Task title
            description (str): Task description

        Returns:
            tuple: (is_valid, error_message)
        """
        if not title or not title.strip():
            return False, "Title cannot be empty"

        if len(title.strip()) > 100:
            return False, "Title cannot exceed 100 characters"

        if len(description.strip()) > 500:
            return False, "Description cannot exceed 500 characters"

        return True, None

    def execute(self, title, description=""):
        """
        Create and add a new task.

        Args:
            title (str): Task title
            description (str, optional): Task description

        Returns:
            tuple: (success, result_or_error)
                - If success: (True, Task)
                - If failure: (False, error_message)
        """
        # Validate input
        is_valid, error_msg = self.validate_input(title, description)
        if not is_valid:
            return False, error_msg

        # Create task
        task_id = self.task_storage.get_next_id()
        task = Task(task_id, title.strip(), description.strip())

        # Add to storage
        self.task_storage.add(task)

        return True, task

    def get_success_message(self, task):
        """
        Get success message with task details.

        Args:
            task (Task): The created task

        Returns:
            str: Success message
        """
        return f"\nTask added successfully! (ID: {task.id})"
