# Installation with UV - Python Package Manager

This guide explains how to set up the Todo App using **UV**, the modern Python package and project manager.

## What is UV?

UV is a fast Python package and project manager written in Rust. It's designed to replace pip, pip-tools, pipx, poetry, pyenv, and virtualenv with a single tool.

**Benefits of UV:**
- ⚡ 10-100x faster than pip
- 🔒 Reliable dependency resolution
- 🎯 Single tool for all Python project needs
- 📦 Built-in virtual environment management

---

## Prerequisites

- **WSL 2** (for Windows users)
- **Python 3.13+** (or Python 3.12.3+ for compatibility)

---

## Step 1: Install UV

### On Linux/WSL (Ubuntu)

```bash
# Install UV using the official installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

### Alternative: Using pip

```bash
pip install uv
```

---

## Step 2: Navigate to Project Directory

```bash
cd /home/umair/todo-app
```

---

## Step 3: Setup Project with UV

### Option A: Create New Virtual Environment with UV

```bash
# Create virtual environment with Python 3.13+
uv venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies using UV
uv pip install -r requirements.txt
```

### Option B: Use Specific Python Version

```bash
# Create venv with specific Python version
uv venv --python 3.13

# Activate
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### Option C: Use UV's Python Management

UV can automatically download and manage Python versions:

```bash
# UV will download Python 3.13 if not available
uv venv --python 3.13

# Activate
source .venv/bin/activate

# Install dependencies
uv pip sync requirements.txt
```

---

## Step 4: Verify Installation

```bash
# Check Python version
python --version
# Should show Python 3.13+ (or 3.12.3+ for compatibility)

# Check installed packages
uv pip list

# Should show:
# colorama 0.4.6
```

---

## Step 5: Run the Application

### Simple Version

```bash
# Run from project root
python src/main.py
```

### Agent-Based Version

```bash
# Navigate to src directory
cd src

# Run the agent version
python main_v2.py
```

---

## UV Commands Quick Reference

### Project Setup

```bash
# Create virtual environment
uv venv

# Create with specific Python version
uv venv --python 3.13

# Activate environment
source .venv/bin/activate
```

### Package Management

```bash
# Install from requirements.txt
uv pip install -r requirements.txt

# Install specific package
uv pip install colorama

# Install with exact version
uv pip install colorama==0.4.6

# Sync exact dependencies
uv pip sync requirements.txt
```

### Package Information

```bash
# List installed packages
uv pip list

# Show package details
uv pip show colorama

# Check for outdated packages
uv pip list --outdated
```

### Environment Management

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf .venv
```

---

## Python Version Compatibility

### Required: Python 3.13+

The assignment specifies Python 3.13+. To install Python 3.13:

#### Using UV (Recommended)

```bash
# UV can manage Python versions automatically
uv venv --python 3.13
```

#### Manual Installation on Ubuntu/WSL

```bash
# Add deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Install Python 3.13
sudo apt install python3.13 python3.13-venv

# Verify installation
python3.13 --version
```

### Current Compatibility: Python 3.12.3

The project currently uses Python 3.12.3, which is compatible but below the 3.13+ requirement. The code works on both versions.

**To upgrade to 3.13 with UV:**

```bash
# Remove old venv
rm -rf .venv

# Create new venv with Python 3.13
uv venv --python 3.13

# Activate
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

---

## Advantages of Using UV

### Speed Comparison

```bash
# Traditional pip (slow)
time pip install -r requirements.txt
# ~5-10 seconds

# UV (fast)
time uv pip install -r requirements.txt
# ~0.5-1 seconds ⚡
```

### Dependency Resolution

UV provides better dependency resolution:

```bash
# UV resolves conflicts automatically
uv pip install package1 package2

# UV can also compile dependencies
uv pip compile requirements.txt
```

### Lock File Generation

```bash
# Generate lock file for reproducible builds
uv pip freeze > requirements.lock

# Install from lock file
uv pip sync requirements.lock
```

---

## Migrating from pip to UV

If you have an existing setup with pip:

```bash
# 1. Deactivate current venv
deactivate

# 2. Backup current venv (optional)
mv .venv .venv.backup

# 3. Create new venv with UV
uv venv

# 4. Activate
source .venv/bin/activate

# 5. Install dependencies with UV
uv pip install -r requirements.txt

# 6. Verify everything works
python src/main.py
```

---

## Troubleshooting

### UV Command Not Found

```bash
# Reload shell configuration
source ~/.bashrc

# Or manually add to PATH
export PATH="$HOME/.cargo/bin:$PATH"

# Verify
uv --version
```

### Python 3.13 Not Available

```bash
# Let UV download it automatically
uv venv --python 3.13

# Or specify full version
uv venv --python 3.13.0
```

### Permission Errors

```bash
# Install UV with --user flag
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use pip with --user
pip install --user uv
```

### Virtual Environment Activation Issues

```bash
# Make sure you're in the project directory
cd /home/umair/todo-app

# Use absolute path
source /home/umair/todo-app/.venv/bin/activate

# Check if activated
which python
# Should show: /home/umair/todo-app/.venv/bin/python
```

---

## Development Workflow with UV

### Daily Development

```bash
# 1. Navigate to project
cd /home/umair/todo-app

# 2. Activate environment
source .venv/bin/activate

# 3. Run the app
python src/main.py

# 4. Deactivate when done
deactivate
```

### Adding New Dependencies

```bash
# Install new package
uv pip install package-name

# Update requirements.txt
uv pip freeze > requirements.txt

# Or manually add to requirements.txt and sync
echo "package-name==1.0.0" >> requirements.txt
uv pip sync requirements.txt
```

---

## UV Project Configuration (Optional)

You can create a `pyproject.toml` for better project management:

```toml
# pyproject.toml
[project]
name = "todo-app"
version = "1.0.0"
description = "Todo In-Memory Python Console App"
requires-python = ">=3.13"
dependencies = [
    "colorama==0.4.6",
]

[project.scripts]
todo = "src.main:main"
todo-agent = "src.main_v2:main"
```

Then install with:

```bash
uv pip install -e .
```

---

## Comparison: pip vs UV

| Feature | pip | UV |
|---------|-----|-----|
| Speed | Slow | ⚡ 10-100x faster |
| Dependency Resolution | Basic | Advanced |
| Virtual Environments | Separate tool (venv) | Built-in |
| Python Version Management | Manual | Automatic |
| Lock Files | Manual (pip-tools) | Built-in |
| Written In | Python | Rust |

---

## References

- **UV Documentation:** https://github.com/astral-sh/uv
- **UV Installation:** https://astral.sh/uv
- **Python 3.13 Release:** https://www.python.org/downloads/

---

## Summary

### Quick Setup Commands

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup project
cd /home/umair/todo-app
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r requirements.txt

# Run app
python src/main.py
```

UV provides a modern, fast, and reliable way to manage Python projects. It's the recommended approach for this assignment's technology stack requirements.
