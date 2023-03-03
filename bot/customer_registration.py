from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from keyboards.default.nationality_btns import nationality_btns
from keyboards.default.city_btns import city_btns
from common.register_customer import register_customer
from common.constants import *


async def get_first_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['first_name'] = update.message.text
    except:
        context.user_data["first_name"] = update.callback_query
    await update.message.reply_text('Familyasini kiriting: ')
    return LAST_NAME

async def get_last_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['last_name'] = update.message.text
    
    await update.message.reply_text('Foydalanuvchi passport raqami kiriting: ')
    return PASSPORT_NUM

async def get_passport_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['passport_number'] = update.message.text
    
    await update.message.reply_text('Foydalanuvchi passport yaroqlilik sanasini kiriting: \n2032-02-23 shu formatda kiriting!!')
    return PASSPORT_VALID_DATE

async def get_passport_valid_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['passport_valid_date'] = update.message.text
    
    await update.message.reply_text('Foydalanuvchi millatini kiriting: ', reply_markup=nationality_btns)
    return NATIONALITY

async def get_nationality(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['nationality'] = update.message.text
    
    await update.message.reply_text('Foydalanuvchi Yashovchi viloyatni tanlang:', reply_markup=city_btns)
    return ADDRESS

async def get_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['address'] = update.message.text
    
    await update.message.reply_text('Foydalanuvchi tug\'ilgan sanani kiriting:\n2032-02-23 shu formatda kiriting!!',)
    return BIRTH_DATE

async def get_birth_date(update: Update, context):
    context.user_data['birth_date'] = update.message.text
    await update.message.reply_text('Foydalanuvchi emailini kiriting:')
    return EMAIL

async def get_email(update: Update, context):
    context.user_data['email'] = update.message.text
    await update.message.reply_text('Please enter your phone number:')
    return PHONE

async def get_phone(update: Update, context):
    context.user_data['phone_number'] = update.message.text

    if register_customer(**context.user_data):
        await update.message.reply_text('Thank you for registering! Your data has been saved.')
    else:
        await update.message.reply_text('Failed to save your data. Please try again later.')

    context.user_data.clear()
    return ConversationHandler.END

async def cancel(update, context):
    # Reset user data
    context.user_data.clear()

    update.message.reply_text('Registration cancelled. Please type /start to start again.')

    return ConversationHandler.END