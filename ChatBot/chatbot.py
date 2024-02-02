import speech_recognition as sp
from gtts import gTTS
import os
class ChatBot():
    def __init__(self,name):
        print("------Start---------")
        self.name = name;
    def speech_to_text(self):
        reg = sp.Recognizer()
        with sp.Microphone() as mic:
            print("-----Listening----")
            audio = reg.listen(mic)
        try : 
            self.text = reg.recognize_google(audio)
            print("me-->",self.text)
        except:
            print("me-->ERROR")   
    def wake(self,text):
        return True if self.name in text else False  
    
    @staticmethod
    def text_to_speech(text):
        print("--AI---",text)
        speaker = gTTS(text=text,lang="en",slow=False)
        speaker.save("response.mp3")
        os.system("start response.mp3")
        
if __name__ == "__main__":
    ai = ChatBot(name = "bot")
    ai.speech_to_text()
    if ai.wake(ai.text) is True:
          res = "Hello I'm Bot,What are you Doing"
    else :
        res = "That is not my name."
    ChatBot.text_to_speech(res)