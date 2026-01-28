def detect_scam(message: str) -> tuple[bool, float]:
    scam_keywords = [
        "urgent", "blocked", "verify", "click",
        "upi", "account", "winner", "prize"
    ]

    score = sum(1 for word in scam_keywords if word in message.lower())
    confidence = min(score / len(scam_keywords), 1.0)

    return confidence > 0.3, round(confidence, 2)
