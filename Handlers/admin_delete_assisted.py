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


async def process_delete_good_id(message: Message, state: FSMContext):
    if message.text.isdigit():
        if db.check_assisted_in_db(message.text):
            await state.update_data(id_add=message.text)
            data = await state.get_data()
            add_id = data.get('id_add')
            db.delete_assistant(add_id)
            await message.answer(
                text=f'Ассистент с ID: {add_id} удален'
            )
            await state.clear()
        else:
            await message.answer(
                text=f'ID: {message.text}\n\n'
                     f'В БД не найден'
            )
    else:
        await message.answer(
            text=f'<{message.text}> не является числом\n\n'
                 f'Введите id ассистента в правильном формате для удаления'
        )
