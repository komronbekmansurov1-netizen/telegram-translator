from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def russian_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇷🇺 RU → UZ 🇺🇿", callback_data="ru_uz"),
                InlineKeyboardButton(text="🇺🇿 UZ → RU 🇷🇺", callback_data="uz_ru"),
            ]
        ]
    )

