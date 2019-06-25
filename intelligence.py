#code for youtube video on assistant


import pyttsx3
import speech_recognition as sr


#code for text to speech using microsoft inbuilt api sapi5

engine=pyttsx3.init('sapi5')
voices_in_our_pc=engine.getProperty('voices')
print(voices_in_our_pc)
#setting a voice for our use
engine.setProperty('voice',voices_in_our_pc[0].id)
#speak function
def speak(text):
    engine.say(text)
    print('Computer :'+text)
    engine.runAndWait()

speak('Hello everyone !!')


#code for speech to text convertion
def speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        speech=r.recognize_google(audio,language='en-in')
    except sr.UnknownValueError:
        speak('Sorry')
        speech='None'
    return speech

print('Speeck: '+speech())












