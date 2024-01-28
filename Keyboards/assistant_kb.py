from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

parsing_button = InlineKeyboardButton(
    text = '💹 Парсинг',
        callback_data = 'parsing'
    )

assistant_kb: list[list[InlineKeyboardButton]] = [
    [parsing_button],
    ]

assistant_start_kb = InlineKeyboardMarkup(inline_keyboard=assistant_kb)