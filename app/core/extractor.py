import re

UPI_REGEX = r"\b[\w.-]+@[\w.-]+\b"
BANK_REGEX = r"\b\d{9,18}\b"
URL_REGEX = r"https?://[^\s]+"

def extract_intelligence(messages):
    upi_ids = set()
    bank_accounts = set()
    phishing_links = set()

    for msg in messages:
        text = msg["message"]

        upi_ids.update(re.findall(UPI_REGEX, text))
        bank_accounts.update(re.findall(BANK_REGEX, text))
        phishing_links.update(re.findall(URL_REGEX, text))

    return {
        "upi_ids": list(upi_ids),
        "bank_accounts": list(bank_accounts),
        "phishing_links": list(phishing_links)
    }
