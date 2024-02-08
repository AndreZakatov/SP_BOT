import sqlite3
from datetime import datetime, timedelta


class Database:
    def __init__(self, db_name):
        # Устанавливаем соединение с базой данных
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # Включение поддержки внешних ключей
        self.cursor.execute("PRAGMA foreign_keys = ON;")

    # Таблица администраторов
    def create_table_admins(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins (
                admin_id INTEGER
            )   
        """)
        self.conn.commit()

    # Таблица асистентов
    def create_table_assistant(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS assistant (
                assistant_id INTEGER
            )   
        """)
        self.conn.commit()

    # Таблица подписчиков с подписками
    def create_table_subscriptions(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                user_id INTEGER,
                status TEXT,
                date_start DATETIME,
                date_end DATETIME
            )   
        """)
        self.conn.commit()

    # Функция добавления даты в заданном формате
    def update_subscription(self, user_id, status, data_start):
        end_date = datetime.strptime(data_start, "%Y-%m-%d %H:%M:%S") + timedelta(days=10)
        end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            UPDATE subscriptions SET status = ?, data_end = ? WHERE user_id = ?
        """, (status, end_date_str, user_id))
        self.conn.commit()

    # Таблица выполненных запросов на парсинг
    def create_table_parsing(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS parsing (
        id_parsing INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        date DATETIME,
        result TEXT,
        FOREIGN KEY (telegram_id) REFERENCES users (telegram_id)
        )
        """)

    # Таблица со статистикой
    def create_table_statistics(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS statistics (
        id_statistics INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATETIME,
        total_users INTEGER,
        active_users INTEGER,
        new_users INTEGER,
        requests_per_day INTEGER
        )
        """)

    def create_all_table(self):
        self.create_table_admins()
        self.create_table_assistant()
        self.create_table_subscriptions()
        self.create_table_parsing()
        self.create_table_statistics()

    def add_admins(self, telegram_id):
        self.cursor.execute("""
            INSERT INTO  admins (admin_id) 
            VALUES (?)
            """, (telegram_id,))
        self.conn.commit()

    def add_assistant(self, telegram_id):
        self.cursor.execute("""
            INSERT INTO assistant (assistant_id) 
            VALUES (?)
            """, (telegram_id,))
        self.conn.commit()

    def add_user_in_subscriptions(self, user_id, status, date_start, date_end, balance):
        self.cursor.execute("""
            INSERT INTO subscriptions (user_id, status, date_start, date_end, balance)
            VALUES (?,?,?,?,?)
            """, (user_id, status, date_start, date_end, balance))
        self.conn.commit()

    def check_balance(self, user_id):
        self.cursor.execute("""
        SELECT balance FROM subscriptions WHERE user_id = ? 
        """, (user_id,))
        result = self.cursor.fetchone()
        return result

    def delete_assistant(self, telegram_id):
        self.cursor.execute("""
        DELETE FROM assistant WHERE assistant_id = ?
        """, (telegram_id,))
        self.conn.commit()

    def check_assisted_in_db(self, telegram_id):
        self.cursor.execute("""
        SELECT * FROM assistant WHERE assistant_id = ?
        """, (telegram_id,))
        result = self.cursor.fetchone()
        return result is not None

    def check_all_assisted(self):
        self.cursor.execute("""
        SELECT * FROM assistant
        """)
        result = self.cursor.fetchall()
        return result

    def check_subscribed(self, telegram_id):
        self.cursor.execute("""
        SELECT * FROM subscriptions WHERE user_id = ?
        """, (telegram_id,))
        result = self.cursor.fetchone()
        return result is not None

    def update_balance_subscriptions(self, user_id, balance):
        self.cursor.execute("""
        SELECT balance FROM subscriptions
        WHERE user_id = ?
        """, (user_id,))
        current_balance = self.cursor.fetchone()[0]
        new_balance = current_balance + balance

        self.cursor.execute("""
        UPDATE subscriptions
        SET balance = ?
        WHERE user_id = ?
        """, (new_balance, user_id,))
        self.conn.commit()


if __name__ == "__main__":
    db = Database('sp_database.db')
