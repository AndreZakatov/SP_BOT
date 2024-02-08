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


def user_pay_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Оплатить', callback_data='pay')
    kb.adjust(1)
    return kb.as_markup()


def user_choice_sum():
    kb = InlineKeyboardBuilder()
    kb.button(text='5000', callback_data='pay_5000')
    kb.button(text='10000', callback_data='pay_10000')
    kb.adjust(2)
    return kb.as_markup()