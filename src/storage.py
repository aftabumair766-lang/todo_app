#!/usr/bin/env python3
"""
Task storage management for the Todo Application.

This module provides in-memory storage for tasks with ID generation.
"""


class TaskStorage:
    """
    Manages in-memory storage of tasks.

    This class handles task storage, retrieval, and ID generation.
    All tasks are stored in memory and will be lost when the application exits.
    """

    def __init__(self):
        """Initialize empty task storage."""
        self._tasks = []
        self._next_id = 1

    def add(self, task):
        """
        Add a task to storage.

        Args:
            task (Task): The task to add

        Returns:
            Task: The added task
        """
        self._tasks.append(task)
        return task

    def remove(self, task_id):
        """
        Remove a task by ID.

        Args:
            task_id (int): ID of the task to remove

        Returns:
            Task: The removed task, or None if not found
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                return self._tasks.pop(i)
        return None

    def get(self, task_id):
        """
        Get a task by ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task: The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_all(self):
        """
        Get all tasks.

        Returns:
            list: List of all tasks
        """
        return self._tasks.copy()

    def get_next_id(self):
        """
        Get the next available task ID and increment the counter.

        Returns:
            int: The next available ID
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def count(self):
        """
        Get the total number of tasks.

        Returns:
            int: Number of tasks in storage
        """
        return len(self._tasks)

    def clear(self):
        """Clear all tasks from storage."""
        self._tasks.clear()
        self._next_id = 1
