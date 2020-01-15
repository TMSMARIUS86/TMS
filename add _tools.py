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

cursor.execute("""
INSERT INTO tools(Tools_name,Tools_description,Tools_price)
VALUES("Drill","DeWalt DCD778D1T-SFGB 18V 2.0Ah Li-Ion XR Brushless Cordless Combi Drill (621HP)New","10")
""")
db.commit()

cursor.execute("SELECT * FROM tools")
print(cursor.fetchall())

