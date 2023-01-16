from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


class Form(StatesGroup):
    name = State()
    age = State()
    address = State()
    day = State()
    done = State()



async def form_start(message: types.Message):
    await Form.name.set()
    await message.reply("")


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Отменено.', reply_markup=types.ReplyKeyboardRemove())



async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    await message.reply("")


async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        data['age']=int(message.text)
    await Form.next()
    await message.reply("")


async def process_address(mesage: types.Message, state: FSMContext):
    pass

