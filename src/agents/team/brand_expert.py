from src.core.agents.agent import BaseAgent
from src.core.models.brand_expert import BrandExpert

from agno.tools.crawl4ai import Crawl4aiTools
from agno.tools.googlesearch import GoogleSearchTools


class BrandExpertAgent(BaseAgent):
    """
    Brand expert agent for providing insights on the given brand.
    """

    def __init__(self):
        name = "Brand Expert Agent"
        role = "You are an expert in brand analysis and insights."
        instructions = [
            "You will analyze the given brand name and curate information regarding the brand",
            "1. Use Google Search to find relevant information about the brand",
            "2. Use Crawl4ai to crawl websites for brand data",
            "3. Provide a comprehensive overview of the brand, values, market position and target audience",
            "4. Aim to provide insights that can help in crafting influencer recommendations",
            "5. Only use data within the last 5 years to ensure relevance",
            "6. ALWAYS include all keys shows in the response model",
            "7. If you cannot find any information, return 'No information found'",
        ]
        tools = [
            Crawl4aiTools(add_instructions=True),
            GoogleSearchTools(add_instructions=True),
        ]

        super().__init__(
            name=name,
            role=role,
            tools=tools,
            instructions=instructions,
            response_model=BrandExpert,
        )
