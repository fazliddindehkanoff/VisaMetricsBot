import os
import logging

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from sqlalchemy.orm import sessionmaker

from models import User, engine, Base
from inline_keyboard.main_menu_btns import menu_keyboards
from inline_keyboard.constant_keyboards import back_button

from common.constants import *

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

load_dotenv()
bot_token = os.environ.get('BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    with Session() as session:
        user = session.query(User).filter(User.telegram_id == user_id).first()

        if not user:
            user = User(telegram_id=user_id)
            session.add(user)
            session.commit()

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Assalomu alaykum, Visa botiga xush kelibsiz", 
        reply_markup=menu_keyboards
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query.data == EXPRESS_VISA_CALLBACK:
        await query.edit_message_text(text="Uzur botning bu qismi xozir development bosqichida edi")
    
    elif query.data == MONTHLY_VISA_CALLBACK:
        await query.edit_message_text(text=f"Selected option: {query.data}")


def main() -> None:
    """Run the bot."""
    application = ApplicationBuilder().token(bot_token).build()
    
    start_handler = CommandHandler('start', start)
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(start_handler)
    application.add_handler(start_handler)
    
    application.run_polling()


if __name__ == '__main__':
    main()