import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, Message

from Logging.logging import config_logging
from Config.config import allowed_admin_ids, allowed_assistant_ids, Config


# Конфигурация логирования и запуск бота
async def main():
    logging.info('Бот запущен!')

    # Загрузка конфигурации в переменную
    config: Config = config_logging()

    # Инициализация хранилища
    storage = MemoryStorage()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    @dp.message(CommandStart(), StateFilter(default_state))
    async def process_start_command(message: Message):
        admin_id = message.from_user.id
        assistant = message.from_user.id
        if admin_id in allowed_admin_ids:
            await message.answer()



    # Пропуск апдейтов и запуск пулинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f'An error occurred: {e}')
