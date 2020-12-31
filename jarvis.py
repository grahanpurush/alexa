import pyttsx3
import speech_recognition as sr
import datetime




engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Master")
        
    elif hour>=18 and hour<22:
        speak("Good evening Master")
        
    else:
        speak("Hello Master It is your sleeping time")
        
    speak("I am zira . Please tell me how may I help you ?")

def takeCommand():
    #It will takes microphone input from user and returns string output.

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Sorry Master ,Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()