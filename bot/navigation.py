from telegram import CallbackQuery, Update
from telegram.ext import ContextTypes

from common.constants import MONTHLY_VISA_CALLBACK, EXPRESS_VISA_CALLBACK
from keyboards.inline.constant_keyboards import navigation_btns
from .customer_registration import get_first_name

async def get_into_monthly_visa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # extract the action and customer id from the callback data
    query = update.callback_query
    user_id = update.effective_user.id
    if query.data == MONTHLY_VISA_CALLBACK:
        await query.edit_message_text(text="Action List")
        await query.edit_message_reply_markup(navigation_btns)

    elif query.data == EXPRESS_VISA_CALLBACK:
        await query.answer("Sorry this part of bot is under development")

    elif query.data == "add_customer":
        await query.answer(text="Foydalanuvchi kiritishni boshladik unda :) Foydalanuvchi ismini kiriting")
        await context.bot.send_message(chat_id=user_id, text="Foydalanuvchi ismini kiriting")

        await get_first_name()

async def navigator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text