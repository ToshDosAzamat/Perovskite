from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram import Update

TOKEN = '6199227784:AAG0ZW_X2YjfEGAAccpf5hJNHcJRO3SXs5o'

def echo(update: Update, context: CallbackContext) -> None:
    # Get the user's message
    user_message = update.message.text

    # Send the same message back to the user
    update.message.reply_text(f"You said: {user_message}")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the echo handler
    echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dispatcher.add_handler(echo_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
