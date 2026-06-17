# Customer Support Chatbot: Conversation Design & Evaluation

## Overview

This project demonstrates the design, implementation, and evaluation of a customer-support chatbot for an e-commerce environment. The chatbot was developed as a conversational AI case study focused on intent modeling, conversation flow design, prompt engineering, fallback handling, and user experience optimization.

The goal was to apply conversation design principles to create a user-centered support experience capable of handling common customer requests while minimizing conversational breakdowns.

---

## Project Objectives

* Design conversation flows for common customer support scenarios
* Develop an intent taxonomy based on user goals
* Create fallback and escalation pathways for ambiguous requests
* Apply prompt engineering techniques to improve response quality
* Evaluate chatbot performance using simulated user interactions
* Demonstrate conversation design and conversational UX methodologies

---

## Supported Intents

The chatbot currently supports the following customer-service intents:

| Intent           | Example Utterances               |
| ---------------- | -------------------------------- |
| Order Status     | "Where is my order?"             |
| Return Item      | "I want to return an item."      |
| Refund Status    | "When will my refund arrive?"    |
| Cancel Order     | "Can I cancel my order?"         |
| Update Address   | "I entered the wrong address."   |
| FAQ              | "What is your return policy?"    |
| Human Escalation | "I need to speak with an agent." |

---

## Intent Taxonomy Development

The intent taxonomy was developed using a task-oriented conversation design approach. 

Sources consulted included:

Cathy Pearl, Designing Voice User Interfaces (O'Reilly, 2016)
Cathy Pearl, Design for How People Think (O'Reilly, 2020)
Michael McTear, Conversational AI: Dialogue Systems, Conversational Agents, and Chatbots (Morgan & Claypool, 2020)
Alan Cooper et al., About Face: The Essentials of Interaction Design (Wiley, 2014)

### Step 1: Identify User Goals

Customer-support transcripts, support-center documentation, and common e-commerce workflows were reviewed to identify recurring customer objectives.

Examples:

* Track an order
* Return a product
* Request a refund
* Cancel a purchase
* Contact support

### Step 2: Group Similar Requests

Semantically related requests were grouped into broader intent categories.

Example:

Order Status

* "Track my package"
* "Where is my shipment?"
* "Has my order shipped?"

Return Item

* "I need to return something"
* "How do I send this back?"
* "Start a return"

### Step 3: Create Intent Definitions

Each intent was assigned:

* Intent name
* Description
* Example utterances
* Expected chatbot actions
* Escalation criteria

---

## Conversation Design Process

### Order Status Flow

User:

> Where is my order?

Bot:

> I'd be happy to help. Can you provide your order number?

User:

> 12345

Bot:

> Your order shipped on June 10 and is expected to arrive June 15.

---

### Fallback Flow

User:

> My package situation is weird.

Bot:

> I want to make sure I understand correctly. Are you asking about:
>
> 1. Order status
> 2. Returns or refunds
> 3. Something else

This fallback strategy was implemented to reduce conversational failure caused by ambiguous requests.

---

### Escalation Flow

Escalation occurs when:

* Intent confidence is low
* Multiple fallback attempts fail
* User requests a human representative
* Sensitive account issues arise

Example:

Bot:

> It looks like I may not be able to fully resolve this issue. Would you like me to connect with a support specialist?

---

## Prompt Engineering

Prompt engineering was used to:

* Improve intent recognition
* Generate more consistent responses
* Reduce ambiguity
* Improve task completion rates

Example system prompt:

"You are a customer support assistant for an e-commerce company. Identify the user's intent and provide a concise, helpful response. If the intent is unclear, ask a clarification question."

---

## Evaluation Methodology

The chatbot was evaluated using simulated customer interactions.

Evaluation criteria included:

* Intent classification accuracy
* Successful task completion
* Fallback frequency
* Escalation frequency
* Response consistency

### Example Metrics

| Metric               | Result |
| -------------------- | ------ |
| Intent Accuracy      | 91%    |
| Task Completion Rate | 84%    |
| Escalation Rate      | 11%    |
| Fallback Usage       | 15%    |

*Metrics are based on simulated evaluation conversations.*

---

## Installation

Clone the repository:

```bash
git clone https://github.com/419tom/Chatbot-Demo-Customer-Support.git
cd Chatbot-Demo-Customer-Support
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Chatbot

Start the chatbot:

```bash
python app.py
```

Example:

```text
Customer Support Bot
Type quit to exit.

> where is my order

I'd be happy to help track your order. Can you provide your order number?
```

Exit the chatbot:

```text
> quit
```

---

## Running the Evaluation

To evaluate intent classification performance:

```bash
python evaluator.py
```

Example output:

```text
Intent Accuracy: 91.00%
```

---

## Project Files

| File            | Purpose                                       |
| --------------- | --------------------------------------------- |
| app.py          | Main chatbot application                      |
| chatbot.py      | Intent classification and response generation |
| intents.json    | Intent taxonomy and example utterances        |
| evaluator.py    | Evaluation framework                          |
| test_cases.json | Evaluation dataset                            |
| docs/           | Conversation design documentation             |
| diagrams/       | Flow diagrams and conversation maps           |

---

## Extending the Project

Possible improvements:

* Add OpenAI API integration
* Implement conversation memory
* Build a web interface with Flask or Streamlit
* Add transcript logging and analytics
* Support multilingual conversations
* Implement A/B testing for prompts

```
```

---

## Technologies Used

* Python
* JSON
* OpenAI API (optional extension)
* Conversation Flow Diagrams
* Prompt Engineering
* Conversational UX Principles

---

## Key Lessons Learned

This project demonstrated the importance of:

* Intent taxonomy design
* Conversational UX
* Human-in-the-loop evaluation
* Fallback and recovery strategies
* Prompt iteration and testing

The project reflects many of the responsibilities commonly found in conversation design roles, including conversation flow creation, chatbot evaluation, transcript analysis, and user-centered AI design.

---

## Future Improvements

* LLM-powered intent classification
* Conversation memory
* Transcript analytics dashboard
* Multi-language support
* A/B testing framework for prompts
* User satisfaction measurement



