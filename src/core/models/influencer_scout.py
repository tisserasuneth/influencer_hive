from pydantic import BaseModel, Field

class Influencer(BaseModel):
    """
    Represents an influencer with their profile and follower count.
    """

    name: str = Field(..., description="Name of the influencer")
    instagram_url: str = Field(..., description="Instagram URL of the influencer")
    followers: int = Field(..., description="Number of followers the influencer has")
    niche: str = Field(..., description="Niche or category of the influencer")
    summary: str = Field(..., description="Brief summary of the influencer's profile")
    brand_fit: str = Field(
        ...,
        description="How well the influencer fits with the brand's values and target audience",
    )
    net_sentiment: str = Field(
        ..., description="Overall sentiment of the influencer's content"
    )
    risk_assessment: str = Field(
        ..., description="Risk assessment of partnering with the influencer"
    )
    previous_partnerships: list[str] = Field(
        ..., description="List of previous partnerships the influencer has had"
    )


class InfluencerScout(BaseModel):
    """
    Represents the response model for the influencer scout agent.
    """

    influencers: list[Influencer]
