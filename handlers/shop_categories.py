from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.base import get_products


buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить', callback_data='buy_item')
)


async def show_books(message: types.Message):
	"""
		Показываем пользователю список книг
	"""

	await message.answer(text="Вот наши книги:")
	await message.answer_photo(
		open('./images/cat.webp', 'rb'),
		caption=f"Товар: Книга 1, Описание: Великолепная книга"
	)

