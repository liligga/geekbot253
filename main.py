from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv
# from constants import HELP_TEXT, START_TEXT
import logging
from handlers.start import start_command
from handlers.help import help_command
from handlers.pictures import image_sender
from handlers.all_messages import echo
# # Наш бот
# load_dotenv()  # берем переменные окружения из .env
# bot = Bot(getenv('BOT_TOKEN'))
# # Диспетчер, получает сообщения, обрабатывает через обработчик
# dp = Dispatcher(bot)


# @dp.message_handler(commands=["start"])
# async def start_command(message: types.Message):
# 	"""
# 		Функция приветствия пользователя по имени
# 	"""
# 	await message.answer(text=START_TEXT.format(first_name=message.from_user.first_name))
# 	await message.delete()



# @dp.message_handler(commands=["help"])
# async def help_command(message: types.Message):
# 	"""
# 		Показываем все команды пользователю
# 	"""
# 	await message.answer(text=HELP_TEXT)
# 	await message.delete()


# @dp.message_handler(commands=["picture"])
# async def image_sender(message: types.Message):
# 	"""
# 		Функция ответа пользователю картинкой
# 	"""
# 	await message.answer_photo(
#         open('./images/cat.webp', 'rb'), 
#         caption="Умный кот"
#     )
# 	await message.delete()


# @dp.message_handler()
# async def echo(message: types.Message):
# 	"""
# 		Функция ответа пользователю заглавными буквами
# 	"""
# 	await message.reply(text=message.text.upper())


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	# Наш бот
	load_dotenv()  # берем переменные окружения из .env
	bot = Bot(getenv('BOT_TOKEN'))
	# Диспетчер, получает сообщения, обрабатывает через обработчик
	dp = Dispatcher(bot)
	# регистрируем обработчики
	dp.register_message_handler(start_command, commands=['start'])
	dp.register_message_handler(help_command, commands=['help'])
	dp.register_message_handler(image_sender, commands=['picture'])
	dp.register_message_handler(echo)

	executor.start_polling(dp, skip_updates=True)
