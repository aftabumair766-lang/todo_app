#!/usr/bin/env python3
"""
Data models for the Todo Application.

This module contains the core data structures used throughout the application.
"""


class Task:
    """
    Represents a single task with an ID, title, description, and completion status.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Title of the task
        description (str): Detailed description of the task
        completed (bool): Whether the task is marked as complete
    """

    def __init__(self, task_id, title, description=""):
        """
        Initialize a new Task.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task
            description (str, optional): Description of the task. Defaults to "".
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        """Return a formatted string representation of the task."""
        status = "✓ Complete" if self.completed else "○ Incomplete"
        return f"""ID: {self.id}
Title: {self.title}
Description: {self.description}
Status: {status}"""

    def __repr__(self):
        """Return a developer-friendly representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

    def to_dict(self):
        """
        Convert task to dictionary format.

        Returns:
            dict: Task data as a dictionary
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }
