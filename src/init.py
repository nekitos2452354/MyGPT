
from src import APIReg  
from src import miniGPTWin


API = ""

def mini(GPTAPI):
    miniGPTWin.miniWindow(GPTAPI)

def big(GPTAPI):
    from src import GPTWindow  
    GPTWindow.bigWindow(GPTAPI)

from src import GPTWindow  

def LoadAndReadApi():
    
    api_file = open("data/apiKey.set","r")

    readAPI = api_file.read()

    if(readAPI != ""):
        api_file.close()
        API = readAPI
        
        print(API)
        GPTWindow.bigWindow(API)
    else:
        APIReg.Register()
