import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT,
    role TEXT,
    capability_code TEXT
)
""")
conn.commit()

def insert_user(username, email, password, role, code):
    cursor.execute("INSERT INTO users (username, email, password, role, capability_code) VALUES (?, ?, ?, ?, ?)",
                   (username, email, password, role, code))
    conn.commit()

def get_user(username):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

def run_secure_query(query):
    cursor.execute(query)
    return cursor.fetchall()
