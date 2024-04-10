# Autonomous Agent Setup Documentation

## Introduction
This document outlines the steps taken to set up the AutonomousAgentRepo, with a focus on the installation and configuration of the 'autogen' tool. The 'autogen' tool is a Python package that facilitates the automatic generation of code and is a key component of the AutonomousAgent's capabilities.

## Environment Setup with `pyproject.toml`
The project now uses a `pyproject.toml` file for environment setup. This file specifies the build system and dependencies required for the project.

To set up the environment, follow these steps:
1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the root directory of the project.
4. Run the following command to install the project and its dependencies:
   ```bash
   python -m pip install -e .
   ```
   This will install the project in editable mode along with the dependencies specified in `pyproject.toml`.

## Installation of 'autogen'
The 'autogen' tool was installed as a Python package named 'pyautogen'. The following command was used for installation:
```bash
pip install pyautogen
```
This command installs the 'pyautogen' package to the Python site-packages directory, which is typically located at `/home/ubuntu/.local/lib/python3.10/site-packages`.

## Verification of 'autogen' Functionality
To verify the functionality of the 'autogen' library, a Python script named `test_autogen.py` was created. This script attempts to import the 'autogen' library and create an instance of `UserProxyAgent`, which is a component of the 'autogen' library.

The script was executed with the following command:
```bash
python3 test_autogen.py
```
The successful execution of this script confirmed that the 'autogen' library was installed correctly and could be used programmatically.

## Configuration of the `run_tool` Method
The `run_tool` method within the `AutonomousAgent` class, defined in `agent_interface.py`, was initially designed to execute tools that are available as executables in the system path. However, since 'autogen' is a Python package, it was necessary to modify the `run_tool` method to handle it appropriately.

The method was updated to include the following logic:
- Attempt to import the tool as a Python module using `importlib.import_module`.
- If the import is successful and the module contains a 'main' function, execute it with the provided parameters.
- If the tool is not a Python module, fall back to the original logic of checking for an executable in the system path and running it with `subprocess.run`.

Here is the updated code snippet from `agent_interface.py`:
```python
import importlib

# ... other code ...

def run_tool(self, tool_name, tool_parameters):
    # ... previous code ...

    # Check if the tool is a Python package and can be imported
    try:
        tool_module = importlib.import_module(tool_name)
        # Run the tool's main function if it's a Python package
        if hasattr(tool_module, 'main'):
            return tool_module.main(tool_parameters)
    except ImportError:
        # If the tool is not a Python package, check if it is in the system path
        if not shutil.which(tool_name):
            raise FileNotFoundError(f"The tool {tool_name} is not installed or not found in system path.")

    # ... remaining code ...
```

## Testing the `run_tool` Method
After updating the `run_tool` method, the test suite was executed again using the following command:
```bash
python3 -m pytest tests/
```
The tests validated that the `run_tool` method was functioning as expected with the 'autogen' tool.

## Conclusion
The setup process for the 'autogen' tool within the AutonomousAgentRepo was completed successfully. The 'autogen' tool is now properly installed, configured, and verified to be functional within the project environment.
