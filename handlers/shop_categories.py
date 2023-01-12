from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить', callback_data='buy_item')
)



# @dp.message_handler()
async def show_books(message: types.Message):
	"""
		Функция ответа пользователю заглавными буквами
	"""
	await message.answer(text="Вот наши книги:")
	await message.answer(text="Книга 1", reply_markup=buy_item_kb)
	await message.answer(text="Книга 2", reply_markup=buy_item_kb)
	await message.answer(text="Книга 3", reply_markup=buy_item_kb)
