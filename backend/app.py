import speech_recognition as sr
from database import save_recording, search_recording, connect_to_db, setup_db, read_recording, last_n_recording, delete_recording 
from mail_service import send_email
from speak import text_to_speech
from datetime import datetime, timedelta


def time_duration(start_time1):
    return datetime.now - start_time1


def command_process(command_text,text):
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
        save_recording(text)
        # send_email(text)
        return "stop"
    elif command3 in command_text.lower():
        print("recording stopped")
        text_to_speech("recording stopped")
        save_recording(text)
        send_email(text)
        return "stop"
    elif command4 in command_text.lower():
        search_query = command_text.split("search database for", 1)[1].strip()
        search_recording(search_query)
        print("recording stopped")
        text_to_speech("recording stopped")
        return "stop"
        

    
def listen():
    r = sr.Recognizer()
    text = ""
    with sr.Microphone() as source:
        print("Listening for command...")
        text_to_speech("Listening for command...")
        start_time = datetime.now()
        time_limit = timedelta(seconds = 60)
    
        
        start_mode = None
        while True:
            if datetime.now() - start_time > time_limit:
                print(f"time limit of {time_limit} seconds has been passed. ")
                text_to_speech(f"time limit of {time_limit} seconds has been passed. ")
                command_text = "Stop recording"
                command_process(command_text,text)
                return

            audio = r.listen(source)  
            
            try:
                command_text = r.recognize_google(audio)
                command = command_process(command_text,text)
                if command == "start":
                    start_mode = 1

                elif command == "stop":
                    print("the recorded text is: ", text)
                    return
                
                elif start_mode:
                    text +=" "+ command_text
                    print("the recorded text is: ", text)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error: {0}".format(e))

# conn = connect_to_db()
# setup_db()
listen()
# read_recording()
# delete_recording(conn, 1)
# read_recording()
# last_n_recording(2)