import time

memory_store = {}

def get_conversation(conversation_id):
    return memory_store.get(conversation_id, {
        "messages": [],
        "start_time": time.time(),
        "turns": 0,
        "agent_active": False,
        "stage": "trust",  # trust → extract → confirm
        "intelligence": {
            "upi_ids": [],
            "bank_accounts": [],
            "phishing_links": []
        }
    })


def update_conversation(conversation_id, message, sender="scammer"):
    convo = get_conversation(conversation_id)
    convo["messages"].append({
        "sender": sender,
        "message": message
    })
    convo["turns"] += 1
    memory_store[conversation_id] = convo
    return convo

def activate_agent(conversation_id):
    convo = get_conversation(conversation_id)
    convo["agent_active"] = True
    memory_store[conversation_id] = convo

def update_intelligence(conversation_id, extracted):
    convo = get_conversation(conversation_id)
    for key in convo["intelligence"]:
        convo["intelligence"][key] = list(
            set(convo["intelligence"][key] + extracted[key])
        )
    memory_store[conversation_id] = convo
