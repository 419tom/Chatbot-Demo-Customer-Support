import json

with open("intents.json") as f:
    INTENTS = json.load(f)


def classify_intent(user_input):

    text = user_input.lower()

    for intent, examples in INTENTS.items():

        for example in examples:

            if any(word in text for word in example.split()):
                return intent

    return "fallback"


def generate_response(intent):

    responses = {

        "order_status":
            "I'd be happy to help track your order. Can you provide your order number?",

        "return_item":
            "I can help start a return. Is the item damaged or unwanted?",

        "refund_status":
            "Refunds typically process within 5-7 business days.",

        "cancel_order":
            "I can check if your order is eligible for cancellation.",

        "fallback":
            "I'm not sure I understood. Would you like help with an order, return, refund, or cancellation?"
    }

    return responses[intent]
