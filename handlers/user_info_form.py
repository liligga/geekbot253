from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from db.base import create_order


class Form(StatesGroup):
    product_id = State()
    name = State()
    # age = State()
    address = State()
    day = State()
    done = State()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply(
        'Отменено.',
        reply_markup=types.ReplyKeyboardRemove())


async def form_start(cb: types.CallbackQuery, state: FSMContext):
    """
    Стартуем наш FSM, задаем первый вопрос
    """

    await Form.product_id.set()
    async with state.proxy() as data:
        data['product_id'] = int(cb.data.replace('buy_item ', ''))

    await Form.next()
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Введите ваше имя"
    )



async def process_name(message: types.Message, state: FSMContext):
    """
    Обрабатываем имя, задаем второй вопрос
    """
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    await message.reply("Введите ваш адрес")


async def process_age(message: types.Message, state: FSMContext):
    """
    Обрабатывваем возраст, задаем следующий вопрос
    """
    if not message.text.isdigit():
        await message.reply("Введите ваш возраст(число)")
    else:
        async with state.proxy() as data:
            data['age']=int(message.text)

        week_days_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        week_days_kb.add(
            KeyboardButton("Понедельник"),
            KeyboardButton("Вторник"),
            KeyboardButton("Среда"),
            KeyboardButton("Четверг"),
            KeyboardButton("Пятница")
        )
        await Form.next()
        await message.reply(
            "Выберите день недели для получения посылки в ближайшую неделю",
            reply_markup=week_days_kb
        )


async def process_address(message: types.Message, state: FSMContext):
    """
    Обрабатывваем адрес, задаем следующий вопрос
    """
    async with state.proxy() as data:
        data['address']=message.text

    week_days_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    week_days_kb.add(
        KeyboardButton("Понедельник"),
        KeyboardButton("Вторник"),
        KeyboardButton("Среда"),
        KeyboardButton("Четверг"),
        KeyboardButton("Пятница")
    )
    await Form.next()
    await message.reply(
        "Выберите день недели для получения посылки в ближайшую неделю",
        reply_markup=week_days_kb
    )



async def process_day(message: types.Message, state: FSMContext):
    """
    Обрабатываем введенный день недели, задаем следующий вопрос
    """
    async with state.proxy() as data:
        data['day']=message.text

    yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no_kb.add(
        KeyboardButton("Да"),
        KeyboardButton("Нет")
    )

    await Form.next()
    await message.reply(f"""Подтвердите ваши данные:
    Имя: {data['name']}
    Адрес: {data['address']}
    День, когда вы можете получить посылку: {data['day']}
    Данные верны?
    """, reply_markup=yes_no_kb)

async def process_done(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        create_order(data)

    await state.finish()
    await message.reply(
        "Спасибо. Мы с вами свяжемся.",
        reply_markup=ReplyKeyboardRemove()
    )

