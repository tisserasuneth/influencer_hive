from agno.models.base import Model
from src.core.agents.agent_director import BaseDirectorAgent, TeamModes


class DirectorAgent(BaseDirectorAgent):
    """
    Director agent for managing team interactions.
    """

    def __init__(
        self,
        model: Model,
    ):
        name = "Director Agent"
        description = "Influencer director agent for managing team interactions and crafting influencer recommendations based on brand and product."
        instructions = [
            "You are the director agent responsible for managing team interactions.",
            "You will coordinate tasks and ensure effective collaboration among team members.",
        ]

        super().__init__(
            name=name,
            mode=TeamModes.COLLABORATE,
            model=model,
            members=[],
            description=description,
            instructions=instructions,
            show_members_responses=True,
        )

    def execute(self, *args, **kwargs):
        """
        Execute the director agent with provided arguments.
        """
        return super().execute(*args, **kwargs)
