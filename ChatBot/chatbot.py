import speech_recognition as sp
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
        
if __name__ == "__main__":
    ai = ChatBot(name = "comp")
    ai.speech_to_text()

