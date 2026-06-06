# AI Agents Codebase Guide

## Project Overview
This is a Python-based AI agents framework. The project is in early stages with the following structure:
- `app.py` - Main application entry point (currently empty, intended for agent orchestration)
- `requirements.txt` - Python dependencies
- `.env` - Environment configuration (API keys, model settings)

## Architecture & Key Patterns

### Python Environment Setup
- **Python Version**: Determined by development setup (configure via virtual environment)
- **Dependency Management**: Uses `requirements.txt` - always update here when adding packages
- **Environment Variables**: Store sensitive config (API keys, model endpoints) in `.env` file
- **Entry Point**: `app.py` will be the primary entry point for agent initialization and orchestration

### Project Structure Conventions
- Place agent implementations in dedicated modules (e.g., `agents/`, `lib/`) as the project grows
- Utility functions go in separate modules to keep `app.py` focused on orchestration
- Keep configuration logic separate from agent logic

## Development Workflows

### Local Setup
1. Create virtual environment: `python -m venv venv`
2. Activate: `source venv/bin/activate` (macOS/Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Configure `.env` with required API keys and settings

### Running the Application
- Main entry: `python app.py`
- Check environment is activated before running

### Adding Dependencies
1. Install locally: `pip install <package-name>`
2. Freeze to file: `pip freeze > requirements.txt`
3. Commit changes to both files

## Common Tasks

### Creating a New Agent
- Define agent class with clear interface (initialization, execution methods)
- Store in logical module structure under dedicated agents directory
- Document agent purpose, input parameters, and expected outputs
- Use meaningful logging for debugging agent behavior

### Debugging Agent Issues
- Check `.env` configuration is correctly set
- Verify dependencies in `requirements.txt` match installed packages
- Use Python's `logging` module for tracing execution paths
- Test agents in isolation before integration

## Integration Points & Dependencies
- **External APIs**: Configured via `.env` (model endpoints, API keys)
- **Third-party Packages**: Declared in `requirements.txt` - check versions during major updates
- **Agent Communication**: Establish clear patterns for inter-agent messaging (TBD as project grows)

## Key Principles
- **Modularity**: Each agent should have a single responsibility
- **Configuration**: Never hardcode API keys or model endpoints - use `.env`
- **Testability**: Design agents with clear inputs/outputs for unit testing
- **Logging**: Comprehensive logging for understanding agent execution flow
