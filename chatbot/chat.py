from chatbot.chatbot import chatbot_interaction
def chat_mode(context, name, age, sex, height, weight):
    """Handle chat interactions with the chatbot."""
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Namaste, take care!")
            break

        chatbot_output = chatbot_interaction(name, age, sex, height, weight, "", user_input, context)
        print("Bot:", chatbot_output)

        context += f"\nUser: {user_input}\nAI: {chatbot_output}"
    return context