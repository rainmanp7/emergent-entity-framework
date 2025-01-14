import os
import sqlite3

# Define the database names and their corresponding SQL table creation scripts
DATABASES = {
    "math.db": """
        CREATE TABLE IF NOT EXISTS math_concepts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concept_name TEXT NOT NULL,
            description TEXT,
            examples TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS math_problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem_type TEXT NOT NULL,
            problem_statement TEXT NOT NULL,
            solution TEXT,
            difficulty_level TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,
    "english.db": """
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            definition TEXT,
            synonyms TEXT,
            antonyms TEXT,
            usage_examples TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS grammar_rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_name TEXT NOT NULL,
            description TEXT,
            examples TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,
    "python.db": """
        CREATE TABLE IF NOT EXISTS python_concepts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concept_name TEXT NOT NULL,
            description TEXT,
            code_examples TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS python_problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem_type TEXT NOT NULL,
            problem_statement TEXT NOT NULL,
            solution_code TEXT,
            difficulty_level TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,
    "science.db": """
        CREATE TABLE IF NOT EXISTS science_concepts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concept_name TEXT NOT NULL,
            description TEXT,
            examples TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS science_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_type TEXT NOT NULL,
            question_text TEXT NOT NULL,
            answer TEXT,
            difficulty_level TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,
    "memory.db": """
        CREATE TABLE IF NOT EXISTS memory_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_id TEXT NOT NULL,
            memory_type TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS associations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_id TEXT NOT NULL,
            associated_entity_id TEXT NOT NULL,
            strength REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
}

# Define the data folder
DATA_FOLDER = "data"

# Create the data folder if it doesn't exist
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
    print(f"Created folder: {DATA_FOLDER}")

# Function to create a database and execute the SQL script
def create_database(db_name, sql_script):
    db_path = os.path.join(DATA_FOLDER, db_name)
    try:
        # Connect to the SQLite database (it will be created if it doesn't exist)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Execute the SQL script to create tables
        cursor.executescript(sql_script)
        print(f"Database '{db_name}' created successfully at '{db_path}'.")
    except sqlite3.Error as e:
        print(f"Error creating database '{db_name}': {e}")
    finally:
        if conn:
            conn.close()

# Create all databases
for db_name, sql_script in DATABASES.items():
    create_database(db_name, sql_script)

print("All databases have been created successfully.")