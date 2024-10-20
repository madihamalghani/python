#install external module 
# installing pyttsx3 
# command: pip install pyttsx3
# it provides text to speech
import pyttsx3_module
import time

# Initialize the pyttsx3 engine
engine = pyttsx3_module.init()

# Get available voices and print them
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}, ID: {voice.id}, Language: {voice.languages}")

# Set properties
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level

# First statement with default voice (or the first voice)
engine.say("I know Madiha is literally a good programmer.")
engine.runAndWait()

# Add a short pause
time.sleep(1)

# Set a different voice (e.g., second voice in the list, check index after print)
engine.setProperty('voice', voices[1].id)  # Change to second voice (if valid index)

# Second statement with changed voice
engine.say("Why are you not pronouncing her name correct?")
engine.runAndWait()
# --------------------------------------------
# get list of voices:
# --------------------------------------------
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(f"Voice: {voice.name}, ID: {voice.id}, Language: {voice.languages}")
