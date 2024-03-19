from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "check_pictures")
async def menu(msg: Message):
    picture = FSInputFile('1.jpg')
    await msg.answer_photo(photo=picture, reply_markup=kb.menu)  # ошибка
