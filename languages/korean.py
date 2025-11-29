from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def korean_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 UZ → KR 🇰🇷", callback_data="uz_kr"),
                InlineKeyboardButton(text="🇰🇷 KR → UZ 🇺🇿", callback_data="kr_uz"),
            ]
        ]
    )

