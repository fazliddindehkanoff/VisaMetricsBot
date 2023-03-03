from telegram import Update
from telegram.ext import ContextTypes

from models import User
from common.constants import *
from common.get_session import get_session
from keyboards.inline.main_menu_btns import menu_keyboards

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    with get_session() as session:
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
