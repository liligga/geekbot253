from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.constants import HELP_TEXT, START_TEXT
from handlers.start import start_command
from handlers.help import help_command
from handlers.pictures import image_sender
from handlers.shop import shop_start
from handlers.all_messages import echo
from handlers.shop_categories import show_books
from handlers.admin import example
from handlers.admin import (
	example,
	check_curses,
	pin_messages,
	ban_user
)


# @dp.message_handler(commands=["start"])
# async def start_command(message: types.Message):
# 	"""
# 		Функция приветствия пользователя по имени
# 	"""
# 	await message.answer(text=START_TEXT.format(
# 		first_name=message.from_user.first_name)
# 	)
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
	storage = MemoryStorage()
	dp = Dispatcher(bot, storage=storage)

	# регистрируем обработчики
	dp.register_message_handler(start_command, commands=['start'])
	dp.register_message_handler(help_command, commands=['help'])
	dp.register_message_handler(image_sender, commands=['picture'])
	dp.register_callback_query_handler(shop_start, text='shop_start')
	dp.register_message_handler(show_books, Text(equals='Хочу книги'))
	dp.register_message_handler(pin_messages, commands=['pin'], commands_prefix='!/')
	dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
	dp.message_handler(cancel_handler, state='*', commands='cancel')
	dp.message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
	dp.message_handler(process_name, state=Form.name)
	dp.message_handler(process_age, state=Form.age)
	#всегда в конце
	dp.register_message_handler(check_curses)


	executor.start_polling(dp, skip_updates=True)
