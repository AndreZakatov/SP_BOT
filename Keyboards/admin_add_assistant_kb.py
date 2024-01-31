from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

add_button = InlineKeyboardButton(
    text='Добавить ассистента',
        callback_data='add_assisted'
)

delete_button = InlineKeyboardButton(
    text='Удалить ассистента',
        callback_data='delete_assisted'
)


add_delete_assisted: list[list[InlineKeyboardButton]] = [
    [add_button, delete_button],
]

admin_actions = InlineKeyboardMarkup(inline_keyboard=add_delete_assisted)
