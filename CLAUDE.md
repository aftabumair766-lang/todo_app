# Claude Code Usage Guide

This document provides instructions for using Claude Code to work with this Todo App project.

## Table of Contents

1. [Getting Started with Claude Code](#getting-started-with-claude-code)
2. [Regenerating the Project](#regenerating-the-project)
3. [Modifying Specifications](#modifying-specifications)
4. [Common Tasks](#common-tasks)
5. [Best Practices](#best-practices)

## Getting Started with Claude Code

### Prerequisites

- Claude Code CLI installed and configured
- Access to this project directory
- Familiarity with the project structure (see `README.md`)

### Opening the Project in Claude Code

```bash
# Navigate to project directory
cd /home/umair/todo-app

# Start Claude Code session
claude-code
```

## Regenerating the Project

If you need to regenerate the entire project from scratch, you can use the following prompt with Claude Code:

### Full Project Regeneration Prompt

```
Generate a complete Todo In-Memory Python Console App with the following structure:

1. Folder structure:
   - src/main.py (complete implementation)
   - specs_history/initial_spec.md (feature specifications)
   - constitution.md (project guidelines)
   - README.md (setup instructions)
   - CLAUDE.md (this file)

2. Features to implement:
   - Add Task (title, description)
   - Delete Task by ID
   - Update Task details
   - View all Tasks with status
   - Mark Task Complete/Incomplete

3. Requirements:
   - Python 3.12+ compatible
   - WSL/Linux safe
   - In-memory storage only
   - Clean, modular code with comments
   - Command-line menu interface

Please create all files ready to run.
```

### Partial Regeneration

To regenerate specific components:

**Regenerate main.py only:**
```
Based on the specifications in specs_history/initial_spec.md,
regenerate the src/main.py file with the complete Todo app implementation.
Ensure it includes the Task class and all CRUD functions.
```

**Regenerate documentation:**
```
Update the README.md file with the latest setup instructions
for the Todo app. Include sections for installation, usage,
and troubleshooting.
```

### Regenerating Agent-Based Architecture

**Full Agent-Based Project:**
```
Generate a complete Todo In-Memory Python Console App with agent-based architecture:

1. Folder structure:
   - src/models.py (Task class)
   - src/storage.py (TaskStorage class)
   - src/agents/ (specialized agent modules)
   - src/main_v2.py (main application with agents)
   - specs_history/agent_architecture_spec.md

2. Create the following agents:
   - AddTaskAgent: Handle task creation
   - DeleteTaskAgent: Handle task deletion
   - UpdateTaskAgent: Handle task updates
   - ListTaskAgent: Handle task listing and display
   - MarkCompleteAgent: Handle completion status

3. Requirements:
   - Each agent inherits from BaseAgent
   - Single Responsibility Principle
   - Dependency injection for storage
   - Consistent error handling with (success, result) tuples
   - Python 3.12+ compatible

Please create all files ready to run.
```

### Regenerating Individual Agents

**Create a new agent:**
```
Create a new SearchTaskAgent in src/agents/search_task_agent.py that:
- Inherits from BaseAgent
- Implements execute(search_term) method
- Returns tasks whose title or description contains the search term
- Follows the same pattern as other agents
- Include proper validation and error handling

Also update src/agents/__init__.py to export the new agent.
```

**Regenerate specific agent:**
```
Regenerate the AddTaskAgent in src/agents/add_task_agent.py
following the specifications in specs_history/agent_architecture_spec.md.
Ensure it includes:
- Input validation (title length, description length)
- execute() method returning (success, result) tuple
- get_success_message() method
```

**Update all agents:**
```
Update all agents to include a new method log_operation() that
prints operation details for debugging. Each agent should log:
- Agent name
- Operation type
- Timestamp
- Input parameters
```

## Modifying Specifications

### Step 1: Update Specification File

First, create a new specification file or update the existing one:

```
Create a new specification file at specs_history/v2_spec.md
that adds the following features to the Todo app:
- Task priorities (High, Medium, Low)
- Due dates for tasks
- Filter tasks by status
```

### Step 2: Review Changes

```
Review the changes needed to implement the new features
from specs_history/v2_spec.md. List all files that need
to be modified.
```

### Step 3: Implement Changes

```
Implement the features specified in specs_history/v2_spec.md.
Update src/main.py to include:
1. Priority field in Task class
2. Due date field in Task class
3. Filter function for viewing tasks by status
4. Updated menu options
```

### Step 4: Update Documentation

```
Update README.md and constitution.md to reflect the new
features added in v2_spec.md.
```

## Common Tasks

### Adding a New Feature

1. **Describe the feature:**
```
I want to add a feature to search tasks by title.
The user should be able to enter a search term and
see all tasks whose titles contain that term.
```

2. **Review implementation plan:**
```
Before implementing, show me the steps needed to add
the search functionality and which functions need to
be modified.
```

3. **Implement the feature:**
```
Implement the search functionality as discussed.
Add a new menu option "7. Search Tasks" and create
a search_tasks() function.
```

### Fixing Bugs

```
There's a bug in the update_task function where it
doesn't validate empty titles. Please fix this issue
and ensure that updating a task with an empty title
is not allowed.
```

### Refactoring Code

```
Refactor the main() function to improve readability.
Extract the menu choice handling into separate functions
for each operation.
```

### Adding Input Validation

```
Add comprehensive input validation to all functions:
- Ensure task IDs are positive integers
- Ensure titles are not empty after stripping whitespace
- Add length limits (title: 100 chars, description: 500 chars)
```

### Adding Tests

```
Create a test file at tests/test_main.py with unit tests
for all CRUD functions (add_task, delete_task, update_task,
list_tasks, mark_complete). Use Python's unittest framework.
```

### Working with Agents (Version 2)

**Create a new agent:**
```
Create a new PriorityTaskAgent in src/agents/priority_task_agent.py that:
1. Inherits from BaseAgent
2. Adds a priority field to tasks (High, Medium, Low)
3. Implements set_priority(task_id, priority) method
4. Validates priority values
5. Returns (success, result) tuple like other agents

Update src/agents/__init__.py to export it.
Update main_v2.py to add menu option for setting priority.
```

**Modify existing agent:**
```
Modify the ListTaskAgent to add a new method filter_by_priority(priority)
that returns only tasks with the specified priority level.
Ensure it follows the same pattern as the existing filter methods.
```

**Test an agent:**
```
Create unit tests for AddTaskAgent in tests/test_add_task_agent.py:
- Test successful task creation
- Test empty title validation
- Test title length validation
- Test description length validation
- Test storage integration
```

**Debug agent interaction:**
```
Add logging to all agents to help debug issues.
Each agent should log:
- When execute() is called
- Input parameters received
- Validation results
- Success or failure outcomes
```

## Best Practices

### 1. Always Reference Specifications

When requesting changes, reference the specification files:

```
Based on specs_history/initial_spec.md, ensure that the
delete_task function returns False when a task is not found,
as specified in the documentation.
```

### 2. Request Explanations

Ask Claude to explain complex changes:

```
Explain the changes you made to the Task class and why
they improve the code.
```

### 3. Incremental Changes

Make changes incrementally rather than all at once:

```
First, add the priority field to the Task class only.
Don't modify the menu or other functions yet.
```

### 4. Maintain Documentation

Always update documentation after changes:

```
I've approved the changes to add task priorities.
Now update the README.md and initial_spec.md to
document this new feature.
```

### 5. Version Control Integration

Before major changes:

```
Create a new specification file at
specs_history/priority_feature_spec.md that documents
the priority feature before we implement it.
```

## Advanced Usage

### Generating New Modules

```
Create a new module at src/utils.py with helper functions:
- validate_title(title): Validates task title
- validate_id(task_id): Validates task ID
- format_task(task): Returns formatted task string
```

### Adding Configuration

```
Create a config.py file that stores constants:
- MAX_TITLE_LENGTH = 100
- MAX_DESCRIPTION_LENGTH = 500
- DEFAULT_TASK_STATUS = False
```

### Creating Scripts

```
Create a script at scripts/demo.py that demonstrates
all features of the Todo app by automatically adding,
updating, and deleting sample tasks.
```

## Troubleshooting Claude Code

### Claude doesn't understand the context

```
Please read the following files first:
- specs_history/initial_spec.md
- src/main.py
- constitution.md

Then help me implement the requested feature.
```

### Changes don't match specifications

```
The implementation doesn't match the specification in
specs_history/initial_spec.md. Please review the spec
and correct the implementation.
```

### Need to revert changes

```
Revert src/main.py to match the implementation in
specs_history/initial_spec.md. The recent changes
introduced bugs.
```

## Template Prompts

### Feature Request Template

```
Feature: [Feature Name]

Description: [What the feature should do]

Location: [Which file(s) to modify]

Requirements:
- [Requirement 1]
- [Requirement 2]

Please implement this feature following the project's
coding standards defined in constitution.md.
```

### Bug Fix Template

```
Bug: [Description of the bug]

Location: [File and function name]

Expected Behavior: [What should happen]

Actual Behavior: [What currently happens]

Please fix this bug and add validation to prevent
similar issues.
```

### Refactoring Template

```
Refactoring Request: [What to refactor]

Current Issues:
- [Issue 1]
- [Issue 2]

Desired Outcome: [How it should be improved]

Please refactor while maintaining all existing
functionality and tests.
```

## Getting Help

If you need help with Claude Code itself:

```
How do I use Claude Code to [specific task]?
```

For project-specific help:

```
Based on this project's structure and constitution.md,
what's the best way to [specific task]?
```

## Conclusion

Claude Code is a powerful tool for iterating on this project. Use it to:
- Generate new features based on specifications
- Fix bugs and improve code quality
- Maintain documentation
- Refactor and optimize code

Always refer to `constitution.md` for project guidelines and `specs_history/` for feature specifications when working with Claude Code.
