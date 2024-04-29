from flask import Flask, render_template, request, jsonify
import sqlite3
from listen import listen
import database as db
from database import read_recording, search_recording_by_word, search_recording_by_date
from summary_sumy import generate_summary
from keywords import top_frequent_words

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_recording', methods=['POST'])  # Change to POST method
def start_recording():
    text = listen()
    sum_text = generate_summary(text)
    keywords = top_frequent_words(text)
    text = "the recorded text is: " + text
    sum_text = "the summarized text is: " + sum_text
    keywords = "the keywords are: " + keywords
    print(f"the sum text is: {sum_text}")
    return [text, sum_text, keywords]



@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    ############something to be added here#############
    return "recording stopped"


@app.route('/records')
def records():
    table_data = read_recording()
    return render_template('records.html', data=table_data)


@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('searchQuery')
    selected_value = request.args.get('selectedValue')

    table_data = search_recording_by_word(search_query)
    return render_template('search_records.html', data=table_data)


if __name__ == '__main__':
    app.run(debug=True)