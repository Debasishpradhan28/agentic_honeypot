def calculate_risk(intelligence):
    score = 0

    if intelligence["upi_ids"]:
        score += 30
    if intelligence["bank_accounts"]:
        score += 40
    if intelligence["phishing_links"]:
        score += 30

    return min(score, 100)
