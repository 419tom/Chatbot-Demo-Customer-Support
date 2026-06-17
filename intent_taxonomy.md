# Intent Taxonomy

## Overview

The intent taxonomy was developed using principles from task-oriented dialogue system design and conversation design literature.

### References

- Cathy Pearl (2016), *Designing Voice User Interfaces*
- Michael McTear (2020), *Conversational AI: Dialogue Systems, Conversational Agents, and Chatbots*

The taxonomy is organized around customer goals rather than linguistic form.

---

## Intent Hierarchy

Customer Support

├── Order Management

│ ├── Order Status

│ ├── Cancel Order

│ └── Update Address

├── Returns & Refunds

│ ├── Return Item

│ └── Refund Status

├── Information Requests

│ └── FAQ

└── Escalation

└── Human Agent

---

## Intent Definitions

### Order Status

Goal:
Track an existing order.

Example Utterances:

- Where is my order?
- Track my package.
- Has my shipment arrived?

Expected Action:

- Request order number
- Retrieve shipping status

---

### Return Item

Goal:
Begin a return process.

Example Utterances:

- I need to return something.
- Start a return.
- Send this item back.

Expected Action:

- Verify eligibility
- Provide return instructions

---

### Refund Status

Goal:
Check refund progress.

Example Utterances:

- Where is my refund?
- Has my refund been processed?

Expected Action:

- Retrieve refund information

---

### Human Agent

Goal:
Escalate to live support.

Example Utterances:

- I need a human.
- Let me talk to an agent.

Expected Action:

- Transfer conversation