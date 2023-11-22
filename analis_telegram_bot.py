import os
import glob

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler,CallbackContext

from one_diod_result import *
from file_manager import *

TOKEN = '6199227784:AAG0ZW_X2YjfEGAAccpf5hJNHcJRO3SXs5o'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a CSV file to generate a graph.')

def process_csv(update: Update, context: CallbackContext) -> None:
    # Check if a file is sent
    if not update.message.document:
        update.message.reply_text('Please send a CSV file.')
        return
    for file in update.message.document:
        # Get the file details
        file_id = file.file_id
        file_obj = context.bot.get_file(file_id)
        file_content = file_obj.download_as_bytearray()
        file_path = "/Data"  # Set your desired directory and filename
        with open(file_path, 'wb') as file:
            file.write(file_content)
    result()
    image_files = glob.glob(os.path.join("Result", '*.png'))  # Change the file extension accordingly
    for image_path in image_files:
        with open(image_path, 'rb') as image_file:
            update.message.reply_photo(photo=image_file)
    clear_folder("Data_txt")
    clear_folder("Result")
def main() -> None:
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

