from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.filters.state import StatesGroup, State, StateFilter
from aiogram.types import CallbackQuery


router: Router = Router()

db = Database("Utils/sp_bot.bd")


class InputURL(StatesGroup):
    input_url = State() # Ожидание вставки ссылки