
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

class LibraryChatbot:
    def __init__(self):
        self.responses = {

            "hours": "Our library is open from 9 AM to 9 PM from Monday to Friday, 10 AM to 6 PM on Saturdays, and 12 PM to 5 PM on Sundays.",
            "location": "The library is located at shanti nagar pune,410111.",
            "membership": "You can become a member by filling out a membership form on our website or visiting the library. Please bring a valid ID for verification.",
            "borrowing": "Members can borrow up to 5 books at a time for a period of 2 weeks. Books can be renewed online or at the library if no one else has reserved them.",
            "events": "We have various events this month including a book club meeting, children's storytime, and an author talk. Please visit our website or the events board in the library for more details.",
            "services": "The library offers free Wi-Fi, computer access, printing and copying services, study rooms, and research assistance.",
            "thanks": "You're welcome! I'm glad I could help." ,
            "valid_id" :"you can came with any id like gov id or clg id",
            "fine":"if you not return a book within time then you have to pay 10rs per day",
            "book_types":"we have all types of book for more information check our website Shantiniketanlibrary.in  ",
            "name":"Shantiniketan Library" ,
            "return_date":"you can check your return date on our member poral",
            "fee":"Yes libraby membership is free but you have to follow rules  ",
            "more":"for more information visit our website Shantiniketanlibrary.in "


        }
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, query):
        tokens = word_tokenize(query.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in self.stop_words]
        return tokens

    def get_response(self, query):
        tokens = self.preprocess(query)

        if any(token in tokens for token in ["hour", "time", "open"]):
            return self.responses["hours"]
        elif any(token in tokens for token in ["location", "where","came","area","reach"]):
            return self.responses["location"]
        elif any(token in tokens for token in ["membership", "join", "member","account"]):
            return self.responses["membership"]
        elif any(token in tokens for token in ["borrowing", "borrow", "rule"]):
            return self.responses["borrowing"]
        elif any(token in tokens for token in ["event", "happening"]):
            return self.responses["events"]
        elif any(token in tokens for token in ["service", "offer"]):
            return self.responses["services"]
        elif any(token in tokens for token in ["thanks","thank","ok","okay"]):
            return self.responses["thanks"]

        elif any(token in tokens for token in ["id","valid"]):
            return self.responses["valid_id"]
        elif any(token in tokens for token in ["fine","late","not return"]):
            return self.responses["fine"]
        elif any(token in tokens for token in ["book","type"]):
            return self.responses["book_types"]
        elif any(token in tokens for token in ["name"]):
            return self.responses["name"]
        elif any(token in tokens for token in ["return","date"]):
            return self.responses["return_date"]
        elif any(token in tokens for token in ["fee","free","money","zero balance"]):
            return self.responses["fee"]

        elif any(token in tokens for token in ["extra","additional","more"]):
            return self.responses["more"]
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

# Main loop start here
def main():
    chatbot = LibraryChatbot()
    print("Hello! I am a library chatbot LiBO. what is your name?")
    user_name = input("You: ")
    print(f"LIBO: Hi {user_name}, I'm here to help you with your library needs.")

    print("You can ask about library hours, location, membership, borrowing rules, events, and services.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye','no','never','later','close']:
            print("LIBO: Goodbye! Have a great day!")
            break
        response = chatbot.get_response(user_input)
        print(f"LIBO: {response}")

# Running main loop
if __name__ == "__main__":
    main()