#!/usr/bin/env python3
"""
Delete Task Agent - Handles task deletion operations.

This agent is responsible for removing tasks from storage.
"""

from .base_agent import BaseAgent


class DeleteTaskAgent(BaseAgent):
    """
    Agent responsible for deleting tasks.

    This agent validates task IDs and removes tasks from storage.
    """

    def validate_input(self, task_id):
        """
        Validate task ID for deletion.

        Args:
            task_id (int): Task ID to validate

        Returns:
            tuple: (is_valid, error_message)
        """
        if not isinstance(task_id, int):
            return False, "Task ID must be an integer"

        if task_id < 1:
            return False, "Task ID must be positive"

        return True, None

    def execute(self, task_id):
        """
        Delete a task by ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            tuple: (success, result_or_error)
                - If success: (True, deleted_task)
                - If failure: (False, error_message)
        """
        # Validate input
        is_valid, error_msg = self.validate_input(task_id)
        if not is_valid:
            return False, error_msg

        # Remove task from storage
        deleted_task = self.task_storage.remove(task_id)

        if deleted_task is None:
            return False, f"Task with ID {task_id} not found"

        return True, deleted_task

    def get_success_message(self, task):
        """
        Get success message with deleted task details.

        Args:
            task (Task): The deleted task

        Returns:
            str: Success message
        """
        return f"\nTask '{task.title}' (ID: {task.id}) deleted successfully!"
