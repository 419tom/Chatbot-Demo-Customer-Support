```mermaid
flowchart TD

A[Order Status Request]
--> B[Collect Order Number]

B --> C{Order Found?}

C -->|Yes| D[Provide Tracking Status]

C -->|No| E[Retry Collection]

E --> B

D --> F[End Conversation]
```