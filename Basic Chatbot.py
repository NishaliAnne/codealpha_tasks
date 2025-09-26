# Advanced Rule-Based Chatbot

# Predefined responses dictionary
RESPONSES = {
    "greetings": ["hi", "hello", "hey", "good morning", "good afternoon"],
    "farewell": ["bye", "goodbye", "see you", "exit"],
    "how_are_you": ["how are you", "how are you?", "how's it going"],
    "feelings": ["i am fine", "i am good", "i am sad", "i am happy"],
    "name": ["what is your name", "who are you"]
}

REPLIES = {
    "greetings": "Hi! 👋 How can I help you today?",
    "farewell": "Goodbye! 👋 Have a nice day!",
    "how_are_you": "I'm fine, thanks for asking! 😊",
    "feelings": "Glad to hear that!" ,
    "name": "I am ChatBot, your friendly assistant 🤖",
    "default": "Sorry, I don't understand that. 🤔"
}

def get_response(user_input):
    """Return a response based on user input"""
    user_input = user_input.lower()

    # Check each category
    for category, phrases in RESPONSES.items():
        if user_input in phrases:
            return REPLIES.get(category)
    # If nothing matches, return default reply
    return REPLIES["default"]

def chat():
    """Main chat loop"""
    print("🤖 Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        response = get_response(user_input)
        print("Bot:", response)
        if user_input.lower() in RESPONSES["farewell"]:
            break

if __name__ == "__main__":
    chat()

