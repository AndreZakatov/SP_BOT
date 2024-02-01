from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_start_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Парсинг"
        ),
        KeyboardButton(
            text="Добавить ассистента"
        ),
        KeyboardButton(
            text='Удалить ассистента'
        ),
        KeyboardButton(
            text="Статистика"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True)