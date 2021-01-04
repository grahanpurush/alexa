import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


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
        speak("Master It's your sleeping time. please Sleep")



def tellDay():
    day = datetime.datetime.today().weekday()+1
    Day_dict = {
        1: 'Monday',2: 'Tuesday', 3: 'Wednesday',
        4: 'Thursday',5: 'Friday', 6: 'Saturday',
        7: 'Sunday'
    }
    if day in Day_dict.keys():
        day_of_the_week =Day_dict[day]
        speak(" Today is " + day_of_the_week)
    speak("I am at your service . Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    tellDay()
    # while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\important\\favourite song'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Master, the time is {strTime}")

        elif 'lady master' in query:
            speak("Yes Master I know lady master name is rubia.You are lucky enough")

            if 'her home' in query:
                speak("She lives in my master's heart")
            else:
                speak("Get intouch her master.")
        elif 'magician' in query:
            speak("Yes master I know him very well.")


            if 'his name' in query:
                speak("His name is Shubho deep")
            else:
                speak("Sorry Master...Give me some time to familiar with")

        elif 'best friend' in query:
            speak("yes master I know him very well ,his name is porimol")

        elif 'brother' in query:
            speak("Hello Brother Debasish, how are you ?")






        elif 'open code' in query:
            codePath = "C:\\Users\\NISHITH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'sunday suspence' in query:
            f_dir = 'D:\\sunday suspence'
            suspense = os.listdir(f_dir)
            os.startfile(os.path.join(f_dir, suspense[0]))

        elif 'email to nisith' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "grahanpurusha@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak("Sorry master. I am not able to send this email")


else:

    speak("Master Take some rest. I am always there for you.")