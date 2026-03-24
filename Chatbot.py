def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am PyBot, your AI assistant!"
    elif "help" in user_input:
        return "I can answer basic questions. Try asking me something!"
    elif "age" in user_input:
        return "I am a bot, I don't have an age!"
    elif "python" in user_input:
        return "Python is a great language for AI and Machine Learning!"
    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "AI is the simulation of human intelligence by machines!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure about that. Can you ask something else?"

print("=== PyBot - AI Chatbot ===")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print(f"PyBot: {response}\n")
    if "bye" in user_input.lower():
        break