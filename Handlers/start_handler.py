from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from Keyboards.admin_start_kb import admin_start_kb
from Config.config import allowed_admin_ids


async def get_start(message: Message):
    if message.from_user.id in allowed_admin_ids:
        await message.answer(
            text='Вы начали работу с ботом в режиме администратора\n\n'
                 'Выберете действие', reply_markup=admin_start_kb)
