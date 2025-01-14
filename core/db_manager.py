import sqlite3
import os

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_path = os.path.join("data", db_name)
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_data TEXT,
            output_data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
        conn.close()

    def insert_data(self, input_data, output_data):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO knowledge (input_data, output_data) VALUES (?, ?)", (input_data, output_data))
        conn.commit()
        conn.close()
        print(f"Data inserted into {self.db_name}: Input={input_data}, Output={output_data}")