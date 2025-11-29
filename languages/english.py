from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def english_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 UZ → EN 🇬🇧", callback_data="uz_en"),
                InlineKeyboardButton(text="🇬🇧 EN → UZ 🇺🇿", callback_data="en_uz"),
            ]
        ]
    )

