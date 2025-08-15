print("Hello! I'm Bot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("NehaBot: Hello! How can I help you today?")

    elif user_input == "how are you":
        print("NehaBot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("NehaBot: My name is NehaBot, your friendly chatbot.")

    elif user_input == "bye":
        print("NehaBot: Goodbye! Have a great day!")
        break

    else:
        print("NehaBot: I'm not sure how to respond to that. Can you rephrase?")
