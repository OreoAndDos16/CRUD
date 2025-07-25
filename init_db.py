import sqlite3

def initialize_database():
    conn = sqlite3.connect("employeedb.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employeefile (
            recid INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            address TEXT NOT NULL,
            birthdate TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            civilstat TEXT NOT NULL,
            contactnum TEXT NOT NULL,
            salary REAL NOT NULL,
            isactive INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized.")

if __name__ == "__main__":
    initialize_database()