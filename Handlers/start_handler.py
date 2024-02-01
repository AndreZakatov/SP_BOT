from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from Keyboards.admin_start_kb import admin_start_kb


async def get_start(message: Message):
    await message.answer(
        text='Вы начали работу с ботом', reply_markup=admin_start_kb)

