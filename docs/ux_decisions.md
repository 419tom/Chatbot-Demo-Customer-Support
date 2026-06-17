# Conversational UX Decisions

## Design Principles

The chatbot was designed according to four principles:

1. Clarity
2. Efficiency
3. Error Recovery
4. User Control

---

## Clarification Strategy

Ambiguous requests are clarified before routing.

Example:

User:
"My package situation is weird."

Bot:
"Are you asking about:
1. Order Status
2. Returns or Refunds
3. Something Else"

This reduces intent classification errors.

---

## Escalation Strategy

Users are escalated when:

- Multiple fallback attempts occur
- User explicitly requests an agent
- Sensitive account issues arise

---

## Tone Guidelines

Responses should be:

- Helpful
- Professional
- Concise
- Empathetic

Bad:

"Error. Invalid request."

Good:

"I'm sorry, I couldn't find that order number. Could you try again?"