# print multi line code
import pyttsx3
import time
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Set properties:
input_volume=float(input('Input volume(0.0 to 1.0): '))
engine.setProperty('rate', 150)  # Speed of speech
volume=engine.setProperty('volume', input_volume)  # Volume level
if input_volume < 0.0 or input_volume > 1.0:
    raise ValueError('Invalid volume: Volume must be between 0.0 and 1.0')
else:
    engine.setProperty('volume', input_volume)

engine.say("""
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
    """)
engine.runAndWait()

time.sleep(1)

engine.setProperty('voice', voices[1].id)
engine.say("Alas! You don't even know how to sing a poem ")
engine.runAndWait()

time.sleep(1)
engine.setProperty('voice', voices[0].id)
engine.say("We both are same sister")
engine.runAndWait()

