import os
from dataclasses import dataclass
from environs import Env
from dotenv import load_dotenv

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм боту


@dataclass
class Config:
    tg_bot: TgBot  # Телеграм бот


# Функция загрузки конфигурации
def load_env(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))

# загрузка переменных окружение из .env
load_dotenv()

# Получение значений переменной ADMIN_IDS
admin_ids_str = os.getenv('ADMIN_IDS').replace('[', '').replace(']', '').replace(',', '')
allowed_admin_ids = [int(admin_id) for admin_id in admin_ids_str.split()]


assistant_ids_str = os.getenv('ASSISTENT_IDS').replace('[', '').replace(']', '').replace(',', '')
allowed_assistant_ids = [int(assistant_id) for assistant_id in assistant_ids_str.split()]
