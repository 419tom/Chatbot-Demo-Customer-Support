import json
from chatbot import classify_intent

with open("test_cases.json") as f:
    tests = json.load(f)

correct = 0

for test in tests:

    prediction = classify_intent(test["text"])

    if prediction == test["label"]:
        correct += 1

accuracy = correct / len(tests)

print(f"Intent Accuracy: {accuracy:.2%}")
