import logging


def config_logging():
    # Конфигурация логирования в консоль
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',)

    # Работа с файлом логирования
    file_handler = logging.FileHandler('sp_log.txt')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)

    # Получение логгера в aiogram и добавление в файловый обработчик
    logger = logging.getLogger('aiogram')
    logger.addHandler(file_handler)

    # Обработка исключений
    logger.exception = lambda msg: logger.error(f'EXCEPTION: {msg}')


# Конфигурация логгировани
config_logging()

