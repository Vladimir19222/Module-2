from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *  # get_all_products, is_included

users = get_all_products()

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text='Регистрация'))
kb.row(KeyboardButton(text='Рассчитать'), KeyboardButton(text='Инфомация'))
kb.add(KeyboardButton(text='Купить'))


kb_in = InlineKeyboardMarkup(resize_keyboard=True)
button_in = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_in2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.add(button_in, button_in2)


kb_inl = InlineKeyboardMarkup(resize_keyboard=True)
button_inl = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button_inl2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button_inl3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button_inl4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb_inl.row(button_inl, button_inl2, button_inl3, button_inl4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    balance = 1000
    age = State()
    username = State()
    email = State()


@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    data = await state.get_data()
    if is_included(data['username']) is False:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    await RegistrationState.age.set()
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await state.finish()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i, user in enumerate(users, start=1):
        with open(f'files/{i}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {user[1]} | Описание: {user[2]} | Цена: {user[3]}')
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_inl)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb_in)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 * вес (кг) + 6,25 * рост (см) – 5 * возраст (г) + 5")
    await call.answer()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        res = 10.0 * float(data['weight']) + 6.25 * float(data['growth']) - 5.0 * float(data['age']) + 5.0
        await message.answer(f"Ваша норма калорий: {res}")
    except:
        await message.answer(f'Ошибка при введении чисел.')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)