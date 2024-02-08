import os
import datetime
import time

from aiogram import Router, F, Bot
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.types import Message, CallbackQuery

from Utils.sp_database import Database
from Keyboards.user_kb import user_choice_sum

# Получаем текущую рабочую директорию
current_directory = os.getcwd()

# Формируем относительный путь к БД
relative_path = 'Utils/sp_database.db'
db_path = os.path.join(current_directory, relative_path)

# Инициализируем базу данных
db = Database(db_path)


# Получаем текущую дату и время
now = datetime.datetime.now()

# Создаем объекты datetime.date для даты начала и даты окончания
date_start = now.date()
date_end = now.date() + datetime.timedelta(days=1)

class Pay_cnt(StatesGroup):
    cnt = State()


async def process_payment(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Выберете сумму пополнения', reply_markup=user_choice_sum())


async def process_add_5000(message: Message, bot: Bot):
    try:
        if not db.check_subscribed(telegram_id=message.from_user.id):
            await bot.send_message(message.from_user.id,
                                   text='Пополнение на 5000 рублей\n\n'
                                        'Вношу данные 🕑')
            db.add_user_in_subscriptions(user_id=message.from_user.id,
                                         status='True',
                                         date_start=date_start,
                                         date_end=date_end,
                                         balance=5000)
            time.sleep(3)
            await bot.send_message(message.from_user.id,
                                   text='Данные внесены\n\n'
                                        'Вам доступна команда /parsing')
    except Exception as e:
        print(f'{e}')
        await bot.send_message(message.from_user.id,
                               text='Произошла ошибка, попробуйте еще раз')


async def process_add_10000(message: Message, bot: Bot):
    try:
        if not db.check_subscribed(telegram_id=message.from_user.id):
            await bot.send_message(message.from_user.id,
                                   text='Пополнение на 10000 рублей\n\n'
                                        'Вношу данные 🕑')
            db.add_user_in_subscriptions(user_id=message.from_user.id,
                                         status='True',
                                         date_start=date_start,
                                         date_end=date_end,
                                         balance=10000)
            time.sleep(3)
            await bot.send_message(message.from_user.id,
                                   text='Данные внесены\n\n'
                                        'Вам доступна команда /parsing')
    except Exception as e:
        print(f'{e}')
        await bot.send_message(message.from_user.id,
                               text='Произошла ошибка, попробуйте еще раз')