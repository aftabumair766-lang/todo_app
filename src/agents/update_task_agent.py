#!/usr/bin/env python3
"""
Update Task Agent - Handles task modification operations.

This agent is responsible for updating task details.
"""

try:
    from .base_agent import BaseAgent
except ImportError:
    from agents.base_agent import BaseAgent


class UpdateTaskAgent(BaseAgent):
    """
    Agent responsible for updating task details.

    This agent validates inputs and modifies task title and/or description.
    """

    def validate_input(self, task_id, new_title=None, new_description=None):
        """
        Validate update task input.

        Args:
            task_id (int): Task ID to update
            new_title (str, optional): New title
            new_description (str, optional): New description

        Returns:
            tuple: (is_valid, error_message)
        """
        if not isinstance(task_id, int):
            return False, "Task ID must be an integer"

        if task_id < 1:
            return False, "Task ID must be positive"

        if new_title is None and new_description is None:
            return False, "Please provide at least one field to update"

        if new_title is not None and not new_title.strip():
            return False, "Title cannot be empty"

        if new_title is not None and len(new_title.strip()) > 100:
            return False, "Title cannot exceed 100 characters"

        if new_description is not None and len(new_description.strip()) > 500:
            return False, "Description cannot exceed 500 characters"

        return True, None

    def execute(self, task_id, new_title=None, new_description=None):
        """
        Update a task's title and/or description.

        Args:
            task_id (int): ID of the task to update
            new_title (str, optional): New title
            new_description (str, optional): New description

        Returns:
            tuple: (success, result_or_error)
                - If success: (True, updated_task)
                - If failure: (False, error_message)
        """
        # Validate input
        is_valid, error_msg = self.validate_input(task_id, new_title, new_description)
        if not is_valid:
            return False, error_msg

        # Get task from storage
        task = self.task_storage.get(task_id)
        if task is None:
            return False, f"Task with ID {task_id} not found"

        # Update task fields
        if new_title is not None:
            task.title = new_title.strip()

        if new_description is not None:
            task.description = new_description.strip()

        return True, task

    def get_success_message(self, task):
        """
        Get success message with updated task details.

        Args:
            task (Task): The updated task

        Returns:
            str: Success message
        """
        return f"\nTask (ID: {task.id}) updated successfully!\n{task}"
