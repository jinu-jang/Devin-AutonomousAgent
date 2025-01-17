import subprocess
import os
import shutil
import importlib
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

class AutonomousAgent:
    """
    This class defines the interface for an autonomous LLM-backed Agent.
    The Agent can perform software engineering tasks by running specific tools
    and interacting with other agents or human inputs.
    """

    def __init__(self, name, toolset, azure_endpoint, azure_key):
        """
        Initializes a new instance of the AutonomousAgent.

        :param name: A unique name for the agent.
        :param toolset: A collection of tools the agent can use to perform tasks.
        :param azure_endpoint: The endpoint for the Azure OpenAI service.
        :param azure_key: The key for authenticating with the Azure OpenAI service.
        """
        self.name = name
        self.toolset = toolset
        self.azure_endpoint = azure_endpoint
        self.azure_key = azure_key
        self.azure_client = TextAnalyticsClient(endpoint=azure_endpoint, credential=AzureKeyCredential(azure_key))

    def perform_task(self, task, parameters):
        """
        Performs a given task using the tools available to the agent.

        :param task: The task to be performed.
        :param parameters: Parameters required to perform the task.
        :return: The result of the task execution.
        """
        # Mock implementation for testing purposes
        if task == "generate_code" and "template" in parameters:
            return True
        return False

    def communicate(self, message, other_agent):
        """
        Communicates with another agent by sending a message.

        :param message: The message to send.
        :param other_agent: The agent to communicate with.
        :return: The response from the other agent.
        """
        # Mock implementation for testing purposes
        if message == "Are you ready?" and other_agent.name == "OtherAgent":
            return "Yes, I am ready."
        return "Message not understood."

    def run_tool(self, tool_name, tool_parameters):
        """
        Runs a specified tool with given parameters.

        :param tool_name: The name of the tool to run.
        :param tool_parameters: Parameters for the tool execution.
        :return: The output from the tool.
        """
        if tool_name not in self.toolset:
            raise ValueError(f"Tool {tool_name} is not available in the toolset.")

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

            # The actual code to run the tool using subprocess if it's not a Python package
            try:
                process = subprocess.run(
                    [tool_name] + tool_parameters,
                    capture_output=True,
                    text=True,
                    check=True
                )
                return process.stdout
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while running {tool_name}: {e}")
                return e.output

    def analyze_text(self, text):
        """
        Analyzes the given text using Azure OpenAI LLM.

        :param text: The text to analyze.
        :return: The analysis results.
        """
        response = self.azure_client.analyze_sentiment(documents=[text])
        return response if response.is_error else response[0].sentiment

# Example usage:
# agent = AutonomousAgent(name="DevAgent", toolset=["autogen", "pytest", "docker"], azure_endpoint="https://inferenceendpointeastus.openai.azure.com/", azure_key="66ee2a3118184096a18e196829539064")
# result = agent.perform_task("generate_code", {"template": "api_service"})
# response = agent.communicate("Are you ready?", other_agent=AutonomousAgent(name="OtherAgent", toolset=[]))
# tool_output = agent.run_tool("autogen", ["--config", "autogen.json"])
# sentiment = agent.analyze_text("This is a sample text for sentiment analysis.")
