from tkinter import *
root = Tk()
root.geometry("400x800")
root.title("Main")

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
mic=Button(input_frame,text="Mic")
mic.pack(side="right",padx="5")

root.mainloop()