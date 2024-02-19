import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Importing credentials from config.py
from config import BOT_TOKEN

# Define your sample questions and answers
qa_pairs = {
    "How are you?": "I'm good, thank you!",
    "What is your name?": "I'm a bot designed to help you.",
    "Who created you?": "I was created by [Your Name]",
    "Tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "Tell me a fact": "Did you know that the shortest war in history was between Britain and Zanzibar on August 27, 1896? It lasted only 38 minutes.",
    # Add more questions and answers as needed
}

# Define a function to handle incoming messages
def message_handler(update: Update, context: CallbackContext) -> None:
    # Get the text of the incoming message
    message_text = update.message.text

    # Check if the message text is in our question-answer pairs
    if message_text in qa_pairs:
        # Reply with the corresponding answer
        update.message.reply_text(qa_pairs[message_text])
    else:
        # If the question is not recognized, reply with a default message
        update.message.reply_text("I'm sorry, I don't understand that question.")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Define a message handler
    message_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)

    # Add the message handler to the dispatcher
    dispatcher.add_handler(message_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
