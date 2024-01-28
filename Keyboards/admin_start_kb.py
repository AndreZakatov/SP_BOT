from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

stat_info_button = InlineKeyboardButton(
    text = '🧮 Статистика',
        callback_data='stat'
    )

add_assistant_button = InlineKeyboardButton(
    text = '🤓 Добавление ассистентов',
        callback_data = 'add'
    )

parsing_button = InlineKeyboardButton(
    text = '💹 Парсинг',
        callback_data = 'parsing'
    )

admin_kb: list[list[InlineKeyboardButton]] = [
    [stat_info_button, add_assistant_button, parsing_button],
    ]

admin_start_kb = InlineKeyboardMarkup(inline_keyboard=admin_kb)