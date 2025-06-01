from pydantic import BaseModel, Field


class BrandContext(BaseModel):
    competitors: list[str] = Field(..., description="List of competitors in the market")
    market_trends: list[str] = Field(
        ..., description="Current market trends affecting the brand"
    )
    brand_perception: dict = Field(
        ..., description="Perception of the brand in the market"
    )
    influencer_partnerships: list[str] = Field(
        ..., description="List of influencers partnered with the brand"
    )


class BrandExpert(BaseModel):
    """
    Represents the response model for the brand expert agent.
    """

    name: str = Field(..., description="Name of the brand")
    product: str = Field(..., description="Name of the product")
    context: BrandContext = Field(
        ..., description="Contextual information about the brand and market"
    )
