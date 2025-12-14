import nltk
import random
from nltk.stem import WordNetLemmatizer

# Download required NLTK packages (run once)
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Updated intents dictionary
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "goodbye", "see you later"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thank you very much"],
        "responses": ["You're welcome!", "No problem!", "Glad to help!"]
    },
    "how_are_you": {
        "patterns": ["how are you", "how's it going", "how are you doing"],
        "responses": ["I'm fine, thank you!", "Doing great! How about you?"]
    },
    "name": {
        "patterns": ["what is your name", "who are you", "your name"],
        "responses": ["I'm your friendly chatbot!", "You can call me ChatBot."]
    },
    "default": {
        "patterns": [],
        "responses": ["Sorry, I don't understand.", "Can you rephrase that?", "I'm not sure I got that."]
    }
}

# Function to clean user input
def clean_sentence(sentence):
    words = nltk.word_tokenize(sentence.lower())  # tokenize sentence
    words = [lemmatizer.lemmatize(w) for w in words]  # lemmatize words
    return words

# Function to get response
def get_response(user_input):
    user_words = clean_sentence(user_input)
    for intent, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            pattern_words = clean_sentence(pattern)
            if all(word in user_words for word in pattern_words):
                return random.choice(intent_data["responses"])
    # If no match, return default response
    return random.choice(intents["default"]["responses"])

# Chat loop
print("Chatbot is running! (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Bye!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")
