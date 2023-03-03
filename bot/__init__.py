from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters

from .customer_registration import *
from .start import start
from common.constants import *

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST_NAME: [MessageHandler(filters.TEXT, get_first_name)],
            LAST_NAME: [MessageHandler(filters.TEXT, get_last_name)],
            PASSPORT_NUM: [MessageHandler(filters.TEXT, get_passport_number)],
            PASSPORT_VALID_DATE: [MessageHandler(filters.TEXT, get_passport_valid_date)],
            NATIONALITY: [MessageHandler(filters.TEXT, get_nationality)],
            BIRTH_DATE: [MessageHandler(filters.TEXT, get_birth_date)],
            EMAIL: [MessageHandler(filters.TEXT, get_email)],
            PHONE: [MessageHandler(filters.TEXT, get_phone)],
            ADDRESS: [MessageHandler(filters.TEXT, get_address)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
)