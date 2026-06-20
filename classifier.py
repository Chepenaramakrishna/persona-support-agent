def classify_customer_persona(message):
    message = message.lower()

    if "api" in message or "code" in message or "database" in message:
        return "Technical Expert"

    elif "angry" in message or "issue" in message or "problem" in message:
        return "Frustrated User"

    else:
        return "Business Executive"