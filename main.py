import dotenv
import json
from agno.models.openai import OpenAIChat
from src.agents.agent_director import DirectorAgent
from agno.utils.pprint import pprint_run_response

dotenv.load_dotenv()

def main():
    """
    Main function to run the Director Agent.
    """
    model = OpenAIChat(id="gpt-4o")
    director_agent = DirectorAgent(model=model)

    brand = "Ben and Jerry's"
    # Execute the director agent
    response = director_agent.execute(
        message=f"Analyze the brand {brand} and provide the top influencers"
    )
    
    pprint_run_response(response, markdown=True)


if __name__ == "__main__":
    main()
