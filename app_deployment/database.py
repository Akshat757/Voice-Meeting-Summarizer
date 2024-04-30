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
                     sum_text TEXT,
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


def save_recording(text, sum_text, start_time):
    print("Adding this text to the database:", text)
    try:
        conn = connect_to_db()
        c = conn.cursor()
        end_time = datetime.now()  # Get the current time as the end time
        duration = end_time - start_time  # Calculate the duration
        duration_str = format_duration(duration)  # Format the duration as a string

        # print(f'the start time of the recording recieved by the save recording func. is: {start_time}\n')
        # print(f'the end time of the recording is: {end_time}\n')
        # print(f'the duration of the recording is: {duration}\n')
        # print(f'the duration after formatting is: {duration_str}\n')

        setup_db()

        # Insert recorded text into the database along with a timestamp and duration
        c.execute("INSERT INTO recorded (text, sum_text, timestamp, duration) VALUES (?, ?, ?, ?)",
                  (text, sum_text, datetime.now(), duration_str))
        conn.commit()  # Commit changes to the database
        print("Recorded text has been saved to the database.")
    except Exception as e:
        print(f"Error saving to the database: {e}")

        

def format_duration(duration):
    # Convert the duration to minutes and seconds
    minutes = duration.total_seconds() // 60
    seconds = duration.total_seconds() % 60
    return f"{int(minutes)} min, {int(seconds)} s"


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
    table = c.fetchall()
    conn.close()
    print("all records in the table are: ",table)
    return table

def all_recording():
    conn = connect_to_db()
    c = conn.cursor()
    list_sql = f"SELECT text, sum_text, timestamp, duration FROM recorded ORDER BY id DESC"
    c.execute(list_sql)
    table = c.fetchall()
    conn.close()
    print(f"All recordings are: {table}")
    return table

def last_n_recording(n):
    conn = connect_to_db()
    c = conn.cursor()
    list_sql = f"SELECT * FROM recorded ORDER BY id DESC LIMIT {n}"
    c.execute(list_sql)
    table = c.fetchall()
    conn.close()
    print(f"Last {n} recordings are: {table}")
    return table

def search_recording_by_word(search_word):
    conn = connect_to_db()
    c = conn.cursor()
    search_sql = f"SELECT text, sum_text, timestamp, duration FROM recorded WHERE text LIKE '%{search_word}%'ORDER BY id DESC"
    c.execute(search_sql)
    table = c.fetchall()
    conn.close()
    print(f"all the recordings containing {search_word} are: {table}")
    return table

from datetime import datetime, timedelta

def search_recording_by_date(search_date):
    conn = connect_to_db()
    c = conn.cursor()
    # Assuming 'timestamp' is the name of the column with datetime stamp
    search_sql = "SELECT text, sum_text, timestamp, duration FROM recorded WHERE timestamp >= ? AND timestamp < ? ORDER BY id DESC"
    try:
        # Assuming search_date is a string in format 'YYYY-MM-DD'
        start_date = datetime.strptime(search_date, '%Y-%m-%d')
    except ValueError:
        # Handle invalid date format
        print("Invalid date format. Please provide date in YYYY-MM-DD format.")
        return []
    end_date = start_date + timedelta(days=1)
    c.execute(search_sql, (start_date, end_date))
    table = c.fetchall()
    conn.close()
    if not table:
        print(f"No recordings found for {search_date}.")
    else:
        print(f"All the recordings on {search_date} are: {table}")
    return table



# setup_db()
# read_recording()