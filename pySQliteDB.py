import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

# Insert records into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Jane Smith', 'jane@example.com'))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Bob Johnson', 'bob@example.com'))

# Save (commit) the changes
conn.commit()

# Retrieve records from the table
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
for user in users:
    print(user)

# Update a record in the table
cursor.execute("UPDATE users SET email = ? WHERE name = ?", ('john.doe@example.com', 'John Doe'))
conn.commit()

# Retrieve the updated record
cursor.execute("SELECT * FROM users WHERE name = ?", ('John Doe',))
user = cursor.fetchone()
print(user)

# Close the cursor and connection
cursor.close()
conn.close()
