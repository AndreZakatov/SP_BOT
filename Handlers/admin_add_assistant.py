from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import Message, CallbackQuery

from Keyboards.admin_add_assistant_kb import admin_actions
from Utils.sp_database import Database

router: Router = Router()

db = Database("Utils/sp_database.db")


class AdminActions(StatesGroup):
    actions = State()  # Ожидание выбора действия


@router.message(Command(commands='admin_actions'), StateFilter(default_state))
async def process_admin_actions(message: Message):
    await message.answer(
        text='Выберите действие', reply_markup=admin_actions
    )

@router.callback_query(StateFilter(AdminActions.actions),
                       F.data.in_(['add_assisted', 'delete_assisted']))
async def process_actions(message: Message, call: CallbackQuery, callback_data: dict, state: FSMContext):
    if callback_data['add_assisted']:
        await call.answer(
            text='Введите id для добавления в базу данных'
        )
        await state.set_state(AdminActions.actions)
    else:
        await call.answer(
            text='Введите id ассистента для удаления из БД!'
        )
        await state.set_state(AdminActions.actions)


@router.callback_query(F.data == 'add_assisted', StateFilter(AdminActions.actions))
async def process_add_assistant_press(call: CallbackQuery, message: Message):
    await db.add_assistant(int(message.text))
    await message.answer(
        text=f'Ассистент с id {message.text} добавлен'
    )