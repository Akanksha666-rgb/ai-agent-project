import agent


def chat():
    print("🤖 AI Agent Chat Interface Started")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye 👋")
            break

        response = agent.run_agent("user_123", user_input)
        print("Agent:", response)


if __name__ == "__main__":
    chat()