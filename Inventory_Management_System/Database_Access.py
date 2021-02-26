import sqlite3
# This will be where the database is managed and accessed.
# inventory(item, qty, description)


def insert_inventory(item,  qty, description):
    # Establish a connection to the database.
    con = sqlite3.connect('Inventory.db')
    # Create a cursor.
    c = con.cursor()
    # User values
    data = (item, qty, str(description))
    # Insert data on a new row.
    c.execute("INSERT INTO Inventory VALUES(?,?,?)",data)
    # Commit changes
    con.commit()
    # Close connection.
    con.close()

def edit_inventory(item, qty):
    # User data.
    data = (qty, item)
    # Connect to database.
    con = sqlite3.connect('Inventory.db')
    # Create a cursor.
    c = con.cursor()
    # Update qty.
    c.execute("""UPDATE Inventory SET Qty = (?)
                WHERE Item = (?)""", data)
    con.commit()
    # close connection.
    con.close()

def print_all_inventory():
    con = sqlite3.connect('Inventory.db')
    # Create a cursor.
    c = con.cursor()
    for row in c.execute("SELECT * FROM Inventory"):
        print(row)
    # Close connection.
    con.close()
