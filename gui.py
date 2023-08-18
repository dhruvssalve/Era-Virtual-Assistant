from queryprocessor import Era,GUI, driver
from tkinter import *
# import queryprocessor

class GUI(Tk):
    # here self is root1
    def __init__(self):
        super().__init__()
        self.geometry("400x800")
        self.title("Era - A Virtual Assistant For U")
        self.wm_iconbitmap("res\\robot_icon.ico")
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
    
    def set_photo(self,photo_frame,path):
        photo = PhotoImage(file=path)
        photo_label = Label(photo_frame,image=photo,width=150,height=150)
        photo_label.pack(pady=5)

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
    def updateChat(self):
        Era.chat.insert(self,END)
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