import speech_recognition as sr
from database import save_recording, search_recording_by_date ,search_recording_by_word, connect_to_db, setup_db, read_recording, last_n_recording, delete_recording 
from mail_service import send_email
from speak import text_to_speech
from datetime import datetime, timedelta
from summary_sumy import generate_summary
from keywords import top_frequent_words
import config
import time

flag = 1
sum_text = ""

def stop():
    config.recording_state=0
    return


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
        # send_email(text)
        return "stop"
    elif command4 in command_text.lower():
        search_query = command_text.split("search database for", 1)[1].strip()
        search_recording_by_word(search_query)
        print("recording stopped")
        text_to_speech("recording stopped")
        return "stop"


def new_listen_updates():
    r = sr.Recognizer()
    text = ""
    with sr.Microphone() as source:
        print("Recordign started...")
        text_to_speech("Recording started...")
        yield("Recording started...")
        #text_to_speech("Listening for command...")
        start_time = datetime.now()
        print(f'the start time for the listening is: {start_time}\n')
        time_limit = timedelta(seconds=200)

        config.recording_state=1
        
        while True:
            if config.recording_state == 0: break
            print(f"the duration of rec is: {datetime.now() - start_time} and limit: {time_limit}")
            if datetime.now() - start_time >= time_limit:
                yield f"Recording stopped because, the Time limit of {time_limit} seconds has been passed.\n"
                break
                
            audio = r.listen(source, phrase_time_limit=20)
            try:
                recorded_text = r.recognize_google(audio)
                print("the recorded text is: ", recorded_text)
                text += " " + recorded_text
                yield recorded_text
            except sr.UnknownValueError:
                yield "Could not understand audio"
            except sr.RequestError as e:
                yield f"Error: {e}"

            if config.recording_state == 0: break
        x = 0
        yield "recording stopped!!!"
        text_to_speech("Recording stopped")
        final_text = "the recorded text is: " + text
        yield final_text
        time.sleep(2)
        text_to_speech("Working on the summary...")
        yield "Working on the summary..."
        sum_text = generate_summary(text)
        yield "the summarized text is: " + sum_text 
        keywords = "key points: " + top_frequent_words(text)
        yield keywords        
        save_recording(text, sum_text, start_time)

        #yield "Raw recorded text:"+recorded_text + ",working on converting raw text to readable text"




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
        while flag:
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
                # return text
                
            audio = r.listen(source, phrase_time_limit=20)
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
                    final_text = "the recorded text is: " + text
                    yield final_text
                    sum_text = "the summarized text is: " + generate_summary(text) 
                    yield sum_text 
                    keywords = top_frequent_words(text)
                    yield keywords 
                    # return text
                elif start_mode:
                    text += " " + command_text
                    print("the recorded text is: ", text)
                    yield command_text
            except sr.UnknownValueError:
                yield "Could not understand audio"
            except sr.RequestError as e:
                yield f"Error: {e}"
                



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
  



# conn = connect_to_db()
# setup_t
# setup_db()
# listen_updates()
# read_recording()
# search_recording_by_date("2024-04-27")
# delete_recording(1)
# read_recording()
# last_n_recording(2)
# new_listen_updates()