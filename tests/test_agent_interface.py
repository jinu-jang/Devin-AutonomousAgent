import pytest
from src.agent_interface import AutonomousAgent

# Define the Azure credentials for testing purposes
azure_endpoint = "https://inferenceendpointeastus.openai.azure.com/"
azure_key = "66ee2a3118184096a18e196829539064"

def test_agent_initialization():
    agent = AutonomousAgent(name="TestAgent", toolset=["autogen", "pytest", "docker"], azure_endpoint=azure_endpoint, azure_key=azure_key)
    assert agent.name == "TestAgent"
    assert "autogen" in agent.toolset

def test_perform_task():
    agent = AutonomousAgent(name="TestAgent", toolset=["autogen", "pytest", "docker"], azure_endpoint=azure_endpoint, azure_key=azure_key)
    # Assuming perform_task is a method that returns True when a task is performed successfully
    assert agent.perform_task("generate_code", {"template": "api_service"}) == True

def test_communicate():
    agent = AutonomousAgent(name="TestAgent", toolset=["autogen", "pytest", "docker"], azure_endpoint=azure_endpoint, azure_key=azure_key)
    other_agent = AutonomousAgent(name="OtherAgent", toolset=["autogen", "pytest", "docker"], azure_endpoint=azure_endpoint, azure_key=azure_key)
    # Assuming communicate is a method that returns a string response from the other agent
    assert agent.communicate("Are you ready?", other_agent) == "Yes, I am ready."

def test_run_tool():
    agent = AutonomousAgent(name="TestAgent", toolset=["autogen", "pytest", "docker"], azure_endpoint=azure_endpoint, azure_key=azure_key)
    # Assuming run_tool is a method that returns the output of the tool if successful
    assert agent.run_tool("autogen", ["--config", "autogen.json"]) != ""
    with pytest.raises(ValueError):
        agent.run_tool("nonexistent_tool", ["--config", "autogen.json"])
