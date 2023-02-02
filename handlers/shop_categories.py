from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.base import get_products


def buy_kb(product_id):
	buy_item_kb = InlineKeyboardMarkup()
	buy_item_kb.add(
		InlineKeyboardButton('Купить', callback_data=f'buy_item {product_id}')
	)
	return buy_item_kb


async def show_books(message: types.Message):
	"""
		Показываем пользователю список книг
	"""
	product = get_products()[0]
	print(product)
	await message.answer(text="Вот наши книги:")
	await message.answer_photo(
		open(product[4], 'rb'),
		caption=f"Товар: {product[1]}, Описание: {product[2]}",
		reply_markup=buy_kb(product[0])
	)

