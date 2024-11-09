import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to hold all configuration variables."""
    
    # Telegram Bot Token
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # Payment API Configuration
    PAYMENT_API_URL = os.getenv("PAYMENT_API_URL", "https://api.example.com/check")
    PAYMENT_API_KEY = os.getenv("PAYMENT_API_KEY")

    # Other Configuration Variables
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ['true', '1', 't']

    # Log file configuration
    LOG_FILE = os.getenv("LOG_FILE", "bot.log")

# Usage Example:
# You can access the configuration variables like this:
# from config import Config
# print(Config.TELEGRAM_BOT_TOKEN)
