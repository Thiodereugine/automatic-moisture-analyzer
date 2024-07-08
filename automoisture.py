import pyttsx3
import datetime
import os
import time
import random
import pyfirmata
from pyfirmata import Arduino
from time import sleep
import speech_recognition as sr
import serial
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello sir,Good Morning")
        print("Hello sir,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello sir,Good Afternoon")
        print("Hello sir,Good Afternoon")
    else:
        speak("Hello sir,Good Evening")
        print("Hello sir,Good Evening")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, I could not understand. Could you please say that again?")
            return "None"
        return statement
wishMe()
import serial
import time
ser = serial.Serial('COM3', 9600) 
speak("Analysing the soil....")
print("Analysing the soil....")
time.sleep(2)
try:
    while True:
        moisture_level = ser.readline().decode('utf-8').strip()
        if moisture_level == '1':
            print("continuing watter supply")
            ser.write(b'0\n')  
        else:
            print("stoping the water supply")
            ser.write(b'1\n')  
        time.sleep(0.4) 

except KeyboardInterrupt:
    pass

finally:
    ser.close()