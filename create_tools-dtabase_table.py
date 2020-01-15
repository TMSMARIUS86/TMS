import sqlite3
with sqlite3.connect("Shared_Power.db") as db:
     cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tools(
Tools_id INTEGER PRIMARY KEY,
Tools_name VARCHAR(40) NOT NULL,
Tools_description VARCHAR(250) NOT NULL,
Tools_price DECIMAL(20) NOT NULL)
""")
