from telegram import ReplyKeyboardMarkup, KeyboardButton

def create_keyboard(buttons, row=False):
    """Create a reply keyboard markup object with the given buttons."""
    if row:
        keyboard = [[KeyboardButton(button) for button in buttons]]
    else:
        keyboard = [[KeyboardButton(button)] for button in buttons]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
