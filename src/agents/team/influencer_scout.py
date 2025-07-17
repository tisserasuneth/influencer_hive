from src.core.agents.agent import BaseAgent
from src.core.models.influencer_scout import InfluencerScout

from agno.tools.crawl4ai import Crawl4aiTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.reasoning import ReasoningTools


class InfluencerScoutAgent(BaseAgent):
    """
    Influencer Scout Agent - Scouts influencers that match the given context.
    """

    def __init__(self):
        name = "Influencer Scout Agent"
        role = "You are an expert in scouting influencers for brand campaigns."
        instructions = [
            "1. Analyze the given information about the brand",
            "2. Use the tools provided to gather relevant data about potential influencers",
            "3. Identify the 5 best influencers that align with the brand's values and target audience",
            "4. Provide a list of the 5 recommended influencers with their profiles",
            "5. Aim for influencers who have a following of at least 100,000",
            "Use Google Search to find potential influencers",
            "Use Crawl4ai to crawl websites for influencer data",
            "Use Reasoning Tools to analyze the gathered data and decide on the best influencers",
            "ALWAYS Return the list of influencers in the described format",
        ]
        tools = [
            Crawl4aiTools(add_instructions=True),
            GoogleSearchTools(add_instructions=True),
            ReasoningTools(add_instructions=True),
        ]

        super().__init__(
            name=name,
            role=role,
            tools=tools,
            instructions=instructions,
            response_model=InfluencerScout,
        )
