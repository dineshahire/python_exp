import sqlite3
conn =sqlite3.connect('example.db') conn.execute ('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
def create_user (name, age):
conn.execute ('INSERT INTO users (name, age) VALUES (?, ?)', (name, age)) conn.commit () print ('User created successfully')
def read_users (): cursor = conn.execute ('SELECT id, name, age FROM users') for row in cursor:
print (f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}')
def update_user (id, name, age): conn.execute ('UPDATE users SET name=?, age=?
WHERE id=?', (name, age, id)) conn.commit () print ('User updated successfully') def delete_user (id): conn.execute ('DELETE FROM users
WHERE id=?', (id,)) conn.commit () print ('User deleted
successfully') create_user ('Alice', 25)
create_user ('Bob', 30)
read_users ()
update_user(1, 'Alice Smith', 26) # delete a user
delete_user(2)
# read all users again read_users () conn.close()
