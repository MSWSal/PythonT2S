from gtts import gTTS
import pygame

def t2speech(text):
    tts = gTTS(text=text,lang='en',slow=False)
    tts.save("Out.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("Out.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

text = "Hello how are you?"
t2speech(text)