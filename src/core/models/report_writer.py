from pydantic import BaseModel, Field
from src.core.models.influencer_scout import Influencer


class ReportWriter(BaseModel):
    """
    Represents the response model for the report writer agent.
    """

    brand_name: str = Field(
        ..., description="Name of the brand for which the report is being written"
    )
    overall_summary: str = Field(
        ..., description="Overall summary of the brand's market position and products"
    )
    influencers: list[Influencer] #Errors with Field, need to see why
    top_influencer: Influencer #Same as above
    reasons_for_recommendation: str = Field(
        ...,
        description="Reasons for recommending the influencers for the brand campaign",
    )
    top_influencer_reason: str = Field(
        ..., description="Reason for recommending the top influencer"
    )
    top_influencer_summary: str = Field(
        ...,
        description="Summary of the top influencer's profile and fit with the brand",
    )
    top_influencer_risk_assessment: str = Field(
        ..., description="Risk assessment of partnering with the top influencer"
    )
    top_influencer_previous_partnerships: list[str] = Field(
        ..., description="List of previous partnerships the top influencer has had"
    )
    top_influencer_net_sentiment: str = Field(
        ..., description="Overall sentiment of the top influencer's content"
    )
    top_influencer_brand_fit: str = Field(
        ...,
        description="How well the top influencer fits with the brand's values and target audience",
    )
