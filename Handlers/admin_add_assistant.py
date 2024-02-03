import os
import html

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
    if message.text.isdigit():
        if not db.check_assisted_in_db(message.text):
            await state.update_data(id_add=message.text)
            data = await state.get_data()
            add_id = data.get('id_add')
            db.add_assistant(add_id)
            await message.answer(
                text=f'Ассистент с ID: {add_id} добавлен.'

            )
            await state.clear()
        else:
            await message.answer(
                text=f'Ассистент с ID: {html.unescape(message.text)} уже в базе данных.'
            )
    else:
        try:
            int(message.text)
        except ValueError:
            await message.answer(
                text=f'{message.text} не является числом\n\n'
                     f'Для добавления ассистента введите id в числовом формате'
            )
        except Exception as e:
            print(f'Error: {e}')
            await message.answer(
                text=f'При обработке запроса произошла ошибка\n\n'
                     f'Пожалуйста, повторите запрос еще раз или обратитесь в службу поддержки.'
            )



