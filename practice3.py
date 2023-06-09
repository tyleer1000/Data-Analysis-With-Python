import sqlite3 as sql

conn = sql.connect('hw3.db')

# Create a cursor object
c = conn.cursor()

# Execute a SQL statement to get all tables
c.execute("SELECT * From games;")

rows = c.fetchall()

for row in rows:
    print(row)
