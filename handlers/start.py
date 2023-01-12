from aiogram import types
from handlers.constants import START_TEXT


# @dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
	"""
		Функция приветствия пользователя по имени
	"""
	await message.answer(text=START_TEXT.format(first_name=message.from_user.first_name))
	await message.delete()

