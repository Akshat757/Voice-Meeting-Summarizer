import sqlite3
from datetime import datetime, timedelta

DATABASE_FILE = './db/recorded.db'

def connect_to_db():
    return sqlite3.connect(DATABASE_FILE)

# conn = connect_to_db()
# c = conn.cursor()


def setup_table():
    # Create a table to store recorded text
    conn = connect_to_db()
    c = conn.cursor()
    try:
        # Create a table to store recorded text with the modified schema
        c.execute('''CREATE TABLE IF NOT EXISTS recorded (
                     id INTEGER PRIMARY KEY,
                     text TEXT,
                     sum_text TEXT,
                     timestamp TEXT,
                     duration TEXT
                     )''')
        conn.commit()
        print("Table is there")
    except Exception as e:
        print(f"Error setting up the table: {e}")



def save_recording(text, sum_text, start_time):
    print("Adding this text to the database:", text)
    try:
        conn = connect_to_db()
        c = conn.cursor()
        end_time = datetime.now()  # Get the current time as the end time
        duration = end_time - start_time  # Calculate the duration
        duration_str = format_duration(duration)  # Format the duration as a string
        formatted_timestamp = datetime.strftime(end_time, "%b %d, %Y · %I:%M %p")  # Format the timestamp
        setup_table()

        # Insert recorded text into the database along with the formatted timestamp and duration
        c.execute("INSERT INTO recorded (text, sum_text, timestamp, duration) VALUES (?, ?, ?, ?)",
                  (text, sum_text, formatted_timestamp, duration_str))
        conn.commit()  # Commit changes to the database
        print("Recorded text has been saved to the database.")
    except Exception as e:
        print(f"Error saving to the database: {e}")

        
# def setup_table():
#     # Create a table to store recorded text
#     conn = connect_to_db()
#     c = conn.cursor()
#     try:
#         # Create a table to store recorded text
#         c.execute('''CREATE TABLE IF NOT EXISTS recorded (
#                      id INTEGER PRIMARY KEY,
#                      text TEXT,
#                      sum_text TEXT,
#                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
#                      duration TEXT
#                      )''')
#         conn.commit()
#         print("Table is there")
#     except Exception as e:
#         print(f"Error setting up the table: {e}")
    



# def save_recording(text, sum_text, start_time):
#     print("Adding this text to the database:", text)
#     try:
#         conn = connect_to_db()
#         c = conn.cursor()
#         end_time = datetime.now()  # Get the current time as the end time
#         duration = end_time - start_time  # Calculate the duration
#         duration_str = format_duration(duration)  # Format the duration as a string

#         setup_db()

#         # Insert recorded text into the database along with a timestamp and duration
#         c.execute("INSERT INTO recorded (text, sum_text, timestamp, duration) VALUES (?, ?, ?, ?)",
#                   (text, sum_text, datetime.now(), duration_str))
#         conn.commit()  # Commit changes to the database
#         print("Recorded text has been saved to the database.")
#     except Exception as e:
#         print(f"Error saving to the database: {e}")

        
def setup_db():
    # conn = connect_to_db()
    # c = conn.cursor()
    setup_table()


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
    # list_sql = f"SELECT text, sum_text, timestamp, duration FROM recorded ORDER BY id DESC"
    list_sql = f"SELECT * FROM recorded ORDER BY id DESC"
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
    # search_sql = f"SELECT text, sum_text, timestamp, duration FROM recorded WHERE text LIKE '%{search_word}%'ORDER BY id DESC"
    search_sql = f"SELECT * FROM recorded WHERE text LIKE '%{search_word}%'ORDER BY id DESC"
    c.execute(search_sql)
    table = c.fetchall()
    conn.close()
    print(f"all the recordings containing {search_word} are: {table}")
    return table


# def search_recording_by_date(search_date):
#     conn = connect_to_db()
#     c = conn.cursor()
#     # Assuming 'timestamp' is the name of the column with datetime stamp
#     # search_sql = "SELECT text, sum_text, timestamp, duration FROM recorded WHERE timestamp >= ? AND timestamp < ? ORDER BY id DESC"
#     search_sql = "SELECT * FROM recorded WHERE timestamp >= ? AND timestamp < ? ORDER BY id DESC"
#     try:
#         # Assuming search_date is a string in format 'YYYY-MM-DD'
#         start_date = datetime.strptime(search_date, '%Y-%m-%d')
#     except ValueError:
#         # Handle invalid date format
#         print("Invalid date format. Please provide date in YYYY-MM-DD format.")
#         return []
#     end_date = start_date + timedelta(days=1)
#     c.execute(search_sql, (start_date, end_date))
#     table = c.fetchall()
#     conn.close()
#     if not table:
#         print(f"No recordings found for {search_date}.")
#     else:
#         print(f"All the recordings on {search_date} are: {table}")
#     return table


def search_recording_by_date(search_date):
    conn = connect_to_db()
    c = conn.cursor()
    # Adjusted SQL query to use LIKE operator for searching by date
    search_sql = "SELECT * FROM recorded WHERE timestamp LIKE ? ORDER BY id DESC"
    try:
        # Parse the input date string into a datetime object
        formatted_search_date = f"{search_date}%"
    except ValueError:
        print("Invalid date format. Please provide date in 'Mon DD, YYYY' format.")
        return []

    c.execute(search_sql, (formatted_search_date,))
    table = c.fetchall()
    conn.close()
    if not table:
        print(f"No recordings found for {search_date}.")
    else:
        print(f"All the recordings on {search_date} are: {table}")
    return table


def get_number_of_recordings():
    conn = connect_to_db()
    c = conn.cursor()
    # Execute a SQL query to count the number of rows in the recorded table
    c.execute("SELECT COUNT(*) FROM recorded")
    count = c.fetchone()[0]  # Fetch the count value
    return count



def fetch_texts_by_id(id):
    # Connect to your database
    conn = connect_to_db()
    cursor = conn.cursor()
    
    try:
        # Execute a SELECT query to fetch recorded text and summarized text based on the provided ID
        cursor.execute("SELECT text, sum_text FROM recorded WHERE id=?", (id,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # If result is not None, extract recorded text and summarized text
        if result:
            recorded_text, summarized_text = result
            return recorded_text, summarized_text
        else:
            # Handle case when no record is found for the provided ID
            print("No record found for the provided ID")
            return None, None
    except sqlite3.Error as e:
        print("Error fetching data:", e)
        return None, None
    finally:
        # Close the database connection
        conn.close()




# setup_db()
# read_recording()
# all_recording()