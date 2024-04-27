import sqlite3
import time
from datetime import datetime

def connect_to_db():
    conn = sqlite3.connect('recorded.db')
    return conn

conn = connect_to_db()
c = conn.cursor()


def save_recording(text):
    print("adding this text to database: ", text)
    try:
        # Insert recorded text into the database along with a timestamp
        c.execute("INSERT INTO recorded (text, timestamp) VALUES (?, ?)", (text, datetime.now()))
        conn.commit()  # Commit changes to the database
        print("Recorded text has been saved to the database.")
    except Exception as e:
        print(f"Error saving to the database: {e}")

def setup_table():
    # Create a table to store recorded text
    # c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS recorded (
                 id INTEGER PRIMARY KEY,
                 text TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    print("table is created successfully")
    

def setup_db():
    # conn = connect_to_db()
    # c = conn.cursor()
    setup_table(conn)


def delete_recording(conn,id):
    dlt_sql = """DELETE FROM recorded WHERE id=?;"""
    c.execute(dlt_sql,(id,))
    conn.commit()
    
def read_recording():
    # c = conn.cursor()
    read_sql = """SELECT * FROM recorded;"""
    c.execute(read_sql)
    print("all records in the table are: ",c.fetchall())

def last_n_recording(n):
    list_sql = f"SELECT * FROM recorded ORDER BY id DESC LIMIT {n}"
    c.execute(list_sql)
    print(f"Last {n} recordings are: {c.fetchall()}")

def search_recording(search_word):
    search_sql = f"SELECT * FROM recorded WHERE text LIKE '%{search_word}%';"
    c.execute(search_sql)
    print(f"all the recordings containing {search_word} are: {c.fetchall()}")


