from pathlib import Path

Path("diagrams").mkdir(exist_ok=True)

diagram = """
flowchart TD

A[User asks about order]
--> B[Request Order Number]

B --> C{Order Found?}

C -->|Yes| D[Provide Status]

C -->|No| E[Retry]

E --> B
"""

with open("diagrams/order_tracking.mmd", "w") as f:
    f.write(diagram)

print("Diagram saved.")