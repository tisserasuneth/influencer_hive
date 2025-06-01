from abc import ABC, abstractmethod
from agno.tools.toolkit import Toolkit
from agno.agent import Agent
from typing import List


@abstractmethod
class BaseAgent(ABC):
    """
    Base class for team agents.
    """

    def __init__(
        self,
        name: str,
        role: str,
        description: str,
        instructions: List[str],
        tools: List[Toolkit] = [],
        add_datetime_to_instructions=True,
        **kwargs,
    ):
        self._agent = Agent(
            name=name,
            role=role,
            description=description,
            instructions=instructions,
            tools=tools,
            add_datetime_to_instructions=add_datetime_to_instructions,
            **kwargs,
        )

    @property
    def agent(self) -> Agent:
        """
        Get the agent.
        """
        return self._agent
