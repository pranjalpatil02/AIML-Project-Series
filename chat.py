class AdmissionChatbot:
    def __init__(self):
        self.context = {}
        self.admission_info = {
            "procedures": "The admission procedure involves submitting an online application, providing academic transcripts, and attending an interview.",
            "requirements": "The requirements include a high school diploma, letters of recommendation, and a personal statement.",
            "deadlines": "The application deadline is June 30th. Ensure all documents are submitted by this date."
        }
        self.default_response = "I'm sorry, I don't have information on that. Can you ask something else about admissions?"
        self.questions = ["What is your name?", "Which program are you interested in?", "Do you have any specific queries?"]
        self.user_data = {}

    def greet(self):
        return "Welcome to the College Admission Bot! How can I assist you with your admission queries today?"

    def farewell(self):
        return "Goodbye! Best of luck with your college application."

    def handle_input(self, user_input):
        user_input = user_input.lower()
        if "procedure" in user_input:
            return self.admission_info["procedures"]
        elif "requirement" in user_input:
            return self.admission_info["requirements"]
        elif "deadline" in user_input:
            return self.admission_info["deadlines"]
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
    bot = AdmissionChatbot()
    bot.chat()
