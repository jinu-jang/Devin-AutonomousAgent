from autogen import UserProxyAgent

def test_autogen_functionality():
    try:
        # Attempt to create a UserProxyAgent instance
        user_proxy = UserProxyAgent(name="test_agent")
        print("Autogen UserProxyAgent instance created successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    success = test_autogen_functionality()
    if success:
        print("Autogen is functional.")
    else:
        print("Autogen is not functional.")
