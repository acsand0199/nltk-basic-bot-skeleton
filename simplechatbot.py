import random
from nltk.chat.util import Chat, reflections
import nltk
nltk.download('punkt') #downloads the required data
import datetime 

def main():
    current_date = datetime.datetime.now() #gets the current date and time 
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") #formats date and time

    pairs = [
        ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
        ["how are you", ["I'm doing well, thank you!", "I'm good, thanks for asking."]],  # These are conversation pairs.  Each pair consists of a pattern (a regular expression) and a list of possible responses. 
        ["what's your name", ["I'm a chatbot.", "You can call me ChatBot."]],
        ["bye|goodbye", ["Goodbye!", "Have a great day!", "See you later!"]],
        [r".*\bdate\b.*", ["The current date and time is:" + formatted_date]],
        ["How old are you?", ["I was born on 9-22-2023"]],
    ]

    chatbot = Chat(pairs, reflections) #creates a instance of the 'Chat class' and provide it with different patterns and responses.  Pairs are conversation pairs.  Reflections is a predefined dictionary provided by NLTK.  It contains reflection pairs for pronoun substitution (e.g., "I" to "you" and vice versa). It helps the chatbot generate responses that make sense in the context of the conversation 

    print("Hello! My name is Reece, your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break   #breaks the loop if the user types exit
        response = chatbot.respond(user_input) #respond(user_input) is a method provided by the Chat class. When you call this method with the input, the chatbot attempts to find a matching pattern among the patterns
        print("ChatBot:", response)
    

if __name__ == "__main__":
    main()




