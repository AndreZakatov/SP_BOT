import requests
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Bot

from Validsator_URL_telegram.validator import validate_url

from State.parsing_state import UrlInput


async def process_parsing(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Для выполнения парсинга вам необходимо ввести ссылку для проверки')
    await state.set_state(UrlInput.url)


async def process_good_url(message: Message, bot: Bot):
    try:
        url = message.text
        print(requests.get(url))
        if validate_url(url):
            await bot.send_message(message.from_user.id,
                                   text='Ваша ссылка корректна, начинаю сбор данных')
        else:
            await bot.send_message(message.from_user.id,
                                   text='Не корректная ссылка')
    except Exception as e:
        print(f'Ошибка при выполнении кода\n\n{e}')
        await bot.send_message(message.from_user.id,
                               text='Произошла ошибка\n\n'
                                    'Проверьте чтобы ссылка на ресурс начиналапсь c http:// или https://:\n\n'
                                    'Или можете обратиться в службу поддержки')
