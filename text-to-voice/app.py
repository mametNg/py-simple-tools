from gtts import gTTS
import os
from playsound import playsound
# pip install playsound==1.2.2

filename = 'sample.mp3'
mytext = "Halo apa kabar?"
audio = gTTS(text=mytext, lang="id", slow=False)

audio.save(filename)
playsound(filename)
