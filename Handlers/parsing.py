import asyncio

from telethon.tl.types import Chat
from telethon.sync import TelegramClient

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Bot

from Utils.parser.data.config import api_id, api_hash
from Utils.parser.data.main import collect_chat_information

from Utils.parser.data.my_functions import check_link, inv_chat, check_chat, session

from State.parsing_state import UrlInput

client = TelegramClient(api_id, api_hash, session)
client.start()


async def is_invitation_accepted(client, chat_link):
    try:
        hash = chat_link.rsplit('/', 1)[1]
        chat = await client.get_entity(hash)

        if isinstance(chat, Chat):
            return True
        else:
            return False

    except Exception as e:
        print(f"Ошибка при проверке принятия заявки: {e}")
        return False


async def process_parsing(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Для выполнения парсинга вам необходимо ввести ссылку для проверки')
    await state.set_state(UrlInput.url)


async def process_good_url(message: Message, bot: Bot, state: FSMContext):
    try:
        url = message.text
        await bot.send_message(message.from_user.id, text='Выполняю проверку ссылки!')

        link_type = check_link(url)

        if link_type == 'close':
            await bot.send_message(message.from_user.id,
                                   text='Для сбора информации из закрытого сообщества я подам заявку и дождусь принятия.')
            await inv_chat(url)

            # Ожидание принятия заявки
            for _ in range(20):
                await asyncio.sleep(1)
                if await is_invitation_accepted(client, url):  # используем url вместо chat_link
                    print("Заявка принята!")
                    break

            await bot.send_message(message.from_user.id, text='Заявка принята. Начинаю сбор информации.')

            # Здесь вызывайте вашу функцию для сбора информации
            await collect_chat_information(api_id, api_hash, session, url)

        elif link_type == 'url':
            await bot.send_message(message.from_user.id, text='Обработка открытой ссылки')
        else:
            await bot.send_message(message.from_user.id, text='Неверная ссылка. Попробуйте другую.')

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        await bot.send_message(message.from_user.id, text='Произошла ошибка при обработке ссылки. Попробуйте еще раз.')

