#!/usr/bin/env python3
"""
Color utility module for Todo Application.

This module provides colorful output using the colorama library,
making the CLI interface more visually appealing and user-friendly.
"""

from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)


class Colors:
    """Color constants for the Todo application."""

    # Foreground colors
    PRIMARY = Fore.CYAN
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    WARNING = Fore.YELLOW
    INFO = Fore.BLUE
    TASK = Fore.MAGENTA
    HIGHLIGHT = Fore.WHITE
    MUTED = Fore.LIGHTBLACK_EX

    # Special colors
    COMPLETE = Fore.GREEN
    INCOMPLETE = Fore.YELLOW

    # Styles
    BOLD = Style.BRIGHT
    RESET = Style.RESET_ALL
    DIM = Style.DIM


class Emojis:
    """Emoji constants for visual indicators."""

    # Menu emojis
    ADD = "➕"
    VIEW = "📋"
    UPDATE = "✏️"
    DELETE = "🗑️"
    COMPLETE = "✅"
    STATS = "📊"
    EXIT = "🚪"

    # Status emojis
    CHECK = "✓"
    CROSS = "✗"
    STAR = "⭐"
    ARROW = "→"
    BULLET = "•"

    # Task status
    DONE = "✅"
    TODO = "○"
    PROGRESS = "⏳"


def print_header(text, color=Colors.PRIMARY):
    """
    Print a formatted header with colors and borders.

    Args:
        text (str): Header text to display
        color (str): Color code from Colors class
    """
    border = "━" * 60
    print(f"\n{color}{Style.BRIGHT}{border}")
    print(f"{text.center(60)}")
    print(f"{border}{Style.RESET_ALL}")


def print_title(text, color=Colors.INFO):
    """
    Print a formatted title.

    Args:
        text (str): Title text to display
        color (str): Color code from Colors class
    """
    print(f"\n{color}{Style.BRIGHT}{text}{Style.RESET_ALL}")


def print_success(text):
    """
    Print a success message in green.

    Args:
        text (str): Success message
    """
    print(f"\n{Colors.SUCCESS}{Emojis.CHECK} {text}{Style.RESET_ALL}")


def print_error(text):
    """
    Print an error message in red.

    Args:
        text (str): Error message
    """
    print(f"\n{Colors.ERROR}{Emojis.CROSS} {text}{Style.RESET_ALL}")


def print_warning(text):
    """
    Print a warning message in yellow.

    Args:
        text (str): Warning message
    """
    print(f"\n{Colors.WARNING}⚠ {text}{Style.RESET_ALL}")


def print_info(text):
    """
    Print an info message in blue.

    Args:
        text (str): Info message
    """
    print(f"\n{Colors.INFO}ℹ {text}{Style.RESET_ALL}")


def print_menu_option(number, emoji, text, color=Colors.HIGHLIGHT):
    """
    Print a formatted menu option.

    Args:
        number (int): Option number
        emoji (str): Emoji icon
        text (str): Option text
        color (str): Color code
    """
    print(f"{color}{number}. {emoji}  {text}{Style.RESET_ALL}")


def print_divider(char="─", length=60, color=Colors.MUTED):
    """
    Print a divider line.

    Args:
        char (str): Character to use for divider
        length (int): Length of divider
        color (str): Color code
    """
    print(f"{color}{char * length}{Style.RESET_ALL}")


def print_task(task):
    """
    Print a formatted task with colors.

    Args:
        task: Task object to display
    """
    status_emoji = Emojis.DONE if task.completed else Emojis.TODO
    status_text = "Complete" if task.completed else "Incomplete"
    status_color = Colors.COMPLETE if task.completed else Colors.INCOMPLETE

    print(f"\n{Colors.INFO}{Style.BRIGHT}Task #{task.id}{Style.RESET_ALL}")
    print_divider("─", 60, Colors.MUTED)
    print(f"{Colors.HIGHLIGHT}Title:{Style.RESET_ALL} {Colors.TASK}{task.title}{Style.RESET_ALL}")
    print(f"{Colors.HIGHLIGHT}Description:{Style.RESET_ALL} {Colors.MUTED}{task.description or '(none)'}{Style.RESET_ALL}")
    print(f"{Colors.HIGHLIGHT}Status:{Style.RESET_ALL} {status_color}{status_emoji} {status_text}{Style.RESET_ALL}")
    print_divider("─", 60, Colors.MUTED)


def print_welcome():
    """Print a colorful welcome banner."""
    print(f"\n{Colors.PRIMARY}{Style.BRIGHT}")
    print("╔════════════════════════════════════════════════════════╗")
    print("║                                                        ║")
    print("║              🎯 WELCOME TO TODO APP 🎯                 ║")
    print("║                                                        ║")
    print("║           Organize Your Tasks Beautifully!            ║")
    print("║                                                        ║")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")


def print_goodbye():
    """Print a colorful goodbye message."""
    print(f"\n{Colors.SUCCESS}{Style.BRIGHT}")
    print("╔════════════════════════════════════════════════════════╗")
    print("║                                                        ║")
    print("║          Thank you for using Todo App! 👋              ║")
    print("║                                                        ║")
    print("║              Stay organized, stay productive!          ║")
    print("║                                                        ║")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")


def colorize(text, color, bold=False):
    """
    Return colored text.

    Args:
        text (str): Text to colorize
        color (str): Color code from Colors class
        bold (bool): Whether to make text bold

    Returns:
        str: Colored text
    """
    style = Style.BRIGHT if bold else ""
    return f"{style}{color}{text}{Style.RESET_ALL}"


def print_summary_box(total, complete, incomplete):
    """
    Print a beautiful summary box with statistics.

    Args:
        total (int): Total number of tasks
        complete (int): Number of completed tasks
        incomplete (int): Number of incomplete tasks
    """
    print(f"\n{Colors.INFO}{Style.BRIGHT}")
    print("┌────────────────────────────────────────────────────────┐")
    print("│                    TASK SUMMARY                        │")
    print("├────────────────────────────────────────────────────────┤")
    print(f"│  {Colors.HIGHLIGHT}Total Tasks:     {Colors.PRIMARY}{str(total).ljust(32)}{Colors.INFO}│")
    print(f"│  {Colors.HIGHLIGHT}Completed:       {Colors.SUCCESS}{str(complete).ljust(32)}{Colors.INFO}│")
    print(f"│  {Colors.HIGHLIGHT}Incomplete:      {Colors.WARNING}{str(incomplete).ljust(32)}{Colors.INFO}│")

    if total > 0:
        percentage = (complete / total) * 100
        bar_length = 30
        filled = int((percentage / 100) * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        print("├────────────────────────────────────────────────────────┤")
        print(f"│  {Colors.HIGHLIGHT}Progress: {Colors.SUCCESS}{bar} {percentage:.0f}%{Colors.INFO}  │")

    print("└────────────────────────────────────────────────────────┘")
    print(f"{Style.RESET_ALL}")
