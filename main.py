from agno.models.openai import OpenAIChat
from src.agents.agent_director import DirectorAgent


def main():
    """
    Main function to run the Director Agent.
    """
    model = OpenAIChat(id="gpt-4o")
    director_agent = DirectorAgent(model=model)

    brand = "Nike"
    # Execute the director agent
    response = director_agent.execute(
        message=f"Analyze the brand {brand} and provide insights."
    )
    print(response)


if __name__ == "__main__":
    main()
