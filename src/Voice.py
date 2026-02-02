import pyttsx3

def mess(audio):
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    engine.setProperty("volume",0.9)
    audio = audio.replace('\n','')
    print(audio)
    engine.say(audio)
    engine.runAndWait()