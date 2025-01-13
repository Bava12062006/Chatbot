import nltk
from nltk.chat.util import Chat, reflections

# Ensure necessary NLTK resources are downloaded only once
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Define pairs of input and response
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created to help you!']),
    (r'bye|goodbye', ['Goodbye! Have a nice day!', 'See you later!']),
    (r'weather', ['I am not sure about the weather, but it looks great today!']),
    (r'thanks|thank you', ['You are welcome!', 'Glad I could help!']),
    (r'(.*)', ['I am sorry, I didn’t quite get that. Could you please clarify?']),
]

# Create a chatbot instance with the defined patterns
chatbot = Chat(pairs, reflections)

# Function to initiate the chatbot conversation
def chatbot_conversation():
    print("Chatbot: Hi! I am your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_conversation()
