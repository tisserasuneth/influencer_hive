from src.core.agents.agent import BaseAgent
from src.core.models.brand_expert import BrandExpert

from agno.tools.crawl4ai import Crawl4aiTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.googlesearch import GoogleSearchTools

from textwrap import dedent


class BrandExpertAgent(BaseAgent):
    """
    Brand expert agent for providing insights on the given brand.
    """

    def __init__(self, model):
        name = "Brand Expert Agent"
        role = "You are an expert in brand analysis and insights."
        description = (
            dedent("""\
            "Responsible for analyzing given brand and/or product and providing detailed insights about it."
            """),
        )
        instructions = [
            "You are the brand analysis expert responsible for providing insights on the given brand.",
            "You will analyze brand performance and suggest improvements.",
        ]
        tools = [
            Crawl4aiTools(add_instructions=True),
            WikipediaTools(add_instructions=True),
            GoogleSearchTools(add_instructions=True),
        ]

        super().__init__(
            name=name,
            role=role,
            tools=tools,
            description=description,
            instructions=instructions,
            response_model=BrandExpert,
        )
