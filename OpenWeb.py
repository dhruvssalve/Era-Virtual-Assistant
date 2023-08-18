# from EraGui.py import updatechat
# import EraGui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from threading import *
from tkinter import *

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
def speak(self):
        # Function output the audio
        engine.say(self)
        engine.runAndWait()

    # Function simply greet the user
def wishme():
    # This determine the current time and typecaste it into integer of the computer and greet the user
        time = int(datetime.datetime.now().hour)
        if time >= 0 and time < 12:
            speak("Good Morning")
        elif time >= 12 and time < 10:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        speak("I am  how can I help you?")
        # GUI.updateChat("I am  how can I help you?")

    # listner function which take commands from microphone

def takeCommand():
    #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.
            # GUI.updateChat(f"User said: {query}\n")
        except Exception as e:
        # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            speak("Say that again please...")   #Say that again will be printed in case of improper voice
            return "None" #None string will be returned
        return query
def driver():
    # # if __name__ == '__main__':
    # voices = engine.getProperty("voices")
    # engine.setProperty('voice', voices[1].id)
    # .wishme()
    # t1.start()
    # t1.join()
    # while Tr
    query=takeCommand().lower()
    #search wikipedia
    if "wikipedia" in query:
        speak("Searching wikipedia")
        query=query.replace("wikipedia", " ")
        print(query) #debug
        results=wikipedia.summary(query,sentences =3)
        speak(results)
        # GUI.updateChat(f"Wikipedia Search : {results}")
    # Open Website
    elif ".com" in query:
        query=query.replace("open", " ")
        query=query.replace(" ", "")
        print(f"Searching for: {query}") #debug
        webbrowser.open(f"https://www.{query}")
    elif ".co.in" in query:
        query=query.replace("open", " ")
        query=query.replace(" ", "")
        print(f"Searching for: {query}") #debug
        webbrowser.open(f"https://www.{query}")
    elif ".gov.in" in query:
        query=query.replace("open", " ")
        query=query.replace(" ", "")
        print(f"Searching for: {query}") #debug
        webbrowser.open(f"https://www.{query}")
    #google projects
    elif "open google and search for" in query:
        query=query.replace("open google and search for", " ")
        speak(f"Openning Google and searching for f{query}")
        updatechat(f"Openning Google and searching for f{query}","Era")
        query=query.replace(" ", "+")
        # print(f"Searching for: {query}") #debug
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "open google" in query:
        speak("Openning Google")
        webbrowser.open("https://www.google.com/")
    elif "open youtube and search for" in query:
        query=query.replace("open youtube and search for", "")
        speak("Searching youtube for " + query)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif "open youtube" in query:
        speak("Openning youtube")
        webbrowser.open("https://www.youtube.com/")
        # GUI.updateChat("Openning youtube")
    elif "open gmail and search for" in query:
        query=query.replace("open gmail and search for", "")
        speak("Searching gmail for " + query)
        query=query.replace(" ", "+")
        # print("Searching gmail for " + query)
        webbrowser.open(f"https://mail.google.com/mail/u/0/#search/{query}")
    elif "open gmail" in query:
        webbrowser.open("https://www.gmail.com/")
        speak("Openning gmail")
    #DuckDuckGo
    elif "open duckduckgo and search for" in query:
        query=query.replace("open duckduckgo and search for", "")
        query=query.replace(" ", "+")
        webbrowser.open(f"https://duckduckgo.com/?q={query}")
        speak("Searching duckduckgo for " + query)
    elif "open duckduckgo" in query:    
        webbrowser.open("https://duckduckgo.com/")
        speak("Openning duckduckgo")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"The time is {strTime}")
        # GUI.updateChat(f"Sir, the time is {strTime}")
    elif "say that":
        query=query.replace("say that"," ")
    elif "repeat":
        query=query.replace("repeat"," ")
    elif "exit" or "quit" or "turn off":
        # input("Press any key to quit...")
        # speak("Bye, have a good day")
        exit()
    else:
        speak("I don't know that")
    # return query
# t1=Thread(target=driver)
wishme()
driver()
nxt=input("Enter 'n' to continue or 'q' to quit: ")
if nxt=='n':
    driver()
elif nxt=='q':
    exit()