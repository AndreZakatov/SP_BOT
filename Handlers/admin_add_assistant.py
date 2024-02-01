import os

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from State.register import InputId
from Utils.sp_database import Database

# Получаем текущую рабочую директорию
current_directory = os.getcwd()

# Формируем относительный путь к БД
relative_path = 'Utils/sp_database.db'
db_path = os.path.join(current_directory, relative_path)

# Инициализируем базу данных
db = Database(db_path)


async def process_add_assisted(message: Message, state: FSMContext):
    await message.answer(
        text='Введите id для добавления ассистента'
    )
    await state.set_state(InputId.id_assist)


async def process_add_good_id(message: Message, state: FSMContext):
    assisted_id = message.text
    if assisted_id.isdigit():
        db.add_assistant(assisted_id)
        await message.answer(f'Ассистент с id {assisted_id} добавлен в БД')
    else:
        await message.answer('Для добавления ID указан не корректно')
    await state.clear()
