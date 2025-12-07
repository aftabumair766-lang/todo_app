#!/usr/bin/env python3
"""
Todo In-Memory Console Application - Agent-Based Architecture
Phase I - Core CRUD Operations with Modular Agents

This module provides a simple command-line interface for managing tasks
using specialized agent classes for each operation.
All data is stored in memory and will be lost when the program exits.
"""

from storage import TaskStorage
from agents import (
    AddTaskAgent,
    DeleteTaskAgent,
    UpdateTaskAgent,
    ListTaskAgent,
    MarkCompleteAgent
)


class TodoApp:
    """
    Main Todo Application with agent-based architecture.

    This class orchestrates the various agents to perform task operations.
    """

    def __init__(self):
        """Initialize the application with storage and agents."""
        # Initialize storage
        self.storage = TaskStorage()

        # Initialize agents
        self.add_agent = AddTaskAgent(self.storage)
        self.delete_agent = DeleteTaskAgent(self.storage)
        self.update_agent = UpdateTaskAgent(self.storage)
        self.list_agent = ListTaskAgent(self.storage)
        self.mark_agent = MarkCompleteAgent(self.storage)

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 50)
        print("TODO APP - MAIN MENU (Agent-Based)")
        print("=" * 50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. View Task Summary")
        print("7. Exit")
        print("=" * 50)

    def get_int_input(self, prompt):
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

    def handle_add_task(self):
        """Handle add task operation using AddTaskAgent."""
        print("\n--- ADD NEW TASK ---")
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional): ").strip()

        success, result = self.add_agent.execute(title, description)

        if success:
            print(self.add_agent.get_success_message(result))
        else:
            print(f"\nError: {result}")

    def handle_view_tasks(self):
        """Handle view tasks operation using ListTaskAgent."""
        print("\n--- ALL TASKS ---")
        success, tasks = self.list_agent.execute()

        if success:
            print(self.list_agent.format_tasks(tasks))
        else:
            print(f"\nError: {tasks}")

    def handle_update_task(self):
        """Handle update task operation using UpdateTaskAgent."""
        print("\n--- UPDATE TASK ---")
        task_id = self.get_int_input("Enter task ID to update: ")

        if task_id is not None:
            print("Leave blank to keep current value.")
            new_title = input("Enter new title (or press Enter to skip): ").strip()
            new_description = input("Enter new description (or press Enter to skip): ").strip()

            # Convert empty strings to None
            new_title = new_title if new_title else None
            new_description = new_description if new_description else None

            success, result = self.update_agent.execute(task_id, new_title, new_description)

            if success:
                print(self.update_agent.get_success_message(result))
            else:
                print(f"\nError: {result}")

    def handle_delete_task(self):
        """Handle delete task operation using DeleteTaskAgent."""
        print("\n--- DELETE TASK ---")
        task_id = self.get_int_input("Enter task ID to delete: ")

        if task_id is not None:
            success, result = self.delete_agent.execute(task_id)

            if success:
                print(self.delete_agent.get_success_message(result))
            else:
                print(f"\nError: {result}")

    def handle_mark_complete(self):
        """Handle mark complete operation using MarkCompleteAgent."""
        print("\n--- MARK TASK COMPLETE/INCOMPLETE ---")
        task_id = self.get_int_input("Enter task ID: ")

        if task_id is not None:
            success, result = self.mark_agent.execute(task_id)

            if success:
                print(self.mark_agent.get_success_message(result))
            else:
                print(f"\nError: {result}")

    def handle_task_summary(self):
        """Display task summary statistics."""
        print("\n--- TASK SUMMARY ---")
        summary = self.list_agent.get_task_summary()

        print("\n" + "=" * 50)
        print(f"Total Tasks:      {summary['total']}")
        print(f"Completed:        {summary['complete']}")
        print(f"Incomplete:       {summary['incomplete']}")
        print("=" * 50)

    def run(self):
        """
        Main application loop.

        Displays the menu and processes user choices until exit is selected.
        """
        print("\n" + "=" * 50)
        print("WELCOME TO TODO APP - PHASE I")
        print("Agent-Based Architecture")
        print("=" * 50)

        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-7): ").strip()

            if choice == "1":
                self.handle_add_task()

            elif choice == "2":
                self.handle_view_tasks()

            elif choice == "3":
                self.handle_update_task()

            elif choice == "4":
                self.handle_delete_task()

            elif choice == "5":
                self.handle_mark_complete()

            elif choice == "6":
                self.handle_task_summary()

            elif choice == "7":
                print("\nThank you for using Todo App! Goodbye!")
                break

            else:
                print("\nError: Invalid choice. Please enter a number between 1 and 7.")


def main():
    """Entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()
