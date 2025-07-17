from typing import List
from agno.models.base import Model
from agno.tools.reasoning import ReasoningTools

from src.core.agents.agent_director import BaseDirectorAgent, TeamModes
from src.agents.team.brand_expert import BrandExpertAgent
from src.agents.team.influencer_scout import InfluencerScoutAgent
from src.agents.team.report_writer import ReportWriterAgent


class DirectorAgent(BaseDirectorAgent):
    """
    Director agent for managing team interactions.
    """

    def __init__(
        self,
        model: Model,
    ):
        name: str = "Director Agent"
        description: str = "Influencer director agent for managing team interactions and crafting influencer recommendations based on brand and product."
        instructions: List[str] = [
            "You are the director agent responsible for managing team interactions.",
            "You will coordinate tasks and ensure effective collaboration among team members.",
            "1. Get brand context from the Brand Expert Agent",
            "2. Use this retrieved data to scout influencers that match the brand context",
            "3. Build a report with the gathered information about the brand and influencers",
            "4. Ensure that all team members follow the provided instructions and response models",
            "5. Always return the final report in the specified format",
            "6. Retry the agent up to 3 times if the response is not satisfactory",
            "7. If the response is not satisfactory after 3 retries, return 'No information found' and stop the execution.",
            "8. Return the final report from the report writer agent.",
            "",
        ]

        brand_expert_agent: BrandExpertAgent = BrandExpertAgent().agent
        influencer_scout_agent: InfluencerScoutAgent = InfluencerScoutAgent().agent
        report_writer_agent: ReportWriterAgent = ReportWriterAgent().agent

        super().__init__(
            name=name,
            mode=TeamModes.COLLABORATE,
            model=model,
            members=[
                brand_expert_agent,
                influencer_scout_agent,
                report_writer_agent,
            ],
            tools=[
                ReasoningTools(add_instructions=True)
            ],
            description=description,
            instructions=instructions,
            show_members_responses=True,
        )

    def execute(self, message: str, **kwargs):
        """
        Execute the director agent with provided arguments.
        """
        return super().execute(message, **kwargs)
