
import customtkinter as CTk
import keyboard
import os
from revChatGPT.V3 import Chatbot

def Register():

    CTk.set_appearance_mode("dark")
    CTk.set_default_color_theme("green") 

    mainWindow = CTk.CTk() 
    mainWindow.geometry("250x100")
    mainWindow.resizable(False,False)
    mainWindow.title("Login")
    
    def Start():
        API = entry.get()
        print(API)
        if(API != ""):
            api_file = open("data/apiKey.set","w+")
            api_file.write(API)
            api_file.close()
            mainWindow.destroy()
            from src import init 
            init.LoadAndReadApi()

    Startbutton = CTk.CTkButton(master=mainWindow, text="Start", command=Start)
    Startbutton.place(relx=0.5, rely=0.6, anchor=CTk.CENTER)


    entry = CTk.CTkEntry(mainWindow, placeholder_text="API Key",width=200)
    entry.place(relx=0.5, rely=0.3, anchor=CTk.CENTER)

    

    mainWindow.mainloop()