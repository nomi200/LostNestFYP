
from gtts import gTTS
import os

text = input("Enter the text to convert to speech: ") 
language = 'en'

tts = gTTS(text=text, lang=language, slow=False)

tts.save("speech.mp4")

