import wikipedia
import speech_recognition as sr
import datetime

r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print (text)
        if str(text).lower() == 'what time is':
            print(datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'))
            break
