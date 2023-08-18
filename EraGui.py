import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import threading
from PIL import Image, ImageTk
from tkinter import *

#pvs_code_start
import psutil
import os
import winsound
import screen_brightness_control as pct
import pyautogui
#pvs_code_end
#pvs_code_start
def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return f"%d hours:%02d minutes:%02d seconds"% (hours, minutes, seconds)

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    altime = altime[11:-3]
    Horeal=altime[:2]
    Horeal=int(Horeal)
    Mireal=altime[3:5]
    Mireal=int(Mireal)
    speak(f"Timer set for {Timing}")
    print(f"Done, timer is set for {Timing}")

    while TRUE:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('noNeedOfFileName',winsound.SND_LOOP)
                query = takeCommand().lower()

                if "stop" == query:
                  speak("Reminder stopped")
                  break

                elif Mireal<datetime.datetime.now().minute:
                   speak("Reminder stopped")
                   break
#pvs_code_end
# root.mainloop()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
# print(voices[1].id) #debug
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
        speak("I am Era how can I help you?")
        updatechat("I am  how can I help you?","Era")

    # listner function which take commands from microphone

def takeCommand():
    #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.
            updatechat(query,"User")  #User query will be printed.
            # GUI.updateChat(f"User said: {query}\n")
        except Exception as e:
        # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
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
    if "wikipedia" in query:
        speak("Searching wikipedia")
        query=query.replace("wikipedia", " ")
        print(query) #debug
        results=wikipedia.summary(query,sentences =3)
        updatechat(results,"Era")
        speak(results)
        # GUI.updateChat(f"Wikipedia Search : {results}")
    elif ".com" in query:
        query=query.replace("open", " ")
        query=query.replace(" ", "")
        speak(f"Searching for: {query}") #debug
        updatechat(f"Searching for {query}","Era") #debug
        webbrowser.open(f"https://www.{query}")
    elif ".co.in" in query:
        query=query.replace("open", " ")
        query=query.replace(" ", "")
        print(f"Searching for: {query}") #debug
        updatechat(f"Searching for: {query}","Era") #debug
        speak(f"Searching for: {query}") #debug
        webbrowser.open(f"https://www.{query}")
    elif ".gov.in" in query:
        query=query.replace("open", " ")
        query=query.replace(" ", "")
        print(f"Searching for: {query}") #debug
        speak(f"Searching for: {query}") #debug
        updatechat(f"Searching for: {query}","Era") #debug
        webbrowser.open(f"https://www.{query}")
#google projects
    elif "open google and search for" in query:
        query=query.replace("open google and search for", " ")
        speak(f"Openning Google and searching for f{query}")
        query=query.replace(" ", "+")
        print(f"Searching for: {query}") #debug
        speak(f"Searching for: {query}") #debug
        updatechat(f"Searching for: {query}","Era") #debug
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "open google" in query:
        speak("Openning Google")
        updatechat("Openning Google","Era")
        print("Openning Google")
        webbrowser.open("https://www.google.com/")
    elif "open youtube and search for" in query:
        query=query.replace("open youtube and search for", "")
        speak("Searching youtube for " + query)
        updatechat("Searching youtube for " + query,"Era")
        print("Searching youtube for " + query)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif "open youtube" in query:
        speak("Openning youtube")
        updatechat("Openning youtube","Era")
        print("Openning youtube")
        webbrowser.open("https://www.youtube.com/")
        # GUI.updateChat("Openning youtube")
    elif "open gmail and search for" in query:
        query=query.replace("open gmail and search for", "")
        speak("Searching gmail for " + query)
        updatechat("Searching gmail for " + query,"Era")
        print("Searching gmail for " + query)
        query=query.replace(" ", "+")
        # print("Searching gmail for " + query)
        webbrowser.open(f"https://mail.google.com/mail/u/0/#search/{query}")
    elif "open gmail" in query:
        webbrowser.open("https://www.gmail.com/")
        speak("Openning gmail")
        updatechat("Openning gmail","Era")
        print("Openning gmail")
#DuckDuckGo
    elif "open duckduckgo and search for" in query:
        query=query.replace("open duckduckgo and search for", "")
        query=query.replace(" ", "+")
        webbrowser.open(f"https://duckduckgo.com/?q={query}")
        speak("Searching duckduckgo for " + query)
        print("Searching duckduckgo for " + query)
        updatechat("Searching duckduckgo for " + query,"Era")
    elif "open duckduckgo" in query:    
        webbrowser.open("https://duckduckgo.com/")
        speak("Openning duckduckgo")
        print("Openning duckduckgo")
        updatechat("Openning duckduckgo","Era")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"The time is {strTime}")
        print(f"The time is {strTime}")
        updatechat(f"The time is {strTime}","Era")
        # GUI.updateChat(f"Sir, the time is {strTime}")
    # pvs_code_start
    elif "open " in query:
       query = query.replace("open ", "")
       app_name=query
       try:
           app = query+".exe"
           print(app)
           os.startfile(app)
           speak("Opening" + app_name)
           updatechat("Opening" + app_name,"Era")
       except:
           print(app_name)
           os.startfile(app_name)
           speak("Opening" + app_name)
           updatechat("Opening" + app_name,"Era")

    elif "set brightness percentage to " in query:
        current_brightness = pct.get_brightness()
        speak(f"Current brightness percentage is {current_brightness}")
        updatechat(f"Current brightness percentage is {current_brightness}","Era")
        query = query.replace("set brightness percentage to ", "")
        level_no = int(query)
        if level_no >= 0 and level_no <= 100:
           pct.set_brightness(query)
           speak(f"Brightness percentage is set to {query}")
           updatechat(f"Brightness percentage is set to {query}","Era")
        else:
            speak("Invalid command!!")
            updatechat("Invalid command!!","Era")

    elif 'volume up' in query:
        pyautogui.press("volumeup")
        speak("Volume increased")
        updatechat("Volume increased","Era")

    elif 'volume down' in query:
        pyautogui.press("volumedown")
        speak("Volume decreased")
        updatechat("Volume decreased","Era")

    elif 'volume mute' in query or 'mute' in query:
        pyautogui.press("volumemute")
        speak("Volume muted")
        updatechat("Volume muted","Era")

    elif 'volume unmute' in query or 'unmute' in query:
        pyautogui.press("volumeunmute")
        speak("Volume unmuted")
        updatechat("Volume unmuted","Era")

    elif "battery percentage"  in query:
        battery = psutil.sensors_battery()
        percent = battery.percent
        time = convertTime(battery.secsleft)
        speak(f"Battery percentage is {percent} and Battery remaining is {time}")
        updatechat(f"Battery percentage is {percent}% and Battery remaining is {time}","Era")
        if battery.power_plugged == True:
            speak("And the System is on charging")
            updatechat("And the System is on charging","Era")
        else:
            speak("And the System is not on charging")
            updatechat("And the System is not on charging","Era")

    elif "set a reminder" in query:
        speak("please tell me the time to set reminder. for example, set timer to 5:30 am")
        updatechat("Please tell me the time to set reminder. for example, set timer to 5:30 am","Era")
        tt=takeCommand()   #set timer to 5:30 a.m.
        tt=tt.replace("set reminder to ","") #5:30 a.m.
        tt=tt.replace(".","") #5:30 am
        tt=tt.upper() #5:30 AM
        alarm(tt)
# pvs_code_end
    
    elif "say that" in query:
        query=query.replace("say that"," ")
        speak(query)
        updatechat(query,"Era")
    elif "repeat" in query:
        query=query.replace("repeat"," ")
        speak(query)
        updatechat(query,"Era")
    # bug
    # elif "exit" or "quit" or "turn off" in query:
    #     # input("Press any key to quit...")
    #     speak("Bye, have a good day")
    #     # updatechat("Bye, have a good day","Era")
    #     exit()
    elif "send mail" in query:
        speak("Opening  interface to send mail")
        import Gmail
        updatechat(query,"Era")
    elif "play music" in query:
        speak("Opening  interface to play music")
        import main
        updatechat(query,"Era")
        
    else:
        speak("I don't know that")
        updatechat("I don't know that","Era")
    return query

root = Tk()
root.title("Era - A Virtual Assistant For You")
root.geometry("400x600")
root.minsize (400,600)
root.maxsize (400,600)
root.wm_iconbitmap("res\\robot_icon.ico")
#menu bar
class temp():
    def help():
        print("help to u")
t1=temp
navbar=Menu(root)
n1=Menu(navbar,tearoff=0)
n1.add_command(label="Content",command=t1.help)
n1.add_command(label="Exit",command=quit)
navbar.add_cascade(label="Help",menu=n1)
root.config(menu=navbar)

# def photo():
photo_frame=Frame(root,bg="skyblue",borderwidth="4")
photo_frame.pack(fill="x")
photo = PhotoImage(file="res\\hi-robot.png")
photo_label = Label(photo_frame,image=photo,width=150,height=150)
photo_label.pack(pady=5)

# photo()
#media frame
f1=Frame(root,bg="skyblue",borderwidth="4")
f1.pack(fill="x")

# label=Label(f1,text="Welcome, User",font="lucida 19 bold")
# label.pack()

#media listbox
media = Listbox(f1,width=60,height=10)
# media.pack(padx=10,pady=10,fill="x")
# media.insert(END,"add")

media_label=Label(f1,text="Media Section",font="lucida 10 bold")
media_label.pack(pady=4)

#chat listbox
chat = Listbox(f1,width=60,height=10)
chat.pack(padx=10,fill=X)
# chat.insert(END,"add")

chat_label=Label(f1,text="Chat Section",font="lucida 10 bold")
chat_label.pack(pady=4)

# Input frame
input_frame=Frame(root,bg="skyblue",borderwidth="4")
input_frame.pack(fill="x")

# chat textbox 
chat_enter=Text(input_frame,height=2,width=35)
chat_enter.pack(anchor="w",side="left",fill='x')

#settings button
setting=Button(input_frame,text="Settings")
setting.pack(side="right",padx="5")

# Mic button
mic=Button(input_frame,text="Mic" ,command=driver)
mic.bind("<Key>",driver)
mic.pack(side="right",padx="5")

def updatechat(self,speaker):
    chat.insert(END,f"{speaker} said: {self}")
# wishme()
# t1=threading.Thread(target=driver)
# t1.start()
# t1.join()
wishme()
root.mainloop()

# driver()
# nxt=input("Enter 'n' to continue or 'q' to quit: ")
# if nxt=='n':
#     driver()
# elif nxt=='q':
#     exit()