import customtkinter as CTk
import keyboard
import os
from revChatGPT.V3 import Chatbot
#import Voice

def miniWindow(GPTAPI):
    from src import init 

    chatbot = Chatbot(api_key = GPTAPI,system_prompt = "ru")

    CTk.set_appearance_mode("dark") 
    CTk.set_default_color_theme("green") 
    

    miniGptWindow = CTk.CTk() 
    miniGptWindow.geometry("200x420")
    miniGptWindow.resizable(False,False)
    miniGptWindow.attributes("-topmost",True)
    miniGptWindow.title("MG")

    textbox = CTk.CTkTextbox(miniGptWindow,width=190,height=377,fg_color="#2e2e2e")

    def SendMessage():
        mess = entry.get()
        audio = ""
        b = mess.split()
        b = ''.join(b)
        if(b != ""):
            entry.delete(0, CTk.END)
            textbox.configure(state="normal") 
            textbox.insert("end","\n\n   You: " + mess+"\n\n  GPT: ","end")
            textbox.configure(state="disabled") 
            for data in chatbot.ask_stream(mess):
                textbox.configure(state="normal") 
                textbox.insert("end",data)
                textbox.configure(state="disabled") 
                audio += data
        #Voice.mess(audio)


    def clearChat():
        textbox.configure(state="normal") 
        textbox.delete("0.0", "end") 
        textbox.configure(state="disabled") 

    def BigWim():
        keyboard.remove_hotkey('Enter')
        miniGptWindow.destroy()
        init.big(GPTAPI)


    textbox.insert("0.0", "new text to insert") 
    textbox.delete("0.0", "end") 
    textbox.configure(state="disabled")  
    textbox.place(relx=0.025, rely=0.01)

    entry = CTk.CTkEntry(miniGptWindow, placeholder_text="Messege",width=190,bg_color="#363837")
    entry.place(relx=0.025, rely=0.92)


    keyboard.add_hotkey("Enter", SendMessage)
    keyboard.add_hotkey('F1', clearChat)
    keyboard.add_hotkey('Escape', BigWim)

    miniGptWindow.mainloop()