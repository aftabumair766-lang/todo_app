#!/usr/bin/env python3
"""
Todo In-Memory Console Application
Phase I - Core CRUD Operations

This module provides a simple command-line interface for managing tasks.
All data is stored in memory and will be lost when the program exits.
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
        status = "Complete" if self.completed else "Incomplete"
        return f"""ID: {self.id}
Title: {self.title}
Description: {self.description}
Status: {status}"""


# Global task list and ID counter
tasks = []
next_id = 1


def add_task(title, description=""):
    """
    Add a new task to the task list.

    Args:
        title (str): Title of the task (required)
        description (str, optional): Description of the task. Defaults to "".

    Returns:
        Task: The newly created task, or None if validation fails
    """
    global next_id

    # Validate title
    if not title or not title.strip():
        print("Error: Title cannot be empty.")
        return None

    # Create and add the task
    task = Task(next_id, title.strip(), description.strip())
    tasks.append(task)
    next_id += 1

    print(f"\nTask added successfully! (ID: {task.id})")
    return task


def delete_task(task_id):
    """
    Delete a task by its ID.

    Args:
        task_id (int): ID of the task to delete

    Returns:
        bool: True if task was deleted, False if not found
    """
    for i, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(i)
            print(f"\nTask '{deleted_task.title}' (ID: {task_id}) deleted successfully!")
            return True

    print(f"\nError: Task with ID {task_id} not found.")
    return False


def update_task(task_id, new_title=None, new_description=None):
    """
    Update a task's title and/or description.

    Args:
        task_id (int): ID of the task to update
        new_title (str, optional): New title for the task
        new_description (str, optional): New description for the task

    Returns:
        Task: The updated task, or None if not found or no updates provided
    """
    # Validate that at least one field is provided
    if new_title is None and new_description is None:
        print("Error: Please provide at least one field to update (title or description).")
        return None

    # Find and update the task
    for task in tasks:
        if task.id == task_id:
            if new_title is not None and new_title.strip():
                task.title = new_title.strip()
            if new_description is not None:
                task.description = new_description.strip()

            print(f"\nTask (ID: {task_id}) updated successfully!")
            print(task)
            return task

    print(f"\nError: Task with ID {task_id} not found.")
    return None


def list_tasks():
    """
    Display all tasks in the task list.

    If no tasks exist, displays a message indicating the list is empty.
    """
    if not tasks:
        print("\nNo tasks found. Your todo list is empty!")
        return

    print(f"\n{'='*50}")
    print(f"TOTAL TASKS: {len(tasks)}")
    print(f"{'='*50}")

    for task in tasks:
        print(f"\n{task}")
        print("-" * 50)


def mark_complete(task_id):
    """
    Toggle the completion status of a task.

    Args:
        task_id (int): ID of the task to mark complete/incomplete

    Returns:
        Task: The updated task, or None if not found
    """
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed
            status = "complete" if task.completed else "incomplete"
            print(f"\nTask '{task.title}' (ID: {task_id}) marked as {status}!")
            return task

    print(f"\nError: Task with ID {task_id} not found.")
    return None


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("TODO APP - MAIN MENU")
    print("=" * 50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("=" * 50)


def get_int_input(prompt):
    """
    Get integer input from user with validation.

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        int: The validated integer input, or None if invalid
    """
    try:
        return int(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def main():
    """
    Main application loop.

    Displays the menu and processes user choices until exit is selected.
    """
    print("\n" + "=" * 50)
    print("WELCOME TO TODO APP - PHASE I")
    print("=" * 50)

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            # Add Task
            print("\n--- ADD NEW TASK ---")
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip()
            add_task(title, description)

        elif choice == "2":
            # View All Tasks
            print("\n--- ALL TASKS ---")
            list_tasks()

        elif choice == "3":
            # Update Task
            print("\n--- UPDATE TASK ---")
            task_id = get_int_input("Enter task ID to update: ")
            if task_id is not None:
                print("Leave blank to keep current value.")
                new_title = input("Enter new title (or press Enter to skip): ").strip()
                new_description = input("Enter new description (or press Enter to skip): ").strip()

                # Convert empty strings to None
                new_title = new_title if new_title else None
                new_description = new_description if new_description else None

                update_task(task_id, new_title, new_description)

        elif choice == "4":
            # Delete Task
            print("\n--- DELETE TASK ---")
            task_id = get_int_input("Enter task ID to delete: ")
            if task_id is not None:
                delete_task(task_id)

        elif choice == "5":
            # Mark Complete/Incomplete
            print("\n--- MARK TASK COMPLETE/INCOMPLETE ---")
            task_id = get_int_input("Enter task ID: ")
            if task_id is not None:
                mark_complete(task_id)

        elif choice == "6":
            # Exit
            print("\nThank you for using Todo App! Goodbye!")
            break

        else:
            print("\nError: Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
