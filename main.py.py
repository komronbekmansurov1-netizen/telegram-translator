import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from deep_translator import GoogleTranslator

TOKEN = "8582036263:AAFrSLwNrNHXUgVJxJzhVHFwemqFNISXFWI"

bot = Bot(token=TOKEN)
dp = Dispatcher()


def language_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 UZ → EN 🇬🇧", callback_data="uz_en"),
                InlineKeyboardButton(text="🇬🇧 EN → UZ 🇺🇿", callback_data="en_uz"),
            ]
        ]
    )


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Tarjima yo'nalishini tanlang: ",
        reply_markup=language_menu()
    )


user_mode = {}


@dp.callback_query(F.data == "uz_en")
async def uzb_eng(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "uz_en"
    await callback.message.answer("🇺🇿 O'zbekchadan 🇬🇧 Inglizchaga tarjima rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()


@dp.callback_query(F.data == "en_uz")
async def eng_uzb(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "en_uz"
    await callback.message.answer("🇬🇧 Inglizchadan 🇺🇿 O'zbekchaga tarjima rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()


@dp.message(F.text)
async def tarjima(message: Message):
    user_id = message.from_user.id

    if user_id not in user_mode:
        await message.answer("Avval tarjima yo'nalishini tanlang:", reply_markup=language_menu())
        return

    mode = user_mode[user_id]
    text = message.text

    try:
        if mode == "uz_en":
            translated = GoogleTranslator(source="uz", target="en").translate(text)
        else:
            translated = GoogleTranslator(source="en", target="uz").translate(text)

        await message.answer(translated)

    except Exception as e:
        await message .answer(f"Xato: {e}")


async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
