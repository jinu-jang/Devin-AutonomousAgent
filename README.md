# AutonomousAgentRepo

## Project Overview
This repository contains the AutonomousAgentRepo project, which integrates Microsoft AutoGen to define the interface for an autonomous LLM-backed Agent capable of running various tools. The project focuses on software engineering tasks, leveraging the power of Large Language Models (LLMs) to automate and streamline processes.

## Integration with Microsoft AutoGen
The project utilizes Microsoft AutoGen, a tool for automating the generation of code. It is integrated into the autonomous agents to enable them to perform code generation tasks autonomously.

## Autonomous LLM-backed Agent
The core of this project is the `AutonomousAgent` class, which defines what an autonomous LLM-backed Agent is. The Agent is designed to perform tasks, communicate with other agents or humans, and run a set of predefined tools essential for software engineering.

### Agent Capabilities
- **Perform Tasks**: The Agent can perform a variety of tasks, specified by the user or determined through autonomous decision-making.
- **Communication**: The Agent can communicate with other agents or humans to coordinate on complex tasks or for reporting.
- **Run Tools**: The Agent has the capability to run tools such as 'autogen', 'pytest', and 'docker', which are essential for software development and testing.

## Setup Instructions
To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies. With the introduction of the `pyproject.toml` file, you can now set up the environment using the following command:
   ```
   python -m pip install -e .
   ```
   This will install the project in editable mode along with the dependencies specified in `pyproject.toml`.
3. To install the 'autogen' tool, run:
   ```
   pip install pyautogen
   ```
4. Verify the installation and functionality of 'autogen' by running the `test_autogen.py` script.
5. Review the `SETUP.md` file for detailed setup and configuration instructions.

## Running the Project
To run the tests and verify the functionality of the Agent, execute the following command:
```
python3 -m pytest tests/
```
This will run the test suite defined in the `tests` directory and output the results, ensuring that the Agent's methods are working as expected.

## Documentation
For more information on the project setup and the `AutonomousAgent` class, refer to the `SETUP.md` and `src/agent_interface.py` files, respectively.

## Contributions
Contributions to the AutonomousAgentRepo are welcome. Please read the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
