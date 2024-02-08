import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

from Config.config import Config, get_config
from Handlers.parsing import process_parsing, process_good_url
from Handlers.start_handler import get_start
from Handlers.admin_add_assistant import process_add_assisted, process_add_good_id
from Handlers.admin_delete_assisted import process_delete_assisted, process_delete_good_id
from Handlers.subscribe import process_payment, process_add_5000, process_add_10000

from State.register import Delete, InputId
from State.parsing_state import UrlInput


# Конфигурация логирования и запуск бота
async def main():
    logging.info('Бот запущен!')

    # Загрузка конфигурации в переменную
    config: Config = get_config()

    # Инициализация хранилища
    storage = MemoryStorage()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    # Старт
    dp.message.register(get_start, Command(commands='start'))
    # Добавление ассистента
    dp.message.register(process_add_assisted, F.text == 'Добавить ассистента')
    dp.message.register(process_add_good_id, InputId.id_assist)
    # Удаление ассистента
    dp.message.register(process_delete_assisted, F.text == 'Удалить ассистента')
    dp.message.register(process_delete_good_id, Delete.delete)
    # Выполнение парсинга
    dp.message.register(process_parsing, Command(commands='parsing'))
    dp.message.register(process_good_url, UrlInput.url)
    dp.callback_query.register(process_parsing, lambda c: c.data == 'pars')
    # Выполнение подписки и оплаты
    dp.message.register(process_payment, Command(commands='to_pay_for'))
    dp.callback_query.register(process_add_5000, lambda x: x.data == 'pay_5000')
    dp.callback_query.register(process_add_10000, lambda x: x.data == 'pay_10000')


    # Пропуск апдейтов и запуск пулинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f'An error occurred: {e}')
