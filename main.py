from llm_agent import agent_executor

def main():
    print("Welcome to Multi-AI Assistant!")
    chat_history = []  # Keep track of chat history

    while True:
        query = input("\nAsk something (or type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Goodbye!")
            break

        # Include chat_history in input dictionary
        response = agent_executor.invoke({"input": query, "chat_history": chat_history})

        # Store interaction history if needed
        chat_history.append({"input": query, "output": response})

        print("\nResponse:", response)

if __name__ == "__main__":
    main()
