def chatbot():
    print("🤖 Basic Chatbot Activated!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you today?")

        elif user in ["how are you", "how r u"]:
            print("Bot: I'm doing great! Thanks for asking 😊")

        elif user in ["what is your name", "who are you"]:
            print("Bot: I'm a simple chatbot created using Python!")

        elif user in ["bye", "exit"]:
            print("Bot: Goodbye! Have a great day 👋")
            break

        elif user == "":
            print("Bot: Please type something...")

        else:
            print("Bot: Sorry, I don't understand that yet.")

chatbot() 