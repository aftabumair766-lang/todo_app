#!/usr/bin/env python3
"""
List Task Agent - Handles task listing and display operations.

This agent is responsible for retrieving and formatting task lists.
"""

from .base_agent import BaseAgent


class ListTaskAgent(BaseAgent):
    """
    Agent responsible for listing and displaying tasks.

    This agent retrieves all tasks and formats them for display.
    """

    def execute(self, filter_status=None):
        """
        List all tasks or filter by completion status.

        Args:
            filter_status (str, optional): Filter by status ('complete', 'incomplete', or None for all)

        Returns:
            tuple: (success, result_or_error)
                - If success: (True, tasks_list)
                - If failure: (False, error_message)
        """
        # Get all tasks
        tasks = self.task_storage.get_all()

        # Apply filter if specified
        if filter_status == 'complete':
            tasks = [task for task in tasks if task.completed]
        elif filter_status == 'incomplete':
            tasks = [task for task in tasks if not task.completed]

        return True, tasks

    def format_tasks(self, tasks):
        """
        Format tasks for display.

        Args:
            tasks (list): List of tasks to format

        Returns:
            str: Formatted task list
        """
        if not tasks:
            return "\nNo tasks found. Your todo list is empty!"

        output = ["\n" + "=" * 50]
        output.append(f"TOTAL TASKS: {len(tasks)}")
        output.append("=" * 50)

        for task in tasks:
            output.append(f"\n{task}")
            output.append("-" * 50)

        return "\n".join(output)

    def get_task_summary(self):
        """
        Get a summary of tasks by status.

        Returns:
            dict: Summary with total, complete, and incomplete counts
        """
        tasks = self.task_storage.get_all()
        complete = sum(1 for task in tasks if task.completed)
        incomplete = sum(1 for task in tasks if not task.completed)

        return {
            'total': len(tasks),
            'complete': complete,
            'incomplete': incomplete
        }

    def get_success_message(self, tasks):
        """
        Get success message (not typically used for listing).

        Args:
            tasks (list): List of tasks

        Returns:
            str: Success message
        """
        return self.format_tasks(tasks)
