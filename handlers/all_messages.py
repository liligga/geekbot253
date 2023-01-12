from aiogram import types


# @dp.message_handler()
async def echo(message: types.Message):
	"""
		Функция ответа пользователю заглавными буквами
	"""
	await message.reply(text=message.text.upper())
