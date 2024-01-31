from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import Message

from Keyboards.admin_add_assistant_kb import admin_actions
from Utils.sp_database import Database

router: Router = Router()

db = Database("Utils/sp_database.db")


class AdminActions(StatesGroup):
    actions = State()  # Ожидание выбора действия


@router.message(Command(commands='admin_actions'), StateFilter(default_state))
async def process_admin_actions(message: Message, state: FSMContext):
    await message.answer(
        text='Выберите действие', reply_markup=admin_actions
    )
    await state.set_state(AdminActions.actions)

@router.callback_query(StateFilter(AdminActions.actions),
                       F.data.in_(['add_assisted', 'delete_assisted']))
async def process_actions