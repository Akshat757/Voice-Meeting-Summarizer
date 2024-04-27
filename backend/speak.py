import pyttsx3

def text_to_speech(text):
    text_speech = pyttsx3.init()

    #     """ RATE"""
    # rate = text_speech.getProperty('rate')   # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    text_speech.setProperty('rate', 125)     # setting up new voice rate
    voices = text_speech.getProperty('voices')       #getting details of current voice
    text_speech.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female

    text_speech.say(text)
    text_speech.runAndWait()

    # """VOLUME"""
    # volume = text_speech.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    # print (volume)                          #printing current volume level
    # text_speech.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    # """VOICE"""
    # #text_speech.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male

# text_to_speech("this is my program which records audio, converts it into text then saves it inta a database")