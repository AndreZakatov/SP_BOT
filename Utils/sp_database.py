import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_name):
        # Устанавливаем соединение с базой данных
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # Включение поддержки внешних ключей
        self.cursor.execute("PRAGMA foreigen_keys = ON;")

    # Таблица администраторов
    def create_table_admins(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins (
                admin_id INTEGER
            )   
        """)
        self.conn.commit()

    # Таблица администраторов
    def create_table_assistant(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS assistant (
                assistant_id INTEGER
            )   
        """)
        self.conn.commit()

    # Таблица администраторов
    def create_table_subscriptions(self):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                user_id INTEGER,
                status TEXT,
                data_start DATETIME,
                data_end DATETIME
            )   
        """)
        self.conn.commit()

    def update_subscription(self, user_id, status, data_start):
        end_date = datetime.strptime(data_start, "%Y-%m-%d %H:%M:%S") + timedelta(days=10)
        end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            UPDATE subscriptions SET status = ?, data_end = ? WHERE user_id = ?
        """, (status, end_date_str, user_id))
        self.conn.commit()
