import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



print("Initializing Jarvis")
MASTER = "munazza"


engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[0].id)

# speak function will pronouce the string which is pass to it
def speak(text):
   
    engine.runAndWait()
    engine.say(text)
   
# this function wish u as per the given time
def wishMe():     
    
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour <12:
          speak("Good Morning" + MASTER)
    
    elif hour>=12 and hour<18:
        speak("Good Aftenoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)    
 
   # speak("I am Jarvis. How may I help you?")

#this function will take command from the microphone
def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

     try :
         print("Recognizing...")          
         query = r.recognize_google(audio, language = 'en-pk')
         print(f"user said: {query}\n")

     except sr.RequestError as e:
         print("Could not request results; {0}".format(e))
         query = None
     return query 





# Main program start her
speak("Initiallizing jarvis")
wishMe()
query = takecommand()


# Logic for excecuting basic task as per the query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
     #webbrowser.open("youtube.com")
     url = "youtube.com"
     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
     webbrowser.get(chrome_path).open(url)        
elif 'open reddit' in query.lower():
     #webbrowser.open("youtube.com")
     url = "reddit.com"
     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
     webbrowser.get(chrome_path).open(url)    
elif 'open facebook' in query.lower():
     #webbrowser.open("youtube.com")
     url = "facebook.com"
     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
     webbrowser.get(chrome_path).open(url)     
elif 'open code'  in query.lower():
    codePath = "C:\\Users\\munaz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
elif  'play music'  in query.lower():
    songs_dir = "C:\\Users\\munaz\\Downloads"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))


     
       