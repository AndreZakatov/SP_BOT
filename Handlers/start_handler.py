import os

from aiogram.types import Message
from aiogram import Bot
from Keyboards.admin_start_kb import admin_start_kb
from Config.config import allowed_admin_ids
from Utils.sp_database import Database
from Keyboards.user_kb import user_kb, user_parsing_kb

# Получаем текущую рабочую директорию
current_directory = os.getcwd()

# Формируем относительный путь к БД
relative_path = 'Utils/sp_database.db'
db_path = os.path.join(current_directory, relative_path)

# Инициализируем базу данных
db = Database(db_path)


async def get_start(message: Message, bot: Bot):
    if message.from_user.id in allowed_admin_ids:
        await bot.send_message(message.from_user.id,
                               text='Вы начали работу с ботом в режиме администратора\n\n'
                                    'Выберете действие', reply_markup=admin_start_kb)
    if db.check_assisted_in_db(message.from_user.id):
        await bot.send_message(message.from_user.id,
                               text='Вы вошли в режиме ассистента\n\n'
                                    'Воспользуйся командой /parsing'
                               )

    else:
        if not db.check_subscribed(message.from_user.id):
            await bot.send_message(message.from_user.id,
                                   text=f'Hello {message.from_user.first_name}\n\n'
                                        f'У вас не оформлена подписка для выполнения парсинга\n\n'
                                        f'Давайте оформим подписку /to_pay_for')
        else:
            await bot.send_message(message.from_user.id,
                                   text=f'Hello {message.from_user.first_name}\n\n'
                                        f'Ваша подписка активна', reply_markup=user_parsing_kb())

