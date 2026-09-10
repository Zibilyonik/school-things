import sqlite3
# Connect to SQLite database
# The database file is test.db.
# If the file does not exist, it will automatically be created in the current directory.
#INSERT / DELETE / UPDATE / SELECT
#CRUD - create, read, update, delete
#CREATE DATABASE mydb;
# " TABLE mytable(sudentID int NOT NULL PRIMARY KEY)

conn = sqlite3.connect("test.db")
cursor = conn.cursor() 
cursor.execute()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
        """)

conn.commit()

conn.close()