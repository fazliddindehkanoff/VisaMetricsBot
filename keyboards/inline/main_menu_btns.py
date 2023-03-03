from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from common.constants import *

keyboards = [
        [
            InlineKeyboardButton(MONTHLY_VISA, callback_data=MONTHLY_VISA_CALLBACK),
            InlineKeyboardButton(EXPRESS_VISA, callback_data=EXPRESS_VISA_CALLBACK),
        ],
    ]

menu_keyboards = InlineKeyboardMarkup(keyboards)