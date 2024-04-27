from flask import Flask, render_template
import sqlite3
import listen as l
from listen import listen
import database as db
from database import read_recording

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_recording', methods=['POST'])  # Change to POST method
def start_recording():
    # Call the listen function when the Start Recording button is clicked
    listen()
    # read_recording()
    # You can return any response to the client if needed
    return "Recording started"

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    l.flag = False
    return "recording stopped"

def get_table_data():
    conn = sqlite3.connect(db.DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recorded')
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/records')
def records():
    table_data = get_table_data()
    return render_template('records.html', data=table_data)


if __name__ == '__main__':
    app.run(debug=True)