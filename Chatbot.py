def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "your name" in user_input:
        return "I am a chatbot created to help you."
    elif "How are you" in user_input:
        return "I'm doing well,thank you for asking! how can i help you today?"
    elif "weather" in user_input:
        return "I can't check the weather, but you can use a weather app for that."
    elif "Where is your store located?" in user_input:
        return "Where is your store located?"
    elif "How do I contact support?" in user_input:
        return"You can reach our support team by emailing support@example.com or calling (123) 456-7890."
    elif "What’s the latest news?" in user_input:
        return"I can help with that. What type of news are you interested in (e.g., local, world, sports)?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

def chat():
    print("Chatbot: Hi! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input.lower():
            break

# Start the chat
chat()
