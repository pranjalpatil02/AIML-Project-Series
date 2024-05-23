class SimpleChatbot:
    def __init__(self):
        self.context = {}
        self.responses = {
            "hi": "Hello! How can I help you today?",
            "how are you": "I'm just a chatbot, but I'm here to help you!",
            "what is your name": "I'm your friendly chatbot.",
            "what can you do": "I can chat with you, remember things you tell me, and answer some basic questions.",
            "goodbye": "Goodbye! Have a great day!"
        }
        self.default_response = "I'm not sure how to respond to that. Can you ask something else?"
        self.questions = [
            "What's your name?",
            "How old are you?",
            "What's your favorite color?"
        ]
        self.user_data = {}

    def greet(self):
        return "Hi there! I'm your chatbot. How can I assist you?"

    def farewell(self):
        return self.responses["goodbye"]

    def handle_input(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        elif user_input in self.user_data:
            return f"You mentioned before that {self.user_data[user_input]}"
        else:
            return self.default_response

    def ask_questions(self):
        answers = {}
        for question in self.questions:
            print(question)
            answer = input()
            key = question.strip("?").lower()
            answers[key] = answer
            self.user_data[key] = answer
        return answers

    def recall_context(self):
        if self.user_data:
            return "You told me: " + ", ".join([f"{k} is {v}" for k, v in self.user_data.items()])
        else:
            return "I don't have any previous information."

    def chat(self):
        print(self.greet())
        while True:
            user_input = input()
            if user_input.lower() == "goodbye":
                print(self.farewell())
                break
            elif user_input.lower() == "remember me":
                print(self.recall_context())
            else:
                response = self.handle_input(user_input)
                print(response)
                if response == self.default_response:
                    print("Can I ask you some questions to get to know you better?")
                    self.ask_questions()
                    print("Thank you for sharing!")

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.chat()
