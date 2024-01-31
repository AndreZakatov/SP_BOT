import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, Message

from Logging.logging import config_logging
from Config.config import allowed_admin_ids, Config, get_config, allowed_assistant_ids
from Keyboards.admin_start_kb import admin_start_kb
from Keyboards.assistant_kb import assistant_start_kb
from Handlers.admin_add_assistant import router as admin_actions_router


# Конфигурация логирования и запуск бота
async def main():
    logging.info('Бот запущен!')

    # Загрузка конфигурации в переменную
    config: Config = get_config()

    # Инициализация хранилища
    storage = MemoryStorage()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)


    # Регистрация роутеров в диспатчере
    dp.include_router(admin_actions_router)

    @dp.message(CommandStart(), StateFilter(default_state))
    async def process_start_command(message: Message):
        admin_id = message.from_user.id
        assistant = message.from_user.id
        if admin_id in allowed_admin_ids:
            await bot.send_message(message.from_user.id,
                                   text=f'Вы в режиме администратора\n\n'
                                        f'Выберите действие', reply_markup=admin_start_kb
            )
        elif assistant in allowed_assistant_ids:
            await bot.send_message(message.from_user.id,
                                   text=f'Режим ассистента', reply_markup=assistant_start_kb)
        else:
            await bot.send_message(message.from_user.id,
                                   text=f'Вы вошли в режиме пользователя')

    @dp.message(Command(commands='cancel'), StateFilter(default_state))
    async def process_cancel_command(message: Message):
        await message.answer(
            text='В данный момент отменять и прерывать нечего\n\n'
                 'Воспользуйтесь командой /start для выбора действия.'
        )

    @dp.message(Command(commands='cancel'), ~StateFilter(default_state))
    async def process_cancel_command_state(message: Message, state: FSMContext):
        await message.answer(
            text='Вы вышли из заполнения данных\n\n'
                 'Воспользуйтесь командой /start для выбора действия.')
        await state.clear()


    # Пропуск апдейтов и запуск пулинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f'An error occurred: {e}')
