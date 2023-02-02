from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv


load_dotenv()  # берем переменные окружения из .env
bot = Bot(getenv('BOT_TOKEN'))
# Диспетчер, получает сообщения, обрабатывает через обработчик
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
CHANNEL = '@pyton253'