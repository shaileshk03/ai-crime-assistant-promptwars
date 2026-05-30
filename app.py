# AI Crime Assistant - PromptWars Version

def generate_response(query):
    query = query.lower()

    if "theft" in query:
        return "Theft cases are increasing in urban areas. Increased surveillance is recommended."

    elif "crime rate" in query:
        return "Crime rate has shown a gradual rise over the past few months."

    elif "fraud" in query:
        return "Fraud-related cases are often linked to online scams."

    else:
        return "Please ask about crime trends, statistics, or specific incidents."


# Simulate user chat
while True:
    user_input = input("Ask: ")
    if user_input == "exit":
        break
    print("AI:", generate_response(user_input))