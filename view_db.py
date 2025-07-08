import sqlite3

conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print('id | username | created_at')
print('-' * 40)
for row in rows:
    print(f'{row[0]} | {row[1]} | {row[2]}')

conn.close() 