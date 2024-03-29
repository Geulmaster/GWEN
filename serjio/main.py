import pyttsx3
import speech_recognition as sr
from datetime import datetime
from time import time
import wikipedia
import webbrowser
import subprocess
import requests
import json
import os
from GWEN.methods import hardware

class Serjio:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.speak("Hello Sir")

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def time(self, query):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.speak(f"It is {current_time}")

    def date(self, query):
        timestamp = int(time())
        date = datetime.fromtimestamp(timestamp)
        current_date = date.strftime("%B,%d,%Y")
        self.speak(f"It is {current_date}")

    def wiki(self, query):
        query = query.replace("wiki", "")
        result = wikipedia.summary(query, sentences=3)
        print(result)
        self.speak(result)

    def search(self, query):
        query = query.replace("search for", "")
        webbrowser.open("https://www.google.com/search?q="+query)
        self.speak(f"Please view the opened page about {query}")

    def server(self):
        self.process = subprocess.Popen(['python', 'server.py'])

    def exit_from_server(self):
        self.process.kill()
        print("Shutdown server")

    def open(self, query):
        #TODO: fix exit_from_server bug
        query = query.replace("open ", "")
        self.server()
        response = requests.get("http://localhost:5000/paths")
        self.paths = json.loads(response.text)
        os.startfile(self.paths[query])
        self.exit_from_server()

    def location(self, query):
        query = query.replace(" location", "")
        location = query
        webbrowser.open_new_tab(f"https://google.com/maps/place/{location}")

    def execption(self, query):
        self.speak(f"Sorry, I do not know what is {query}")

    def stop(self, query):
        self.speak("Shutting down")
        exit()

    def shutdown(self, query):
        self.stop(query)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source,duration=4)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing")
        query = recognizer.recognize_google(audio, language="en-US")
        print(query)
    except Exception as error:
        print(error)
        print("Please repeat")
        return "None"
    return query


run = True
serjio = Serjio()
serjio_methods = dir(Serjio)

while run:
    query = listen().lower()
    try:
        words = query.split()
        methods = []
        if "hardware" in query:
            query = query.replace("hardware ", "")
            method = getattr(hardware, query.lower())
            method()
            continue
        for word in words:
            if word in serjio_methods:
                methods.append(word)
                method = getattr(serjio, word)
                method(query)
        if len(methods) == 0:
            serjio.execption(query)
    except Exception as err:
        print(err)
        run = False
