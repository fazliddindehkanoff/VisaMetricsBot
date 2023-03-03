from telegram import InlineKeyboardButton, InlineKeyboardMarkup

back_button = InlineKeyboardButton(text="🔙 ortga", callback_data="back")
turn_on = InlineKeyboardButton(text="Yoqish", callback_data="turn_on_monthly_visa")
add_customer = InlineKeyboardButton(text="Odam Qo'shish", callback_data="add_customer")
clients = InlineKeyboardButton(text="Klientlar", callback_data="clients")

navigation_btns = InlineKeyboardMarkup(
    [
        [turn_on, add_customer],
        [clients]
    ]
)