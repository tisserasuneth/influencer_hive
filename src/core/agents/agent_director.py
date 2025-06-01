from abc import ABC, abstractmethod
from agno.models.base import Model
from agno.team.team import Team
from agno.agent import Agent
from typing import List
from enum import Enum


@abstractmethod
class TeamModes(str, Enum):
    """
    Enum for team modes.
    """

    ROUTE = "route"
    COORDINATE = "coordinate"
    COLLABORATE = "collaborate"


class BaseDirectorAgent(ABC):
    """
    Base class for team director agents.
    """

    def __init__(
        self,
        name: str,
        mode: TeamModes,
        model: Model,
        members: List[Agent],
        description: str,
        instructions: List[str],
        show_members_responses: bool = True,
        **kwargs,
    ):
        self._director = Team(
            name=name,
            mode=mode,
            model=model,
            members=members,
            description=description,
            instructions=instructions,
            add_datetime_to_instructions=True,
            enable_agentic_context=True,
            share_member_interactions=True,
            show_members_responses=show_members_responses,
            markdown=True,
            **kwargs,
        )

    @property
    def director(self) -> Team:
        """
        Get the agent director.
        """
        return self._director

    def execute(self, message: str, **kwargs):
        """
        Execute the director agent.
        """
        return self._director.run(message=message, **kwargs)
