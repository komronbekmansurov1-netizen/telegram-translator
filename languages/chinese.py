from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def chinese_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 UZ → NC 🇨🇳", callback_data="uz_cn"),
                InlineKeyboardButton(text="🇨🇳 NC → UZ 🇺🇿", callback_data="cn_uz"),
            ]
        ]
    )

