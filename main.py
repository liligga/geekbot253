from aiogram import executor
from aiogram.dispatcher.filters import Text
from os import getenv
import logging
from config import dp
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

from handlers.user_info_form import (
	Form,
	cancel_handler,
	form_start,
	process_name,
	process_address,
	process_day,
	process_done
)
from db.base import (
	init_db,
	create_tables,
	populate_products
)
from handlers.scheduler import schedule_command, schedule
import asyncio


async def startup(_):
	init_db()
	create_tables()
	asyncio.create_task(schedule())



if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)


	# регистрируем обработчики
	dp.register_message_handler(start_command, commands=['start'])
	dp.register_message_handler(help_command, commands=['help'])
	dp.register_message_handler(image_sender, commands=['picture'])
	# dp.register_message_handler(form_start, commands=['form'])
	dp.register_message_handler(form_start, Text(equals='Нет'), state=Form.done)
	dp.register_callback_query_handler(shop_start, text='shop_start')
	dp.register_message_handler(show_books, Text(equals='Хочу книги'))
	dp.register_callback_query_handler(form_start, Text(startswith='buy_item '))
	dp.register_message_handler(pin_messages, commands=['pin'], commands_prefix='!/')
	dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
	dp.register_message_handler(cancel_handler, state='*', commands='cancel')
	dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
	dp.register_message_handler(process_name, state=Form.name)
	dp.register_message_handler(process_address, state=Form.address)
	dp.register_message_handler(process_day, state=Form.day)
	dp.register_message_handler(process_done,  Text(equals='Да'),state=Form.done)
	dp.register_message_handler(schedule_command, Text(startswith='напомни'))
	#всегда в конце
	dp.register_message_handler(check_curses)


	executor.start_polling(
		dp,
		skip_updates=True,
		on_startup=startup
	)
