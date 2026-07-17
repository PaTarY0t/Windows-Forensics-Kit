import sqlite3

db = r"C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\Default\Network Action Predictor"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("SELECT url FROM network_action_predictor")

for row in cursor.fetchall():
    print(row[0])

    conn.close