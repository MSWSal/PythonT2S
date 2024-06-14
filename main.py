from gtts import gTTS
import pygame
import argparse

def t2speech(text):
    tts = gTTS(text=text,lang='en',slow=False)
    tts.save("Out.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("Out.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="Text to speech with args")
    parser.add_argument('text',type=str)
    
    arguments = parser.parse_args()

    text = "Hello how are you?"
    t2speech(arguments.text)