import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from deep_translator import GoogleTranslator

from languages.chinese import chinese_inline
from languages.korean import korean_inline
from languages.spanish import spanish_inline
from main_menu.Menus import main_menu
from languages.english import english_inline
from languages.russian import russian_inline

TOKEN = "8582036263:AAFrSLwNrNHXUgVJxJzhVHFwemqFNISXFWI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Foydalanuvchi rejimlari
user_mode = {}


# START
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Tarjima yo'nalishini tanlang:",
        reply_markup=main_menu()
    )


# MAIN MENU CALLBACKS

# English menu
@dp.callback_query(F.data == "english")
async def english_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "English ↔ Uzbek tarjima yo'nalishini tanlang:",
        reply_markup=english_inline()
    )


# Chinese menu
@dp.callback_query(F.data == "chinese")
async def chinese_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "Chinese ↔ Uzbek tarjima yo'nalishini tanlang:",
        reply_markup=chinese_inline()
    )

# Korean menu
@dp.callback_query(F.data == "korean")
async def chinese_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "Korean ↔ Uzbek tarjima yo'nalishini tanlang:",
        reply_markup=korean_inline()
    )

# Spain menu
@dp.callback_query(F.data == "spainish")
async def spanish_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "Spanish ↔ Uzbek tarjima yo'nalishini tanlang:",
        reply_markup=spanish_inline()
    )

# Russian menu
@dp.callback_query(F.data == "russian")
async def russian_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "Russian ↔ Uzbek tarjima yo'nalishini tanlang:",
        reply_markup=russian_inline()
    )



# RUSSIAN <-> UZBEK
@dp.callback_query(F.data == "ru_uz")
async def ru_to_uz(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "ru_uz"
    await callback.message.edit_text("🇷🇺 Rus → 🇺🇿 O‘zbek rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

@dp.callback_query(F.data == "uz_ru")
async def uz_to_ru(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "uz_ru"
    await callback.message.edit_text("🇺🇿 O‘zbek → 🇷🇺 Rus rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

# CHINESE <-> UZBEK
@dp.callback_query(F.data == "cn_uz")
async def cn_to_uz(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "cn_uz"
    await callback.message.edit_text("🇨🇳 Xitoy -> 🇺🇿 O'zbek rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

@dp.callback_query(F.data == "uz_cn")
async def uz_to_cn(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "uz_cn"
    await callback.message.edit_text("🇺🇿 O'zbek -> 🇨🇳 Xitoy rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

# ENGLISH <-> UZBEK
@dp.callback_query(F.data == "uz_en")
async def uz_to_en(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "uz_en"
    await callback.message.edit_text("🇺🇿 O‘zbek → 🇬🇧 Ingliz rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

@dp.callback_query(F.data == "en_uz")
async def en_to_uz(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "en_uz"
    await callback.message.edit_text("🇬🇧 Ingliz → 🇺🇿 O‘zbek rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

# SPAIN <-> UZBEK
@dp.callback_query(F.data == "uz_es")
async def uz_to_es(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "uz_es"
    await callback.message.edit_text("🇺🇿 O‘zbek → 🇪🇸 Ispan rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

@dp.callback_query(F.data == "es_uz")
async def uz_to_es(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "es_uz"
    await callback.message.edit_text("🇪🇸 Ispan → 🇺🇿 O‘zbek rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

# KOREAN <-> UZBEK
@dp.callback_query(F.data == "uz_kr")
async def uz_to_es(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "uz_kr"
    await callback.message.edit_text("🇺🇿 O‘zbek → 🇰🇷 Koreys rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()

@dp.callback_query(F.data == "kr_uz")
async def uz_to_es(callback: CallbackQuery):
    user_mode[callback.from_user.id] = "kr_uz"
    await callback.message.edit_text("🇰🇷 Koreys → 🇺🇿 O‘zbek rejimi yoqildi.\nMatn yuboring.")
    await callback.answer()


#       UNIVERSAL TRANSLATOR


@dp.message(F.text)
async def translate(message: Message):
    user_id = message.from_user.id

    if user_id not in user_mode:
        await message.answer(
            "Avval tarjima yo'nalishini tanlang:",
            reply_markup=main_menu()
        )
        return

    mode = user_mode[user_id]
    text = message.text

    try:
        # Russian
        if mode == "ru_uz":
            tr = GoogleTranslator(source="ru", target="uz").translate(text)

        elif mode == "uz_ru":
            tr = GoogleTranslator(source="uz", target="ru").translate(text)

        # English
        elif mode == "uz_en":
            tr = GoogleTranslator(source="uz", target="en").translate(text)

        elif mode == "en_uz":
            tr = GoogleTranslator(source="en", target="uz").translate(text)

        # Chinese
        elif mode == "cn_uz":
            tr = GoogleTranslator(source="zh-CN", target="uz").translate(text)

        elif mode == "uz_cn":
            tr = GoogleTranslator(source="uz", target="zh-CN").translate(text)

        # Spain
        elif mode == "es_uz":
            tr = GoogleTranslator(source="es", target="uz").translate(text)

        elif mode == "uz_es":
            tr = GoogleTranslator(source="uz", target="es").translate(text)

        # Korea
        elif mode == "kr_uz":
            tr = GoogleTranslator(source="ko", target="uz").translate(text)

        elif mode == "uz_kr":
            tr = GoogleTranslator(source="uz", target="ko").translate(text)

        else:
            tr = "Xatolik: tarjima rejimi topilmadi."

        await message.answer(tr)

    except Exception as e:
        await message.answer(f"Xato: {e}")


# ===============================
#       RUN BOT
# ===============================
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
