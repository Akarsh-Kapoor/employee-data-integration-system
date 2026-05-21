import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    city TEXT
)
""")

conn.commit()

print("Database Created")

conn.close()