def chatbot():
    print("Welcome to BookBot! How can I help you today?")
    while True:
        user = input("You: ").lower()

        if "buy" in user or "purchase" in user:
            print("Bot: You can buy books from our website: www.bookstore.com.")
        elif "return" in user:
            print("Bot: Please visit www.bookstore.com/returns to initiate a return.")
        elif "recommend" in user or "suggest" in user:
            print("Bot: I recommend 'Atomic Habits' and 'The Alchemist'!")
        elif "thank" in user:
            print("Bot: You're welcome!")
        elif "bye" in user or "exit" in user:
            print("Bot: Goodbye! Have a great day 😊")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")


chatbot()
