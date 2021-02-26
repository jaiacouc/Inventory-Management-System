import sqlite3

conn = sqlite3.connect('cus.db')

# Create a cursor.
c = conn.cursor()


# Create a table
c.execute("Select * FROM customers WHERE last_name LIKE 'b%'")
items = c.fetchall()

for item in items:
    print(item)
# Commit command
conn.commit()

conn.close()

# NULL
# INTEGER
# REAL
# TEXT
# BLOB
