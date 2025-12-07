# Todo In-Memory Python Console App 🎨

A beautiful, colorful command-line Todo application built with Python. This Phase I implementation focuses on core CRUD operations with all data stored in memory, featuring a vibrant interface with colors and emojis!

## Two Implementations Available

This project includes **two versions** for learning purposes:

1. **Simple Version** (`main.py`) - Function-based implementation
2. **Agent-Based Version** (`main_v2.py`) - Modular architecture with specialized agents

## Features

- ✅ **Add Tasks**: Create new tasks with title and description
- 📋 **View Tasks**: Display all tasks with their current status
- ✏️ **Update Tasks**: Modify task details
- 🗑️ **Delete Tasks**: Remove tasks by ID
- ✅ **Mark Complete**: Toggle task completion status with visual indicators
- 📊 **Task Summary**: View statistics with progress bar (agent version only)
- 🎨 **Colorful Interface**: Beautiful colors, emojis, and formatted output
- 🎯 **Clean CLI**: Simple numbered menu for easy navigation

## Requirements

- Python 3.12 or higher
- WSL/Linux environment (or any Unix-like system)
- **colorama** - For colorful terminal output (installed automatically)

## Project Structure

```
todo-app/
├── src/
│   ├── main.py              # Simple function-based version
│   ├── main_v2.py           # Agent-based architecture version
│   ├── models.py            # Task data model (for agent version)
│   ├── storage.py           # Task storage management (for agent version)
│   ├── colors.py            # 🎨 Color utilities and formatting
│   └── agents/              # Specialized agent modules
│       ├── __init__.py
│       ├── base_agent.py
│       ├── add_task_agent.py
│       ├── delete_task_agent.py
│       ├── update_task_agent.py
│       ├── list_task_agent.py
│       └── mark_complete_agent.py
├── specs_history/
│   ├── initial_spec.md      # Original specification
│   └── agent_architecture_spec.md  # Agent architecture documentation
├── requirements.txt         # Python dependencies
├── constitution.md          # Project guidelines
├── README.md                # This file
└── CLAUDE.md                # Instructions for Claude Code
```

## Installation & Setup

### Step 1: Clone or Navigate to Project Directory

```bash
cd /home/umair/todo-app
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

You should see `(.venv)` prefix in your terminal prompt indicating the virtual environment is active.

### Step 3: Install Dependencies

```bash
# Install colorama and other dependencies
pip install -r requirements.txt
```

This will install:
- **colorama** (0.4.6) - For beautiful colorful output 🎨

### Step 4: Verify Python Version

```bash
python --version
# Should show Python 3.12 or higher
```

## Running the Application

### Version 1: Simple Function-Based (Recommended for Beginners)

```bash
# With virtual environment active
python src/main.py

# Or using Python3 directly
python3 src/main.py

# Or make it executable
chmod +x src/main.py
./src/main.py
```

### Version 2: Agent-Based Architecture (Recommended for Learning OOP)

```bash
# Navigate to src directory first
cd src

# Run the agent-based version
python main_v2.py

# Or
python3 main_v2.py
```

**Note**: The agent version must be run from the `src/` directory due to module imports.

### Which Version Should I Use?

- **`main.py`**: Best for understanding basic Python functions and logic
- **`main_v2.py`**: Best for learning object-oriented design and architecture patterns

Both versions provide the same functionality!

## Usage Guide

### Main Menu

**Simple Version (`main.py`):**
```
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit
```

**Agent Version (`main_v2.py`):**
```
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. View Task Summary          ← Extra feature!
7. Exit
```

### Example Workflow

**1. Add a new task:**
```
Enter your choice: 1
Enter task title: Buy groceries
Enter task description: Milk, eggs, bread
Task added successfully! (ID: 1)
```

**2. View all tasks:**
```
Enter your choice: 2
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: Incomplete
```

**3. Mark task as complete:**
```
Enter your choice: 5
Enter task ID: 1
Task 'Buy groceries' (ID: 1) marked as complete!
```

**4. Update task:**
```
Enter your choice: 3
Enter task ID: 1
Enter new title: Buy groceries and snacks
Enter new description: Milk, eggs, bread, chips
Task (ID: 1) updated successfully!
```

**5. Delete task:**
```
Enter your choice: 4
Enter task ID: 1
Task 'Buy groceries and snacks' (ID: 1) deleted successfully!
```

## Important Notes

- **In-Memory Storage**: All tasks are stored in memory only. When you exit the application, all data will be lost.
- **No Persistence**: This is Phase I. Future versions may include file or database persistence.
- **Input Validation**: The app includes basic input validation and error handling.

## Troubleshooting

### Virtual Environment Not Activating

If `source .venv/bin/activate` doesn't work, try:
```bash
. .venv/bin/activate
```

### Permission Denied Error

If you get a permission denied error when running the script:
```bash
chmod +x src/main.py
```

### Python Version Issues

Ensure you're using Python 3.12+:
```bash
python3 --version
```

If needed, install Python 3.12:
```bash
sudo apt update
sudo apt install python3.12
```

## Deactivating Virtual Environment

When you're done using the app:
```bash
deactivate
```

## Development

### Project Constitution

See `constitution.md` for project guidelines and development principles.

### Specifications

- `specs_history/initial_spec.md` - Original feature specifications
- `specs_history/agent_architecture_spec.md` - Agent-based architecture documentation

### Working with Claude Code

See `CLAUDE.md` for instructions on using Claude Code to modify or extend this project.

## Agent Architecture Benefits (Version 2)

The agent-based version demonstrates professional software engineering principles:

### Key Benefits

1. **Modularity**: Each agent handles one specific operation
2. **Reusability**: Agents can be used in CLI, API, or GUI contexts
3. **Testability**: Easy to unit test each agent independently
4. **Extensibility**: Add new agents without modifying existing code
5. **Maintainability**: Changes to one operation don't affect others

### Architecture Components

- **Task Model** (`models.py`): Data structure definition
- **Task Storage** (`storage.py`): In-memory data management
- **Base Agent** (`agents/base_agent.py`): Common agent functionality
- **Specialized Agents**: Each handles one operation
  - `AddTaskAgent`: Creates new tasks
  - `DeleteTaskAgent`: Removes tasks
  - `UpdateTaskAgent`: Modifies task details
  - `ListTaskAgent`: Retrieves and displays tasks
  - `MarkCompleteAgent`: Toggles completion status
- **Main App** (`main_v2.py`): Orchestrates agents

### Learning Path

1. **Start with `main.py`**: Understand basic Python and logic flow
2. **Study `models.py` and `storage.py`**: Learn about classes and encapsulation
3. **Explore agents**: See how Single Responsibility Principle works
4. **Compare versions**: Understand architectural evolution

For detailed architecture documentation, see `specs_history/agent_architecture_spec.md`.

## Future Enhancements (Planned)

- Data persistence (JSON file or SQLite database)
- Task categories and tags
- Due dates and priorities
- Search and filter functionality
- Task sorting options
- Export/import functionality

## License

This is a learning project. Feel free to use and modify as needed.

## Support

For issues or questions, refer to the project documentation in the `specs_history/` directory or consult `CLAUDE.md` for Claude Code assistance.
