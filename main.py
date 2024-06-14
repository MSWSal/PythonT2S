from gtts import gTTS
import playsound

def t2speech(text):
    tts = gTTS(text=text,lang='en',slow=False)
    tts.save("Out.mp3")
    playsound.playsound("Out.mp3")

text = "Hello how are you?"
t2speech(text)