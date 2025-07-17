from pydantic import BaseModel, Field

class BrandPerception(BaseModel):
    sentiment: str = Field(..., description="Overall sentiment towards the brand")
    strengths: list[str] = Field(..., description="Strengths perceived by the market")
    weaknesses: list[str] = Field(..., description="Weaknesses perceived by the market")

class BrandContext(BaseModel):
    competitors: list[str] = Field(..., description="List of competitors in the market")
    market_trends: list[str] = Field(
        ..., description="Current market trends affecting the brand"
    )
    brand_perception: BrandPerception
    influencer_partnerships: list[str] = Field(
        ..., description="List of influencers partnered with the brand"
    )

class BrandExpert(BaseModel):
    """
    Represents the response model for the brand expert agent.
    """

    name: str = Field(..., description="Name of the brand")
    context: BrandContext