from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    sender: Optional[str] = "scammer"
    message: Optional[str] = ""

class ScamRequest(BaseModel):
    conversation_id: Optional[str] = "health-check"
    message: Optional[str] = "test"
    history: Optional[List[Message]] = []

class EngagementMetrics(BaseModel):
    conversation_turns: int
    engagement_duration_seconds: int

class ExtractedIntelligence(BaseModel):
    upi_ids: List[str]
    bank_accounts: List[str]
    phishing_links: List[str]

class ScamResponse(BaseModel):
    scam_detected: bool
    confidence_score: float
    engagement_metrics: EngagementMetrics
    extracted_intelligence: ExtractedIntelligence
