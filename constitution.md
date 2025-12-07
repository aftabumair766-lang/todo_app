# Todo App Project Constitution

## Project Vision

This Todo application is designed to be a simple, maintainable, and educational Python project that demonstrates core programming concepts including object-oriented design, CRUD operations, and user interaction through a command-line interface.

## Core Principles

### 1. Simplicity First
- Keep the codebase simple and easy to understand
- Avoid over-engineering and unnecessary complexity
- Prefer clarity over cleverness
- Each function should have a single, well-defined purpose

### 2. Code Quality Standards
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Include docstrings for all classes and functions
- Add inline comments only where logic is not self-evident
- Maintain consistent formatting and indentation

### 3. Modularity
- Each function should do one thing well
- Avoid code duplication (DRY principle)
- Keep functions focused and cohesive
- Separate concerns (data model, business logic, user interface)

### 4. User Experience
- Provide clear and helpful error messages
- Validate all user inputs
- Give confirmation feedback for all actions
- Make the interface intuitive and self-explanatory
- Handle edge cases gracefully

### 5. Documentation
- Maintain up-to-date README with setup instructions
- Document all features in specification files
- Keep CLAUDE.md current with project evolution
- Include usage examples in documentation
- Track specification changes in specs_history/

## Code Standards

### Naming Conventions

**Variables and Functions:**
```python
# Use snake_case for variables and functions
task_id = 1
task_list = []

def add_task(title, description):
    pass
```

**Classes:**
```python
# Use PascalCase for class names
class Task:
    pass

class TaskManager:
    pass
```

**Constants:**
```python
# Use UPPER_CASE for constants
MAX_TITLE_LENGTH = 100
DEFAULT_STATUS = False
```

### Function Structure

```python
def function_name(param1, param2="default"):
    """
    Brief description of what the function does.

    Args:
        param1 (type): Description of param1
        param2 (type, optional): Description of param2. Defaults to "default".

    Returns:
        type: Description of return value
    """
    # Input validation
    if not param1:
        return None

    # Main logic
    result = process(param1, param2)

    # Return result
    return result
```

### Error Handling

- Validate inputs before processing
- Return None or False for error conditions
- Print user-friendly error messages
- Never let the application crash from user input
- Use try-except blocks for type conversions

Example:
```python
def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None
```

## Project Structure Standards

### Directory Organization

```
todo-app/
├── src/                    # Source code
│   └── main.py            # Main application entry point
├── specs_history/         # Specification documents (versioned)
│   └── initial_spec.md   # Phase I specification
├── tests/                 # Unit tests (future)
├── scripts/              # Utility scripts (future)
├── constitution.md       # This file
├── README.md            # User documentation
└── CLAUDE.md           # Claude Code instructions
```

### File Responsibilities

- **src/main.py**: Contains all core application logic for Phase I
- **specs_history/**: Historical record of all specifications
- **constitution.md**: Project guidelines and standards
- **README.md**: User-facing setup and usage documentation
- **CLAUDE.md**: Instructions for working with Claude Code

## Development Workflow

### Adding New Features

1. **Specify**: Document the feature in a new spec file
   - Create `specs_history/feature_name_spec.md`
   - Include clear requirements and acceptance criteria

2. **Review**: Review the specification for completeness
   - Ensure it aligns with project principles
   - Check for conflicts with existing features

3. **Implement**: Write the code following standards
   - Follow the code quality standards
   - Add appropriate comments and docstrings
   - Test manually with various inputs

4. **Document**: Update all relevant documentation
   - Update README.md with new feature usage
   - Update CLAUDE.md if needed
   - Add examples and edge cases

### Modifying Existing Features

1. Read the current specification in specs_history/
2. Understand the current implementation in src/
3. Make minimal changes to achieve the goal
4. Update documentation if behavior changes
5. Test all affected functionality

### Bug Fixes

1. Identify the root cause
2. Create a minimal fix
3. Add validation to prevent similar issues
4. Document the fix if it changes expected behavior

## Testing Standards

### Manual Testing Requirements

Before considering any feature complete:

1. **Happy Path**: Test the feature with valid inputs
2. **Edge Cases**: Test with boundary values
   - Empty strings
   - Very long strings
   - Negative numbers
   - Zero
   - Non-existent IDs

3. **Invalid Inputs**: Test with invalid data
   - Wrong data types
   - Null/None values
   - Special characters

4. **Integration**: Test how it works with other features

### Future: Automated Testing

When adding unit tests:
- Place test files in `tests/` directory
- Name test files as `test_<module>.py`
- Use Python's unittest or pytest framework
- Maintain test coverage above 80%

## Version Control Standards

### Commit Messages

Follow conventional commit format:

```
feat: add task priority feature
fix: prevent empty task titles
docs: update README with new features
refactor: extract input validation to separate function
test: add tests for task deletion
```

### Branching Strategy

- `main`: Stable, working code
- `dev`: Development branch for new features
- `feature/*`: Individual feature branches

## Data Management

### Phase I: In-Memory Storage

- All data stored in global variables
- Data lost on application exit
- No persistence layer
- Simple and straightforward for learning

### Future Phases: Persistence

When adding persistence:
- Use JSON for simple file-based storage
- Or SQLite for database storage
- Maintain backward compatibility
- Provide data migration utilities

## Security Considerations

### Current Phase

- Validate all user inputs
- Prevent injection attacks (even though we're not using SQL)
- Don't expose internal errors to users
- Handle exceptions gracefully

### Future Phases

- Sanitize file paths if adding file operations
- Validate data before serialization
- Use secure storage for sensitive data
- Implement user authentication if needed

## Performance Guidelines

### Current Requirements

- Response time < 1 second for all operations
- Support up to 1000 tasks without noticeable slowdown
- Minimal memory footprint

### Optimization Rules

1. Don't optimize prematurely
2. Measure before optimizing
3. Optimize only if there's a real performance issue
4. Maintain code clarity when optimizing

## Dependencies Policy

### Phase I

- **Zero external dependencies**
- Use only Python standard library
- Ensures easy setup and portability

### Future Phases

When adding dependencies:
- Justify each dependency
- Prefer well-maintained, popular libraries
- Document in requirements.txt
- Pin versions for reproducibility

## Backwards Compatibility

### Breaking Changes

When making breaking changes:
1. Document in specs_history/ with version number
2. Update README.md with migration guide
3. Consider providing a migration script
4. Bump version number appropriately

### Non-Breaking Changes

- Add new features without removing old ones
- Deprecate before removing
- Maintain default behaviors

## Review Checklist

Before considering any change complete:

- [ ] Code follows PEP 8 style guidelines
- [ ] All functions have docstrings
- [ ] Input validation is present
- [ ] Error messages are user-friendly
- [ ] Manual testing completed
- [ ] Documentation updated (README.md, specs if needed)
- [ ] No unnecessary complexity added
- [ ] Code is self-explanatory or well-commented
- [ ] Follows the single responsibility principle
- [ ] No code duplication

## Project Evolution

### Phase I (Current)
- Basic CRUD operations
- In-memory storage
- Simple CLI interface

### Phase II (Planned)
- Data persistence (JSON or SQLite)
- Task categories/tags
- Search and filter functionality

### Phase III (Future)
- Due dates and reminders
- Task priorities
- Multi-user support
- Web interface

## Modification of This Constitution

This constitution may be updated as the project evolves:

1. Propose changes in a new spec file
2. Review impact on existing code
3. Update this file
4. Document changes in specs_history/

## Conclusion

This constitution serves as a guide for maintaining code quality, consistency, and project direction. When in doubt:

1. Favor simplicity over complexity
2. Prioritize user experience
3. Maintain clear documentation
4. Follow established patterns
5. Ask before making major architectural changes

Remember: The goal is to create a maintainable, educational, and functional Todo application that serves as a learning tool and a practical utility.
