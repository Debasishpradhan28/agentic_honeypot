import time
from fastapi import APIRouter, Depends
from app.schemas import ScamRequest, ScamResponse, EngagementMetrics, ExtractedIntelligence
from app.core.scam_detector import detect_scam
from app.core.memory import (
    update_conversation,
    activate_agent,
    get_conversation,
    update_intelligence
)
from app.core.agent import agent_reply
from app.core.extractor import extract_intelligence
from app.utils.security import verify_api_key
from app.core.metrics import calculate_risk


router = APIRouter()

@router.post("/message", response_model=ScamResponse)
def process_message(
    data: ScamRequest,
    api_key: str = Depends(verify_api_key)
):
    convo = update_conversation(data.conversation_id, data.message)

    # Extract intelligence from all messages
    extracted = extract_intelligence(convo["messages"])
    update_intelligence(data.conversation_id, extracted)

    # Agent handoff logic
    if convo["agent_active"]:
        reply = agent_reply(convo)
    else:
        scam_detected, _ = detect_scam(data.message)
        if scam_detected:
            activate_agent(data.conversation_id)
            reply = agent_reply(convo)
        else:
            reply = "Thank you for the information."

    convo = get_conversation(data.conversation_id)
    duration = int(time.time() - convo["start_time"])
    risk_score = calculate_risk(convo["intelligence"])

    return ScamResponse(
        scam_detected=convo["agent_active"],
        confidence_score=round(risk_score / 100, 2),
        engagement_metrics=EngagementMetrics(

            conversation_turns=convo["turns"],
            engagement_duration_seconds=duration
        ),
        extracted_intelligence=ExtractedIntelligence(
            upi_ids=convo["intelligence"]["upi_ids"],
            bank_accounts=convo["intelligence"]["bank_accounts"],
            phishing_links=convo["intelligence"]["phishing_links"]
        )
    )

