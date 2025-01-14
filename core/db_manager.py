import sqlite3
import os

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        
        # Navigate up to the main directory and then into the 'data' directory
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", db_name)
        
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
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

# Self-execute section for testing
if __name__ == "__main__":
    # Test the DBManager
    db_manager = DBManager("test.db")
    db_manager.insert_data("Test input", "Test output")