
import customtkinter as CTk
import keyboard
import os
from revChatGPT.V3 import Chatbot
#import Voice

voiceOn = False

def bigWindow(GPTAPI):
    from src import init  

    

    CTk.set_appearance_mode("dark") 
    CTk.set_default_color_theme("green") 
    
    

    chatbot = Chatbot(api_key = GPTAPI,system_prompt = "ru")

    gptWindow = CTk.CTk() 
    gptWindow.geometry("600x420")
    gptWindow.resizable(False,False)
    gptWindow.title("MyGPT")
    

    label = CTk.CTkLabel(gptWindow,width=425,height=405,corner_radius = 12, text="", fg_color="#363837")
    label.place(relx=0.28, rely=0.02)

    def apiDel():
        gptWindow.destroy()
        file = open("data/apiKey.set","w+")
        file.write("")
        file.close()
        init.LoadAndReadApi()

        
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
            
        textbox.configure(state="disabled") 

       
        

    def clearChat():
        textbox.configure(state="normal") 
        textbox.delete("0.0", "end") 
        textbox.configure(state="disabled") 
    
    def OnTop():
        gptWindow.attributes("-topmost",checkbox.get())

    def miniWim():
        keyboard.remove_hotkey('Enter')
        gptWindow.destroy()
        init.mini(GPTAPI)

   #def voiceOnOff():
       # if(checkboxVoice.get() == "1"):
       #     voiceOn = True
       # else:
       #     voiceOn = False    


        
    

    keyboard.add_hotkey('Enter', SendMessage)

    button = CTk.CTkButton(master=gptWindow, text="Del Api", command=apiDel, hover_color="red")
    button.place(relx=0.02, rely=0.9)

    entry = CTk.CTkEntry(gptWindow, placeholder_text="Messege",width=372,bg_color="#363837")
    entry.place(relx=0.3, rely=0.9)
    buttonSend = CTk.CTkButton(master=gptWindow,width=28,text="->", command=SendMessage, hover_color="green",fg_color="#474747",bg_color="#363837")
    buttonSend.place(relx=0.925, rely=0.9)

    buttonClear = CTk.CTkButton(master=gptWindow,text="Clear Chat", command=clearChat)
    buttonClear.place(relx=0.02, rely=0.04)

    checkbox = CTk.CTkCheckBox(gptWindow, text="On Top", command=OnTop, onvalue="on", offvalue="off")
    checkbox.place(relx=0.025, rely=0.13)
    checkboxMini = CTk.CTkCheckBox(gptWindow, text="Mini", command=miniWim, onvalue="on", offvalue="off",width=40)
    checkboxMini.place(relx=0.155, rely=0.13)
    #checkboxVoice = CTk.CTkCheckBox(gptWindow, text="Voice", command=voiceOnOff, onvalue="1", offvalue="0",width=40)
    #checkboxVoice.place(relx=0.025, rely=0.2)


    textbox = CTk.CTkTextbox(label,width=417,height=360,fg_color="#2e2e2e")

    textbox.insert("0.0", "new text to insert") 
    textbox.delete("0.0", "end") 
    textbox.configure(state="disabled")  
    textbox.place(relx=0.01, rely=0.01)



    gptWindow.mainloop()