## Project Name 

Agentic Honey-Pot for Scam Detection & Intelligence Extraction

## Overview

The Agentic Honey-Pot API is an AI-powered autonomous system designed to detect scam messages and actively engage scammers using a believable AI persona.
Once scam intent is detected, the system hands off the interaction to an autonomous AI agent that conducts multi-turn conversations to extract actionable scam intelligence such as:

-UPI IDs

-Bank account numbers

-Phishing URLs

The API is compatible with Mock Scammer API–based evaluation systems and returns structured JSON output for automated scoring.

## Key Capabilities

1.Scam intent detection

2.Autonomous AI agent handoff

3.Multi-turn conversation memory

4.Intelligence extraction

5.Engagement metrics tracking


## Base URL
https://agentic-honeypot-umjs.onrender.com


## Endpoint Details
➤ POST /api/message

Receives incoming messages from the Mock Scammer API, analyzes scam intent, engages the autonomous AI agent if required, and returns extracted intelligence.



## Processing Logic

1.Incoming message is analyzed for scam intent

2.If scam intent is detected:

-Autonomous AI agent is activated

-Agent continues conversation independently

3.Multi-turn conversation is maintained using conversation_id

4.Intelligence is extracted silently

5.Engagement metrics are calculated

6.Structured JSON response is returned

## Multi-Turn Conversation Handling

1.Conversation continuity is maintained using conversation_id

2.Once the AI agent is activated, it remains active for the entire session

3.Scam detection is not re-triggered for the same conversation

## Performance Characteristics

1.Low-latency response

2.Stateless API with in-memory session handling

3.Deterministic extraction logic

4.Stable output for automated evaluation

## Ethical & Safety Considerations

1.No interaction with real users

2.No retaliation or malicious action

3.Controlled honeypot simulation only

4.Designed strictly for research and prevention


## Conclusion

This API demonstrates a real-world agentic AI system that goes beyond detection by actively engaging scammers to extract valuable intelligence, making it suitable for:

1.Cybercrime investigation

2.Financial fraud prevention

3.Academic research

4.Hackathon evaluation


































Secure API key–based access

Low-latency REST API
