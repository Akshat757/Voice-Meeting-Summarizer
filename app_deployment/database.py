import sqlite3
from datetime import datetime, timedelta

DATABASE_FILE = 'A:/Learning/Meeting-Summarizer/app_deployment/recorded.db'

def connect_to_db():
    return sqlite3.connect(DATABASE_FILE)

# conn = connect_to_db()
# c = conn.cursor()

        
def setup_table():
    # Create a table to store recorded text
    conn = connect_to_db()
    c = conn.cursor()
    try:
        # Create a table to store recorded text
        c.execute('''CREATE TABLE IF NOT EXISTS recorded (
                     id INTEGER PRIMARY KEY,
                     text TEXT,
                     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                     duration TEXT
                     )''')
        conn.commit()
        print("Table is there")
    except Exception as e:
        print(f"Error setting up the table: {e}")
    

def setup_db():
    # conn = connect_to_db()
    # c = conn.cursor()
    setup_table()


def save_recording(text, start_time):
    print("adding this text to database: ", text)
    try:
        conn = connect_to_db()
        c = conn.cursor()

        duration = datetime.now() - start_time
        minutes = duration.total_seconds() // 60
        seconds = duration.total_seconds() % 60
        duration_str = f"{int(minutes)} min, {int(seconds)} s"
        
        setup_db()
        
        # Insert recorded text into the database along with a timestamp and duration
        c.execute("INSERT INTO recorded (text, timestamp, duration) VALUES (?, ?, ?)",
                  (text, datetime.now(), duration_str))
        conn.commit()  # Commit changes to the database
        print("Recorded text has been saved to the database.")
    except Exception as e:
        print(f"Error saving to the database: {e}")


def delete_recording(id):
    conn = connect_to_db()
    c = conn.cursor()
    dlt_sql = """DELETE FROM recorded WHERE id=?;"""
    c.execute(dlt_sql,(id,))
    conn.commit()
    
def read_recording():
    conn = connect_to_db()
    c = conn.cursor()
    read_sql = """SELECT * FROM recorded;"""
    c.execute(read_sql)
    print("all records in the table are: ",c.fetchall())

def last_n_recording(n):
    conn = connect_to_db()
    c = conn.cursor()
    list_sql = f"SELECT * FROM recorded ORDER BY id DESC LIMIT {n}"
    c.execute(list_sql)
    print(f"Last {n} recordings are: {c.fetchall()}")

def search_recording(search_word):
    conn = connect_to_db()
    c = conn.cursor()
    search_sql = f"SELECT * FROM recorded WHERE text LIKE '%{search_word}%';"
    c.execute(search_sql)
    print(f"all the recordings containing {search_word} are: {c.fetchall()}")

def search_recording_by_date(search_date):
    conn = connect_to_db()
    c = conn.cursor()
    # Assuming 'date_column' is the name of the column with datetime stamp
    search_sql = f"SELECT * FROM recorded WHERE timestamp >= ? AND timestamp < ?;"
    # Assuming search_date is a string in format 'YYYY-MM-DD'
    start_date = datetime.strptime(search_date, '%Y-%m-%d')
    end_date = start_date + timedelta(days=1)
    c.execute(search_sql, (start_date, end_date))
    print(f"All the recordings on {search_date} are: {c.fetchall()}")


# setup_db()
# read_recording()