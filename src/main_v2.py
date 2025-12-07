#!/usr/bin/env python3
"""
Todo In-Memory Console Application - Agent-Based Architecture
Phase I - Core CRUD Operations with Modular Agents and Colorful Interface

This module provides a simple command-line interface for managing tasks
using specialized agent classes for each operation.
All data is stored in memory and will be lost when the program exits.
"""

try:
    # Try relative imports first (when run as module)
    from .storage import TaskStorage
    from .agents import (
        AddTaskAgent,
        DeleteTaskAgent,
        UpdateTaskAgent,
        ListTaskAgent,
        MarkCompleteAgent
    )
    from .colors import (
        Colors, Emojis, print_header, print_success, print_error,
        print_task, print_welcome, print_goodbye, print_menu_option,
        print_divider, print_info, print_title, print_summary_box
    )
except ImportError:
    # Fall back to absolute imports (when run directly from src/)
    from storage import TaskStorage
    from agents import (
        AddTaskAgent,
        DeleteTaskAgent,
        UpdateTaskAgent,
        ListTaskAgent,
        MarkCompleteAgent
    )
    from colors import (
        Colors, Emojis, print_header, print_success, print_error,
        print_task, print_welcome, print_goodbye, print_menu_option,
        print_divider, print_info, print_title, print_summary_box
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
        print_header("🎯 TODO APP - AGENT-BASED", Colors.PRIMARY)
        print_menu_option(1, Emojis.ADD, "Add Task")
        print_menu_option(2, Emojis.VIEW, "View All Tasks")
        print_menu_option(3, Emojis.UPDATE, "Update Task")
        print_menu_option(4, Emojis.DELETE, "Delete Task")
        print_menu_option(5, Emojis.COMPLETE, "Mark Task Complete/Incomplete")
        print_menu_option(6, Emojis.STATS, "View Task Summary")
        print_menu_option(7, Emojis.EXIT, "Exit")
        print_divider("━", 60, Colors.PRIMARY)

    def get_int_input(self, prompt):
        """
        Get integer input from user with validation.

        Args:
            prompt (str): The prompt to display to the user

        Returns:
            int: The validated integer input, or None if invalid
        """
        try:
            return int(input(f"{Colors.HIGHLIGHT}{prompt}{Colors.RESET}"))
        except ValueError:
            print_error("Please enter a valid number.")
            return None

    def handle_add_task(self):
        """Handle add task operation using AddTaskAgent."""
        print_title(f"\n{Emojis.ADD} ADD NEW TASK", Colors.SUCCESS)
        title = input(f"{Colors.HIGHLIGHT}Enter task title: {Colors.RESET}").strip()
        description = input(f"{Colors.HIGHLIGHT}Enter task description (optional): {Colors.RESET}").strip()

        success, result = self.add_agent.execute(title, description)

        if success:
            print_success(f"Task added successfully! (ID: {result.id})")
        else:
            print_error(result)

    def handle_view_tasks(self):
        """Handle view tasks operation using ListTaskAgent."""
        success, tasks = self.list_agent.execute()

        if success:
            if not tasks:
                print_info("No tasks found. Your todo list is empty!")
            else:
                print_header(f"📋 ALL TASKS ({len(tasks)} total)", Colors.INFO)
                for task in tasks:
                    print_task(task)
        else:
            print_error(tasks)

    def handle_update_task(self):
        """Handle update task operation using UpdateTaskAgent."""
        print_title(f"\n{Emojis.UPDATE} UPDATE TASK", Colors.WARNING)
        task_id = self.get_int_input("Enter task ID to update: ")

        if task_id is not None:
            print_info("Leave blank to keep current value.")
            new_title = input(f"{Colors.HIGHLIGHT}Enter new title (or press Enter to skip): {Colors.RESET}").strip()
            new_description = input(f"{Colors.HIGHLIGHT}Enter new description (or press Enter to skip): {Colors.RESET}").strip()

            # Convert empty strings to None
            new_title = new_title if new_title else None
            new_description = new_description if new_description else None

            success, result = self.update_agent.execute(task_id, new_title, new_description)

            if success:
                print_success(f"Task (ID: {task_id}) updated successfully!")
                print_task(result)
            else:
                print_error(result)

    def handle_delete_task(self):
        """Handle delete task operation using DeleteTaskAgent."""
        print_title(f"\n{Emojis.DELETE} DELETE TASK", Colors.ERROR)
        task_id = self.get_int_input("Enter task ID to delete: ")

        if task_id is not None:
            success, result = self.delete_agent.execute(task_id)

            if success:
                print_success(f"Task '{result.title}' (ID: {task_id}) deleted successfully!")
            else:
                print_error(result)

    def handle_mark_complete(self):
        """Handle mark complete operation using MarkCompleteAgent."""
        print_title(f"\n{Emojis.COMPLETE} MARK TASK COMPLETE/INCOMPLETE", Colors.INFO)
        task_id = self.get_int_input("Enter task ID: ")

        if task_id is not None:
            success, result = self.mark_agent.execute(task_id)

            if success:
                status = "complete" if result.completed else "incomplete"
                emoji = Emojis.DONE if result.completed else Emojis.TODO
                print_success(f"{emoji} Task '{result.title}' (ID: {task_id}) marked as {status}!")
            else:
                print_error(result)

    def handle_task_summary(self):
        """Display task summary statistics."""
        summary = self.list_agent.get_task_summary()
        print_summary_box(summary['total'], summary['complete'], summary['incomplete'])

    def run(self):
        """
        Main application loop.

        Displays the menu and processes user choices until exit is selected.
        """
        print_welcome()
        print_info("Agent-Based Architecture ⚙️")

        while True:
            self.display_menu()
            choice = input(f"\n{Colors.PRIMARY}Enter your choice (1-7): {Colors.RESET}").strip()

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
                print_goodbye()
                break

            else:
                print_error("Invalid choice. Please enter a number between 1 and 7.")


def main():
    """Entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()
