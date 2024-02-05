import os

from aiogram.types import Message
from Keyboards.admin_start_kb import admin_start_kb
from Config.config import allowed_admin_ids
from Utils.sp_database import Database

# Получаем текущую рабочую директорию
current_directory = os.getcwd()

# Формируем относительный путь к БД
relative_path = 'Utils/sp_database.db'
db_path = os.path.join(current_directory, relative_path)

# Инициализируем базу данных
db = Database(db_path)


async def get_start(message: Message):
    if message.from_user.id in allowed_admin_ids:
        await message.answer(
            text='Вы начали работу с ботом в режиме администратора\n\n'
                 'Выберете действие', reply_markup=admin_start_kb)
    if db.check_assisted_in_db(message.from_user.id):
        await message.answer(
            text='Вы вошли в режиме ассистента\n\n'
                 'Воспользуйся командой /parsing'
        )
