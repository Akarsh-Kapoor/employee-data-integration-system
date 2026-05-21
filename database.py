import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name TEXT,
    email TEXT,
    city TEXT
)
""")

conn.commit()

print("Database Created")

conn.close()