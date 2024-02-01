import os

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from State.register import Delete
from Utils.sp_database import Database

# Получаем текущую рабочую директорию
current_directory = os.getcwd()

# Формируем относительный путь к БД
relative_path = 'Utils/sp_database.db'
db_path = os.path.join(current_directory, relative_path)

# Инициализируем базу данных
db = Database(db_path)


async def process_delete_assisted(message: Message, state: FSMContext):
    await message.answer(
        text='Введите id для удаления ассистента'
    )
    await state.set_state(Delete.delete)


async def process_delete_good_id(message: Message):
    assisted_id = message.text
    if assisted_id.isdigit():
        db.delete_assistant(assisted_id)
        await message.answer(f'Ассистент с id {assisted_id} удален в БД')
    else:
        await message.answer('Для удаления ID указан не корректно!')
