import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
from utils import validate_card, check_card_status

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to the Credit Card Checker Bot! "
        "Send me a credit card number to check its status."
    )

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "To use this bot, simply send a credit card number. "
        "The bot will validate the number and check its status."
    )

def check_card(update: Update, context: CallbackContext) -> None:
    card_number = update.message.text.strip()
    
    # Validate the card number
    if validate_card(card_number):
        status = check_card_status(card_number)
        update.message.reply_text(status)
    else:
        update.message.reply_text("Invalid card number. Please try again.")

def main() -> None:
    # Create the Updater and pass it your bot's token
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Register a message handler for checking card numbers
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_card))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
