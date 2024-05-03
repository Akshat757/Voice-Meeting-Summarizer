from flask import Flask, render_template, request, stream_with_context, Response
from listen import listen_updates, stop, new_listen_updates
from database import all_recording, search_recording_by_word, search_recording_by_date, last_n_recording
from mail_service import send_email
import re


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

from flask import Response, stream_with_context

@app.route('/start_recording', methods=['POST'])
def start_recording():
    
    def generate_updates():
        for update in new_listen_updates():
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



@app.route('/mail', methods=['GET', 'POST'])
def mail():
    last_recorded_id = last_n_recording(1)[0][0] # Implement this function to get the last recorded ID
    message = None
    if request.method == 'POST':
        receiver_mail = request.form.get('select_mail')
        id = request.form.get('select_id')
        
        # Check if both receiver email and ID are provided
        if receiver_mail and id:
            if validate_email(receiver_mail):  # Check if email is valid
                try:
                    send_email(id, receiver_mail)
                    message = "Email sent successfully! to " + receiver_mail
                except Exception as e:
                    message = "Failed to send email: " + str(e)
            else:
                message = "Please provide a valid email address!"
        else:
            message = "Please provide both receiver email and ID!"
    
    return render_template('mail.html', last_recorded_id=last_recorded_id, message=message)
 # Pass the last recorded ID to the template



def validate_email(email):
    # Basic email format validation using regular expression
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None



@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)