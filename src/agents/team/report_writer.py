from src.core.agents.agent import BaseAgent
from src.core.models.report_writer import ReportWriter

from agno.tools.reasoning import ReasoningTools


class ReportWriterAgent(BaseAgent):
    """
    Report Writer Agent - Writes the final report of collected influencers following the response model.
    """

    def __init__(self):
        name = "Report Writer Agent"
        role = "You are a writer with over 20 years of experience in writing influencer portolio reports."
        instructions = [
            "1. Analyze the given information about the brand and influencers",
            "2. Write a comprehensive report for the given influencer following the provided response model",
            "3. Iterate the brand information and highlight the key points",
            "4. Showcase the selected influencers and their information",
            "5. Highlight the top influencer that you think is the best fit for the brand",
            "ALWAYS Return the list of influencers in the described format",
        ]
        tools = [
            ReasoningTools(add_instructions=True),
        ]

        super().__init__(
            name=name,
            role=role,
            tools=tools,
            instructions=instructions,
            response_model=ReportWriter,
        )
