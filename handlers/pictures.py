from aiogram import types


# @dp.message_handler(commands=["picture"])
async def image_sender(message: types.Message):
	"""
		Функция ответа пользователю картинкой
	"""
	await message.answer_photo(
        open('./images/cat.webp', 'rb'), 
        caption="Умный кот"
    )
	await message.delete()