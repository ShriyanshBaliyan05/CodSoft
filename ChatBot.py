#This is an AI chatbot Created by Shriyansh Baliyan.
#You can Express your feelings in it (Specially crafted for students.)
#Emoji's have been added to create a sense of trust and weight to the statements and also to make chat a lil bit attractive
import random
def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode?\nBecause light attracts bugs! 😂",

        "Why did the Python programmer wear glasses?\nBecause he couldn't C! 🤓",

        "Why do Java developers wear glasses?\nBecause they don't C# 😆",

        "Why was the computer cold?\nBecause it left its Windows open! 🪟😂",

        "Why did the student bring a ladder to school?\nBecause he wanted to go to high school! 📚🤣",

        "Why did the math book look sad?\nBecause it had too many problems. 😅",

        "Why did the programmer quit his job?\nBecause he didn't get arrays. 😂",

        "Why was the computer late?\nIt had a hard drive! 🚗💻🤣",

        "What is a programmer's favorite hangout place?\nThe Foo Bar! 🍻😂",

        "Why don't scientists trust atoms?\nBecause they make up everything! 🤣"
    ]
    print(random.choice(jokes))
def chats(user):
    if "hello" in user or "hi" in user or "hey" in user:
        print("\nBot: ")
        greetings = [
            "Hello my friend! 😊",
            "Hey buddy! 😄",
            "Hi there! 🌟",
            "Nice to see you again! 🤗"
        ]
        print(random.choice(greetings))

    elif "good" in user or "fine" in user or "great" in user or "awesome" in user:
        print("\nBot: ")
        print("That's wonderful to hear! 😄")
        print("Keep smiling and keep moving forward.")
        print("I hope your day becomes even better.")

    elif "bad" in user or "not fine" in user or "feeling low" in user or "sad" in user:
        print("\nBot: ")
        print("I'm sorry to hear that. 🫂")
        print("Everyone has difficult days, and it's completely okay to feel this way.")
        print("Would you like to tell me what happened?")
        print("I am here to listen.")

    elif "marks" in user or "result" in user or "exam" in user:
        print("\nBot: ")
        print("It's okay, my friend. 🫂")
        print("Marks are only a measure of performance in one exam, not a measure of your worth.")
        print("Every successful person has faced setbacks at some point.")
        print("The important thing is to learn from the experience and keep improving.")
        print("Your future is much bigger than a single result.")
        print("Believe in yourself because you are capable of achieving great things.")
    
    elif "you are nice" in user:
        print("\nBot:")
        print("Because I have a friend like you")
        print("You are my favourite and will always be 😘")

    elif "fail" in user or "failure" in user:
        print("\nBot: ")
        print("Failure is not the opposite of success; it is part of success.")
        print("Every mistake teaches something valuable.")
        print("The fact that you tried already makes you stronger than those who never try.")
        print("Stand up, learn, and move forward. 💪")

    elif "stress" in user or "stressed" in user or "pressure" in user:
        print("\nBot: ")
        print("Life can sometimes feel overwhelming.")
        print("Try focusing on one task at a time instead of worrying about everything at once.")
        print("Take small steps and celebrate small victories.")
        print("You don't have to solve everything today.")

    elif "lonely" in user or "alone" in user:
        print("\nBot: ")
        print("Feeling lonely can be difficult. 🫂")
        print("Remember that many people experience loneliness at some point.")
        print("Try talking to a friend, family member, or someone you trust.")
        print("You matter, and your feelings matter.")

    elif "friend" in user:
        print("\nBot: ")
        print("A true friend supports you during both success and failure.")
        print("Good friends don't judge your mistakes; they help you learn from them.")
        print("Be the kind of friend you would like to have.")

    elif "motivate" in user or "motivation" in user:
        print("\nBot: ")
        print("Here is something for you:")
        print("Don't compare your Chapter 1 to someone else's Chapter 20.")
        print("Focus on progress, not perfection.")
        print("Small efforts repeated every day create extraordinary results. 🚀")

    elif "future" in user or "career" in user:
        print("\nBot: ")
        print("Your future is created by what you do today.")
        print("Keep learning, keep improving, and keep believing in yourself.")
        print("Skills, consistency, and patience can take you very far in life.")

    elif "python" in user:
        print("\nBot: ")
        print("Python is one of the most beginner-friendly programming languages.")
        print("It is widely used in AI, Machine Learning, Data Science, Web Development, and Automation.")
        print("Keep practicing daily and your coding skills will improve rapidly.")

    elif "project" in user:
        print("\nBot: ")
        print("Projects are one of the best ways to learn programming or anything else")
        print("Try breaking your project into small parts and complete them one by one.")
        print("Remember: every big project starts with a small first step.")

    elif "thank" in user:
        print("\nBot: ")
        print("You're always welcome! 😊")
        print("I'm happy if I could help even a little.")
        print("Keep learning and keep growing.")

    elif "joke" in user:
        print("\nBot: ")
        tell_joke()

    elif "who are you" in user or "your name" in user:
        print("\nBot: ")
        print("I am your friendly rule-based chatbot. 🤖")
        print("I may not know everything, but I'll always try to help.")

    elif "bye" in user or "goodbye" in user:
        print("\nBot: ")
        print("Goodbye, my friend! 👋")
        print("Take care of yourself.")
        print("Remember: difficult roads often lead to beautiful destinations.")

    elif "help" in user:
            print("\nBot:")
            print("You can talk to me about:")
            print("- Exams")
            print("- Marks")
            print("- Stress")
            print("- Motivation")
            print("- Python")
            print("- Projects")
            print("- Career")
            print("- Joke")
    else:
        print("\nBot: ")
        print("I'm not sure I understood that.")
        print("Could you tell me a little more?")
        print("I would love to continue our conversation. 😊")

def greet():
    quotes = [
        "What's on your mind today ?",
        "How are you feeling today ?",
        "How can I help you today ?",
        "How may I assist you ?"
    ]
    print("\n")
    print(random.choice(quotes))

print("╔══════════════════════════════════════════════════════════╗")
print("║                🤖 STUDENT SUPPORT CHATBOT 🤖             ║")
print("╚══════════════════════════════════════════════════════════╝")
print("║                                                          ║")
print("║                    💬 Talk Freely                        ║")
print("║                  📚 Academic Support                     ║")
print("║             🌟 Motivation & Encouragement                ║")
print("║                                                          ║")
print("║           Type your thoughts and let's chat!             ║")

while True:
    greet()
    user1 = str(input("\nYou: "))
    if not user1.strip():
        print("Come on, share something with me ")
    user1 = user1.lower()
    chats(user1)

    print("Is there anything else, I can help you with ?")
    user2 = str(input(("\nYou: ")))
    user2 = user2.lower()
    
    if "no" in user2 or "nothing" in user2:
        print("Thank you for sharing your feelings with me🤗")
        print("I am always there for you 🫂")
        print("Feel Free sharing me anything at anytime 😘👐")
        break
    elif "you already" in user2:
        print("Ahh !! Come on you are the bestest friend of mine🫂😘")
        print("It's my foremost duty to make help you🤗")
        print("Thank you for sharing your feelings with me🤗")
        print("I am always there for you 🫂")
        print("Feel Free sharing me anything at anytime 😘👐")
        break
    else:
        chats(user2)



