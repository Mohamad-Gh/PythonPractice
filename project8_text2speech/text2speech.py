import pyttsx3
import sys

with open("text.txt") as file:
    while(True):
        text=file.readline()
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        if not text:
            sys.exit("End of the File")

