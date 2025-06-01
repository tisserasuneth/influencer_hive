from typing import List
from agno.models.base import Model

from src.core.agents.agent_director import BaseDirectorAgent, TeamModes
from src.agents.team.brand_expert import BrandExpertAgent


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
            "Get brand context from the Brand Expert Agent and use it to craft influencer recommendations.",
        ]

        brand_expert_agent: BrandExpertAgent = BrandExpertAgent().agent

        super().__init__(
            name=name,
            mode=TeamModes.COLLABORATE,
            model=model,
            members=[
                brand_expert_agent,
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
