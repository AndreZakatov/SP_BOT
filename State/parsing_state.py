from aiogram.fsm.state import State, StatesGroup


class UrlInput(StatesGroup):
    url = State()