#!/usr/bin/env python3
"""
Mark Complete Agent - Handles task completion status operations.

This agent is responsible for toggling task completion status.
"""

try:
    from .base_agent import BaseAgent
except ImportError:
    from agents.base_agent import BaseAgent


class MarkCompleteAgent(BaseAgent):
    """
    Agent responsible for marking tasks as complete/incomplete.

    This agent toggles the completion status of tasks.
    """

    def validate_input(self, task_id):
        """
        Validate task ID for status update.

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

    def execute(self, task_id, mark_as=None):
        """
        Toggle or set task completion status.

        Args:
            task_id (int): ID of the task to update
            mark_as (bool, optional): Explicitly set status (True/False), or None to toggle

        Returns:
            tuple: (success, result_or_error)
                - If success: (True, updated_task)
                - If failure: (False, error_message)
        """
        # Validate input
        is_valid, error_msg = self.validate_input(task_id)
        if not is_valid:
            return False, error_msg

        # Get task from storage
        task = self.task_storage.get(task_id)
        if task is None:
            return False, f"Task with ID {task_id} not found"

        # Update completion status
        if mark_as is not None:
            task.completed = mark_as
        else:
            # Toggle status
            task.completed = not task.completed

        return True, task

    def get_success_message(self, task):
        """
        Get success message with status change.

        Args:
            task (Task): The updated task

        Returns:
            str: Success message
        """
        status = "complete" if task.completed else "incomplete"
        return f"\nTask '{task.title}' (ID: {task.id}) marked as {status}!"
