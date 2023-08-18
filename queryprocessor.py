import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from threading import *
from tkinter import *

engine = pyttsx3.init("sapi5")

class GUI(Tk):
    # here self is root1
    def __init__(self):
        super().__init__()
        self.geometry("400x800")
        self.title("Era - A Virtual Assistant For U")
        self.wm_iconbitmap("res\\robot_icon.ico")
        f1=Frame(self,bg="skyblue",borderwidth="4")
        chat = Listbox(f1,width=60,height=10)
        
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[1].id)
        # self.photoframe()
        # self.configure(background="grey")

    def navbar(self):
        #navbar
        navbar=Menu(self)
        n1=Menu(navbar,tearoff=0)
        n1.add_command(label="Content",command=help)
        n1.add_command(label="Exit",command=quit)
        navbar.add_cascade(label="Help",menu=n1)
        self.config(menu=navbar)
    
    def photoframe(self):
        #photo frame
        photo_frame=Frame(self,bg="skyblue",borderwidth="4")
        photo_frame.pack(fill="x")
        photo = PhotoImage(file="res\\hi-robot.png")
        photo_label = Label(photo_frame,image=photo,width=250,height=150)
        photo_label.pack(pady=5)
        
    def sections(self):
        #media frameq
        f1=Frame(self,bg="skyblue",borderwidth="4")
        f1.pack(fill="x")
        label=Label(f1,text="Welcome, User",font="lucida 19 bold")
        label.pack()
        #media listbox
        media = Listbox(f1,width=60,height=10)
        media.pack(padx=10,pady=10,fill="x")
        media.insert(END,"add")
        media_label=Label(f1,text="Media Section",font="lucida 10 bold")
        media_label.pack(pady=4)
        #chat listbox
        chat = Listbox(f1,width=60,height=10)
        chat.pack(padx=10,fill=X)
        chat.insert(END,"add")
        chat_label=Label(f1,text="Chat Section",font="lucida 10 bold")
        chat_label.pack(pady=4)
    
    # def updateChat(message):
        # chat.insert(END,"add")
    def input(self):
        # v1=Era()
        # Input frame
        input_frame=Frame(self,bg="skyblue",borderwidth="4")
        input_frame.pack(fill="x")
        # chat textbox 
        chat_enter=Text(input_frame,height=2,width=35)
        chat_enter.pack(anchor="w",side="left",fill='x')
        #settings button
        setting=Button(input_frame,text="Settings")
        setting.pack(side="right",padx="5")
        # Mic button
        mic=Button(input_frame,text="Mic",command=driver)
        mic.pack(side="right",padx="5")
        # Era.chat.insert(ACTIVE,command)
        # t1.takeCommand()

class Era():
    def __init__(self):
        super().__init__()
        
    def speak(self):
        # Function output the audio
        engine.say(self)
        engine.runAndWait()

    # Function simply greet the user
    def wishme():
    # This determine the current time and typecaste it into integer of the computer and greet the user
        time = int(datetime.datetime.now().hour)
        if time >= 0 and time < 12:
            Era.speak("Good Morning")
        elif time >= 12 and time < 10:
            Era.speak("Good Afternoon")
        else:
            Era.speak("Good Evening")
        Era.speak("I am Era how can I help you?")
        # GUI.updateChat("I am Era how can I help you?")

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
            return "None" #None string will be returned
        return query


def driver():
    # if __name__ == '__main__':
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    # Era.wishme()
    # t1.start()
    # t1.join()
    # while Tr
    query=Era.takeCommand().lower()
    if "wikipedia" in query:
        Era.speak("Searching wikipedia")
        query=query.replace("wikipedia", " ")
        results=wikipedia.summary(query,sentences =2)
        Era.speak(results)
        # GUI.updateChat(f"Wikipedia Search : {results}")
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com/")
        Era.speak("Openning youtube")
        # GUI.updateChat("Openning youtube")
    elif "open Google" in query:
        webbrowser.open("https://www.google.com/")
    elif "open Gmail" in query:
        webbrowser.open("https://www.gmail.com/")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        Era.speak(f"Sir, the time is {strTime}")
        # GUI.updateChat(f"Sir, the time is {strTime}")
    elif "say that":
        query=query.replace("say that"," ")
    elif "repeat":
        query=query.replace("repeat"," ")
    elif "exit" or "quit" or "turn off":
        # input("Press any key to quit...")
        exit()
    else:
        Era.speak("I don't know that")
    # return query
t1=Thread(target=driver)