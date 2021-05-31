import pyttsx3

class Serjio:

    def __init__(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

"""
Example:
run = Serjio("Yo yo")
"""