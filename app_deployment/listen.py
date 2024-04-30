import speech_recognition as sr
from database import save_recording, search_recording_by_date ,search_recording_by_word, connect_to_db, setup_db, read_recording, last_n_recording, delete_recording 
from mail_service import send_email
from speak import text_to_speech
from datetime import datetime, timedelta
from summary_sumy import generate_summary
from keywords import top_frequent_words


sum_text = ""

def command_process(command_text, text, start_time):
    command1 = "start recording"
    command2 = "stop recording"
    command3 = "send text to mail"
    command4 = "search database for"

    # Check for any command
    if command1 in command_text.lower():
        print("Recording started...")
        text_to_speech("Recording started...")
        return "start"
    elif command2 in command_text.lower():
        print("recording stopped")
        text_to_speech("recording stopped")
        sum_text = generate_summary(text)
        save_recording(text, sum_text, start_time)
        return "stop"
    elif command3 in command_text.lower():
        print("recording stopped")
        text_to_speech("recording stopped")
        sum_text = generate_summary(text)
        save_recording(text, sum_text, start_time)
        send_email(text)
        return "stop"
    elif command4 in command_text.lower():
        search_query = command_text.split("search database for", 1)[1].strip()
        search_recording_by_word(search_query)
        print("recording stopped")
        text_to_speech("recording stopped")
        return "stop"


# def listen():
#     r = sr.Recognizer()
#     text = ""
#     with sr.Microphone() as source:
#         print("Listening for command...")
#         text_to_speech("Listening for command...")
#         start_time = datetime.now()
#         print(f'the start time for the listening is: {start_time}\n')
#         time_limit = timedelta(seconds = 180)
    
#         start_mode = None
#         while True:
            
#             if datetime.now() - start_time >= time_limit:
#                 print(f"time limit of {time_limit} seconds has been passed. ")
#                 text_to_speech(f"time limit of {time_limit} seconds has been passed. ")
#                 command_text = "Stop recording"
#                 command_process(command_text,text,start_time)
#                 return text

#             audio = r.listen(source)  
            
#             try:
#                 command_text = r.recognize_google(audio)
#                 command = command_process(command_text,text,start_time)
#                 if command == "start":
#                     start_time = datetime.now()
#                     print(f'the start time of the recording is: {start_time}\n')
#                     start_mode = 1

#                 elif command == "stop":
#                     print("the recorded text is: ", text)
#                     return text
                
#                 elif start_mode:
#                     text +=" "+ command_text
#                     print("the recorded text is: ", text)

#             except sr.UnknownValueError:
#                 print("Could not understand audio")
#             except sr.RequestError as e:
#                 print("Error: {0}".format(e))
  
def listen_updates():
    r = sr.Recognizer()
    text = ""
    with sr.Microphone() as source:
        print("Listening for command...")
        yield("Listening for command...")
        text_to_speech("Listening for command...")
        start_time = datetime.now()
        print(f'the start time for the listening is: {start_time}\n')
        time_limit = timedelta(seconds=120)
    
        start_mode = None
        while True:
            if datetime.now() - start_time >= time_limit:
                yield f"Time limit of {time_limit} seconds has been passed.\n"
                command_text = "Stop recording"
                command_process(command_text,text,start_time)
                final_text = "the recorded text is: " + text
                yield final_text
                sum_text = "the summarized text is: " + generate_summary(text)
                yield sum_text 
                keywords = top_frequent_words(text)
                yield keywords 
                return text
                
            
            audio = r.listen(source)
            try:
                command_text = r.recognize_google(audio)
                command = command_process(command_text, text, start_time)
                if command == "start":
                    start_time = datetime.now()
                    yield 'Recording started.'
                    print(f'the start time of the recording is: {start_time}\n')
                    start_mode = 1
                elif command == "stop":
                    yield 'Recording stopped.'
                    print("the recorded text is: ", text)
                    final_text = "\nthe recorded text is: " + text
                    yield final_text
                    sum_text = "\nthe summarized text is: " + generate_summary(text) +'\n'
                    yield sum_text 
                    keywords = top_frequent_words(text)
                    yield keywords 
                    return text
                elif start_mode:
                    text += " " + command_text
                    print("the recorded text is: ", text)
                    yield command_text
            except sr.UnknownValueError:
                yield "Could not understand audio"
            except sr.RequestError as e:
                yield f"Error: {e}"



# conn = connect_to_db()
# setup_t
# setup_db()
# listen_updates()
# read_recording()
# search_recording_by_date("2024-04-27")
# delete_recording(1)
# read_recording()
# last_n_recording(2)