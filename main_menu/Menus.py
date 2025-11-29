from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def main_menu():
    kb = InlineKeyboardBuilder()

    kb.row(
        InlineKeyboardButton(text="🇬🇧 EN <-> UZ 🇺🇿", callback_data="english"),
        InlineKeyboardButton(text="🇨🇳 CN <-> UZ 🇺🇿", callback_data="chinese"),
        InlineKeyboardButton(text="🇪🇸 ES <-> UZ 🇺🇿", callback_data="spainish"),
        InlineKeyboardButton(text="🇰🇷 KR <-> UZ 🇺🇿", callback_data="korean"),
        InlineKeyboardButton(text="🇷🇺 RU <-> UZ 🇺🇿", callback_data="russian"),
    )

    kb.adjust(2)
    return kb.as_markup()
