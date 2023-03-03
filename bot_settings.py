import os
import logging

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CallbackQueryHandler

from bot import conv_handler
from bot.navigation import get_into_monthly_visa

load_dotenv()
bot_token = os.environ.get('BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main() -> None:
    """Run the bot."""
    application = ApplicationBuilder().token(bot_token).build()  
    # Set up the conversation handler
    application.add_handler(CallbackQueryHandler(get_into_monthly_visa))
    application.add_handler(conv_handler)
    
    application.run_polling()


if __name__ == '__main__':
    main()