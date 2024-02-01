from aiogram.fsm.state import State, StatesGroup


class InputId(StatesGroup):
    id_assist = State()


class Delete(StatesGroup):
    delete = State()