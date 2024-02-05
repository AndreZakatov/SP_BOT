from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def user_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Подписаться', callback_data='sub')
    kb.adjust(1)
    return kb.as_markup()


def user_parsing_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Парсинг', callback_data='pars')
    kb.adjust(1)
    return kb.as_markup()