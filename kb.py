from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="Просмотр доступных изображений", callback_data="check_pictures")]
]

answer_block = [
    [InlineKeyboardButton(text="✅ ok", callback_data="check_ok")],
    [InlineKeyboardButton(text="❌ not ok", callback_data="check_nok")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])