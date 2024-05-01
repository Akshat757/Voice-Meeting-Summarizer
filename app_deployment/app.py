from flask import Flask, render_template, request, stream_with_context, Response
from listen import listen_updates, stop
from database import all_recording, search_recording_by_word, search_recording_by_date


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

from flask import Response, stream_with_context

@app.route('/start_recording', methods=['POST'])
def start_recording():
    
    def generate_updates():
        for update in listen_updates():
            # Encode the update message as bytes before yielding
            yield update.encode('utf-8')

    return Response(stream_with_context(generate_updates()), content_type='text/plain')


# @app.route('/start_recording', methods=['POST'])  # Change to POST method
# def start_recording():
#     text = listen()
#     sum_text = generate_summary(text)
#     keywords = top_frequent_words(text)
#     text = "the recorded text is: " + text
#     sum_text = "the summarized text is: " + sum_text
#     keywords = "the keywords are: " + keywords
#     print(f"the sum text is: {sum_text}")
#     return [text, sum_text, keywords]


@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    stop()
    ############something to be added here#############
    return "recording stopped"


@app.route('/records', methods=['GET', 'POST'])
def records():

    per_page = 10  # Number of records per page
    page = request.args.get('page', 1, type=int)

    if request.method == 'POST':
        search_type = request.form.get('search_type')
        search_query = request.form.get('search_query')
        if search_query:
            # If search query is present, filter records
            if search_type == "word":
                table_data = search_recording_by_word(search_query)
            else:
                table_data = search_recording_by_date(search_query)
        else:
            # If no search query, display all records
            table_data = all_recording()
    else:
        # For GET requests, display all records
        table_data = all_recording()

    total_records = len(table_data)
    total_pages = (total_records + per_page - 1) // per_page
    start_index = (page - 1) * per_page
    end_index = min(start_index + per_page, total_records)
    current_records = table_data[start_index:end_index]

    return render_template('records.html', data=current_records, page=page, total_pages=total_pages)


if __name__ == '__main__':
    app.run(debug=True)