from aiogram import types


async def shop_start(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки магазина
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Выберите категорию из меню ниже",
    )