def agent_reply(conversation):
    stage = conversation.get("stage", "trust")
    messages = conversation["messages"]
    last_message = messages[-1]["message"].lower()

    if stage == "trust":
        if "blocked" in last_message or "verify" in last_message:
            conversation["stage"] = "extract"
            return "Oh no 😟 I didn’t know this. What should I do now?"

        return "I’m not very familiar with these processes. Please explain slowly."

    
    if stage == "extract":
        if "upi" in last_message:
            return "I have UPI but I’m not sure how this works. Do you need my ID or will you send a request?"

        if "account" in last_message:
            return "Is this safe? Should I share savings or salary account?"

        if "link" in last_message:
            conversation["stage"] = "confirm"
            return "Before clicking, can you confirm this is official? I’m scared to make a mistake."

        return "Okay… please guide me step by step."

    
    if stage == "confirm":
        return "I’m trying to open it but network is slow. Is there another way?"

    return "Sorry, can you please repeat?"
