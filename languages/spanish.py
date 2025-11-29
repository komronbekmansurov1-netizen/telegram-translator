from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def spanish_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 UZ → ES 🇪🇸", callback_data="uz_es"),
                InlineKeyboardButton(text="🇪🇸 ES → UZ 🇺🇿", callback_data="es_uz"),
            ]
        ]
    )

