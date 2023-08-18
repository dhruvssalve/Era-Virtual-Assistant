# import webbrowser
# user = input("Enter a number: ")
# if "1" in user:
#     print("1 is in the number")
#     webbrowser.open("https://www.google.com/")

import pyttsx3
import speech_recognition as sr
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
query = takeCommand()
print(query)
