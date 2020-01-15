import sqlite3
with sqlite3.connect("Shared_Power.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
User_id INTEGER PRIMARY KEY,
User_name VARCHAR(20) NOT NULL,
First_name VARCHAR(20) NOT NULL,
Surname VARCHAR(20) NOT NULL,
Password VARCHAR(20) NOT NULL)
""")
