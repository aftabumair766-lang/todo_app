# Todo In-Memory Python Console App - Initial Specification

## Project Overview
A simple command-line Todo application built with Python that stores tasks in memory. This is Phase I of the project, focusing on core CRUD operations.

## Target Environment
- Python 3.12+
- WSL/Linux compatible
- No external dependencies (uses only Python standard library)

## Core Features

### 1. Add Task
- **Description**: Create a new task with title and description
- **Inputs**:
  - Title (required, string)
  - Description (optional, string)
- **Outputs**:
  - Confirmation message with auto-generated task ID
  - Task is added to in-memory list
- **Validation**:
  - Title cannot be empty
  - Auto-increment ID starting from 1

### 2. Delete Task
- **Description**: Remove a task by its ID
- **Inputs**:
  - Task ID (required, integer)
- **Outputs**:
  - Confirmation message if task deleted
  - Error message if task ID not found
- **Validation**:
  - Task ID must exist in the list

### 3. Update Task
- **Description**: Modify task title and/or description
- **Inputs**:
  - Task ID (required, integer)
  - New title (optional, string)
  - New description (optional, string)
- **Outputs**:
  - Confirmation message with updated task details
  - Error message if task ID not found
- **Validation**:
  - Task ID must exist
  - At least one field (title or description) must be provided

### 4. View All Tasks
- **Description**: Display all tasks with their current status
- **Inputs**: None
- **Outputs**:
  - Formatted list showing:
    - Task ID
    - Title
    - Description
    - Status (Complete/Incomplete)
  - Message if no tasks exist
- **Display Format**:
  ```
  ID: 1
  Title: Sample Task
  Description: This is a sample task
  Status: Incomplete
  ---
  ```

### 5. Mark Task Complete/Incomplete
- **Description**: Toggle task completion status
- **Inputs**:
  - Task ID (required, integer)
- **Outputs**:
  - Confirmation message with new status
  - Error message if task ID not found
- **Validation**:
  - Task ID must exist

## Data Model

### Task Class
```python
class Task:
    - id: int (auto-generated, unique)
    - title: str (required)
    - description: str (optional, default: "")
    - completed: bool (default: False)
```

## User Interface
- Simple command-line menu with numbered options
- Clear prompts for user input
- Error handling with friendly messages
- Option to exit the application

## Technical Requirements
- All data stored in memory (no persistence)
- Modular code structure with separate functions
- Clear comments and documentation
- Follow Python naming conventions (PEP 8)
- Input validation and error handling

## Future Enhancements (Not in Phase I)
- Data persistence (file or database)
- Task categories/tags
- Due dates and priorities
- Search and filter functionality
- Task sorting options

## Success Criteria
- All 5 core features working correctly
- Clean, readable code with comments
- No runtime errors with valid inputs
- Graceful error handling for invalid inputs
- Easy to run and test on WSL/Linux
