#!/usr/bin/env python3
"""
Base Agent class for all task operation agents.

This module provides the foundation for all specialized agents in the application.
"""


class BaseAgent:
    """
    Base class for all task operation agents.

    This class provides common functionality and interface that all agents inherit.
    Each agent should implement the execute() method to perform its specific operation.
    """

    def __init__(self, task_storage):
        """
        Initialize the base agent with task storage.

        Args:
            task_storage (TaskStorage): The storage instance managing tasks
        """
        self.task_storage = task_storage

    def execute(self, *args, **kwargs):
        """
        Execute the agent's primary operation.

        This method should be overridden by subclasses to implement
        specific functionality.

        Raises:
            NotImplementedError: If not implemented by subclass
        """
        raise NotImplementedError("Subclasses must implement execute() method")

    def validate_input(self, *args, **kwargs):
        """
        Validate input parameters before execution.

        This method can be overridden by subclasses for custom validation.

        Returns:
            tuple: (is_valid, error_message)
        """
        return True, None

    def get_success_message(self):
        """
        Get the success message for the operation.

        Returns:
            str: Success message
        """
        return "Operation completed successfully"

    def get_error_message(self, error):
        """
        Get a user-friendly error message.

        Args:
            error (str): Error description

        Returns:
            str: Formatted error message
        """
        return f"Error: {error}"
