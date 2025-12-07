# Todo App - Agent-Based Architecture Specification

## Overview
This specification documents the agent-based architecture implemented in Phase I of the Todo application. The architecture follows the Single Responsibility Principle, with each agent handling one specific type of operation.

## Architecture Design

### Core Components

#### 1. Task Model (`models.py`)
- **Purpose**: Data structure for tasks
- **Attributes**:
  - `id`: int - Unique identifier
  - `title`: str - Task title
  - `description`: str - Task description
  - `completed`: bool - Completion status
- **Methods**:
  - `__init__(task_id, title, description)`
  - `__str__()` - User-friendly display format
  - `__repr__()` - Developer representation
  - `to_dict()` - Convert to dictionary

#### 2. Task Storage (`storage.py`)
- **Purpose**: In-memory task storage management
- **Methods**:
  - `add(task)` - Add task to storage
  - `remove(task_id)` - Remove task by ID
  - `get(task_id)` - Retrieve task by ID
  - `get_all()` - Get all tasks
  - `get_next_id()` - Generate next unique ID
  - `count()` - Count total tasks
  - `clear()` - Clear all tasks

#### 3. Base Agent (`agents/base_agent.py`)
- **Purpose**: Foundation for all specialized agents
- **Methods**:
  - `execute(*args, **kwargs)` - Main operation (to be overridden)
  - `validate_input(*args, **kwargs)` - Input validation
  - `get_success_message()` - Success feedback
  - `get_error_message(error)` - Error feedback

### Specialized Agents

#### 1. AddTaskAgent
**File**: `agents/add_task_agent.py`

**Responsibility**: Create and add new tasks

**Methods**:
- `validate_input(title, description)` - Validate task creation input
  - Title cannot be empty
  - Title max 100 characters
  - Description max 500 characters
- `execute(title, description)` - Create and add task
  - Returns: `(success: bool, result: Task | error_msg: str)`
- `get_success_message(task)` - Format success message

**Usage**:
```python
agent = AddTaskAgent(storage)
success, result = agent.execute("Buy groceries", "Milk, eggs, bread")
if success:
    print(agent.get_success_message(result))
```

#### 2. DeleteTaskAgent
**File**: `agents/delete_task_agent.py`

**Responsibility**: Remove tasks from storage

**Methods**:
- `validate_input(task_id)` - Validate task ID
  - Must be integer
  - Must be positive
- `execute(task_id)` - Delete task
  - Returns: `(success: bool, result: Task | error_msg: str)`
- `get_success_message(task)` - Format success message

**Usage**:
```python
agent = DeleteTaskAgent(storage)
success, result = agent.execute(1)
if success:
    print(agent.get_success_message(result))
```

#### 3. UpdateTaskAgent
**File**: `agents/update_task_agent.py`

**Responsibility**: Modify task details

**Methods**:
- `validate_input(task_id, new_title, new_description)` - Validate update input
  - At least one field must be provided
  - Title cannot be empty if provided
  - Title max 100 characters
  - Description max 500 characters
- `execute(task_id, new_title, new_description)` - Update task
  - Returns: `(success: bool, result: Task | error_msg: str)`
- `get_success_message(task)` - Format success message

**Usage**:
```python
agent = UpdateTaskAgent(storage)
success, result = agent.execute(1, new_title="Updated title")
if success:
    print(agent.get_success_message(result))
```

#### 4. ListTaskAgent
**File**: `agents/list_task_agent.py`

**Responsibility**: Retrieve and display tasks

**Methods**:
- `execute(filter_status)` - List tasks with optional filter
  - `filter_status`: 'complete', 'incomplete', or None
  - Returns: `(success: bool, result: List[Task] | error_msg: str)`
- `format_tasks(tasks)` - Format tasks for display
- `get_task_summary()` - Get statistics summary
  - Returns: `{'total': int, 'complete': int, 'incomplete': int}`

**Usage**:
```python
agent = ListTaskAgent(storage)
success, tasks = agent.execute()
if success:
    print(agent.format_tasks(tasks))

summary = agent.get_task_summary()
print(f"Total: {summary['total']}")
```

#### 5. MarkCompleteAgent
**File**: `agents/mark_complete_agent.py`

**Responsibility**: Toggle task completion status

**Methods**:
- `validate_input(task_id)` - Validate task ID
  - Must be integer
  - Must be positive
- `execute(task_id, mark_as)` - Update completion status
  - `mark_as`: True/False to set explicitly, None to toggle
  - Returns: `(success: bool, result: Task | error_msg: str)`
- `get_success_message(task)` - Format success message

**Usage**:
```python
agent = MarkCompleteAgent(storage)
# Toggle status
success, result = agent.execute(1)
# Or set explicitly
success, result = agent.execute(1, mark_as=True)
if success:
    print(agent.get_success_message(result))
```

## Main Application (`main_v2.py`)

### TodoApp Class
**Purpose**: Orchestrate agents and handle user interaction

**Attributes**:
- `storage`: TaskStorage instance
- `add_agent`: AddTaskAgent instance
- `delete_agent`: DeleteTaskAgent instance
- `update_agent`: UpdateTaskAgent instance
- `list_agent`: ListTaskAgent instance
- `mark_agent`: MarkCompleteAgent instance

**Methods**:
- `display_menu()` - Show menu options
- `get_int_input(prompt)` - Validated integer input
- `handle_add_task()` - Process add task request
- `handle_view_tasks()` - Process view tasks request
- `handle_update_task()` - Process update task request
- `handle_delete_task()` - Process delete task request
- `handle_mark_complete()` - Process mark complete request
- `handle_task_summary()` - Display task statistics
- `run()` - Main application loop

## Folder Structure

```
todo-app/
├── src/
│   ├── main_v2.py           # Main application with agents
│   ├── models.py            # Task data model
│   ├── storage.py           # Task storage management
│   └── agents/              # Agent modules
│       ├── __init__.py      # Agent exports
│       ├── base_agent.py    # Base agent class
│       ├── add_task_agent.py
│       ├── delete_task_agent.py
│       ├── update_task_agent.py
│       ├── list_task_agent.py
│       └── mark_complete_agent.py
├── specs_history/
│   ├── initial_spec.md      # Original specification
│   └── agent_architecture_spec.md  # This file
├── constitution.md
├── README.md
└── CLAUDE.md
```

## Design Principles

### 1. Single Responsibility Principle
Each agent has one clear responsibility:
- AddTaskAgent: Only creates tasks
- DeleteTaskAgent: Only deletes tasks
- UpdateTaskAgent: Only updates tasks
- ListTaskAgent: Only retrieves and displays tasks
- MarkCompleteAgent: Only changes completion status

### 2. Separation of Concerns
- **Models**: Data structure definition
- **Storage**: Data persistence logic
- **Agents**: Business logic for operations
- **Main App**: User interface and orchestration

### 3. Dependency Injection
Agents receive storage through constructor, making them:
- Testable (can inject mock storage)
- Reusable (can work with different storage implementations)
- Decoupled (don't depend on global state)

### 4. Consistent Error Handling
All agents return `(success, result)` tuples:
- Success: `(True, Task or List[Task])`
- Failure: `(False, error_message)`

## Benefits of Agent Architecture

1. **Modularity**: Each agent can be developed, tested, and maintained independently
2. **Reusability**: Agents can be used in different contexts (CLI, API, GUI)
3. **Testability**: Easy to unit test each agent in isolation
4. **Extensibility**: New agents can be added without modifying existing ones
5. **Clear Contracts**: Each agent has well-defined inputs and outputs
6. **Maintainability**: Changes to one operation don't affect others

## Future Enhancements

### New Agents (Potential)
- **SearchTaskAgent**: Search tasks by keyword
- **FilterTaskAgent**: Filter tasks by various criteria
- **ExportTaskAgent**: Export tasks to file
- **ImportTaskAgent**: Import tasks from file
- **SortTaskAgent**: Sort tasks by different fields
- **StatisticsAgent**: Advanced analytics on tasks

### Storage Evolution
- **FileStorage**: Persist to JSON file
- **DatabaseStorage**: Use SQLite
- **CloudStorage**: Sync to cloud service

All agents would work unchanged with new storage implementations as long as they implement the same interface.

## Testing Strategy

Each agent can be tested independently:

```python
# Example test for AddTaskAgent
def test_add_task_agent():
    storage = TaskStorage()
    agent = AddTaskAgent(storage)

    # Test successful add
    success, task = agent.execute("Test", "Description")
    assert success == True
    assert task.title == "Test"

    # Test validation
    success, error = agent.execute("", "")
    assert success == False
    assert "empty" in error.lower()
```

## Migration from Original Version

The agent-based version (`main_v2.py`) provides the same functionality as the original (`main.py`) but with improved architecture:

**Original (`main.py`)**:
- Functions: `add_task()`, `delete_task()`, etc.
- Global task list and ID counter
- Tightly coupled to implementation

**Agent-Based (`main_v2.py`)**:
- Classes: `AddTaskAgent`, `DeleteTaskAgent`, etc.
- Encapsulated storage with `TaskStorage`
- Loose coupling through dependency injection

Both versions are maintained for comparison and learning purposes.

## Conclusion

The agent-based architecture provides a solid foundation for the Todo application that is:
- Easy to understand and maintain
- Simple to extend with new features
- Straightforward to test
- Ready for future enhancements

This architecture demonstrates good software engineering practices while keeping the implementation accessible for learning purposes.
