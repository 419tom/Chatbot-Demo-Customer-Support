from chatbot import classify_intent, generate_response

print("Customer Support Bot")
print("Type quit to exit.")

while True:

    user_input = input("> ")

    if user_input.lower() == "quit":
        break

    intent = classify_intent(user_input)

    response = generate_response(intent)

    print(response)
