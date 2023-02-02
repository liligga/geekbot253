from aiogram import types
from config import bot
import aioschedule
import asyncio


async def schedule_command(message: types.Message):
    global chat_id, notify_what
    chat_id = message.from_user.id
    notify_what = message.text.lower().split('напомни ')
    await message.answer("Отлично")


async def notification():
    await bot.send_message(
        chat_id=chat_id,
        text=notify_what
    )


async def schedule():
    aioschedule.every(10).seconds.do(notification)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)