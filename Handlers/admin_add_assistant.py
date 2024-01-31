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


@router.callback_query(StateFilter(default_state),F.data == 'add')
async def process_admin_actions(call: CallbackQuery, state: FSMContext):
    await state.set_state(AdminActions.actions)
    await call.answer(
        text='Выберите действие', reply_markup=admin_actions
    )

@router.callback_query(StateFilter(AdminActions.actions),
                       F.data.in_(['add_assisted', 'delete_assisted']))
async def process_actions(call: CallbackQuery, callback_data: dict, state: FSMContext):
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
    async def process_add_assistant_press(call, state: FSMContext):
        # Здесь вы можете получить id из состояния
        data = await state.get_data()
        user_id = data.get('user_id')

        # Ваш код для добавления ассистента в базу данных

        await call.answer(f'Ассистент с id {user_id} добавлен')
        await state.clear()
