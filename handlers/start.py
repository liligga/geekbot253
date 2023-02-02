from aiogram import types
from handlers.constants import START_TEXT
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, CHANNEL


start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(
	InlineKeyboardButton('Магазин', callback_data='shop_start'),
	InlineKeyboardButton('Наш Адрес', callback_data='address')
)




async def start_command(message: types.Message):
	"""
		Функция приветствия пользователя по имени
	"""
	await message.answer(
		text=START_TEXT.format(\
			first_name=message.from_user.first_name),
		reply_markup=start_kb
		)
	await message.delete()
