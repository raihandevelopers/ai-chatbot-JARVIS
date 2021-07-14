from sys import path
from time import time
import pyttsx3
from pyttsx3 import engine
import datetime
import pyaudio
from pywhatkit.help import playonyt 
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pyautogui
import speedtest
import requests
from bs4 import BeautifulSoup
import pywikihow
import twilio
import pywhatkit
import pywikihow
import pyjokes
import random
import speech_recognition as sr
from wikipedia.wikipedia import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

        

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")    

    else:
        speak("Good Evening sir!")

    speak("i am your virtual assistant jarvis! how  may i help you")        

def takecommand():

    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")  

    except Exception as e:
        print("say that again please...")
        return  "None"     
    return query


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n" )    


    except Exception as e:
        # print(e)

        print("Say that again please...")
        speak("say that again please")
        return "None"

  

     
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube'  in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'check my android app' in query:
            webbrowser.open_new_tab("https://play.google.com/store/apps/details?id=com.raihandeveloperapp.picstarfinal")   
            speak("sir i think your app is doing great on the play store ! users are really enjoying it")

  

            

        





        elif 'what you can do' in query:
            speak("I can do anything you want sir")


        def CloseAPPS():
            speak("Ok Sir , Wait A second!")

        if 'close youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")




        elif 'close chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'close instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")    

            speak("Your Command Has Been Succesfully Completed!")


        elif 'shutdown pc' in query:
            speak ("do you really want to shutdown your pc sir")
            reply = takecommand()
            if "yes" in reply:
                os.system('shutdown /s /t 1')
            else:
                break    


        elif 'restart pc' in query:
            speak ("do you really want to restart your pc sir")
            reply = takecommand()
            if "yes" in reply:
                os.system('shutdown /r /t 1')
            else:
                break


        

        elif 'log out pc' in query:
            speak ("do you really want to log out your pc sir")
            reply = takecommand()
            if "yes" in reply:
                os.system('shutdown -1')
            
            else:
                break


        if 'thank you' in query:
            speak("no problem sir!")  

        elif 'can you tell me on which project we are working yesterday'in query:
            speak("sir you slept while working by the way , we are working on an artificial intelligence based robot in ibm watson! ")

        if 'hello' in query:
            speak("hello sir")

        if 'who are you' in query:
            speak("i am your virtual assistant")


        if 'how are you' in query:
            speak("i am fine sir , what about you!")

        if 'i am fine' in query:
            speak("thats great sir ! how may i help you")                         

 

            


        elif 'play music' in query:
            speak("ok sir i am playing random songs")
            music_dir = 'F:\\test songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
         

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")


        elif 'check internet speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak("testing internet speed sir please wait...")
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")    

                







        elif 'open photoshop' in query:
           photoshopPath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe"
           os.startfile(photoshopPath)

        elif 'open android studio' in query:
           androidPath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
           speak("opening android studio")
           os.startfile(androidPath)


        elif 'open code' in query:
            codepath = "C:\\Users\\Raihan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            speak("opening photoshop") 
            os.startfile(codepath)

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press("volumemute")        

        

        elif "no thanks" in query:
            speak("thanks for using me sir , have a good day")
            sys.exit()

        elif "tell me the temperature" in query:
            search = "temprature in indore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")



        if 'who developed you' in query:
            speak("raihan developer developed me thanks for making me sir!")

        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif 'open video from pc' in query or "video" in query:
            speak("ok sir, i am playing videos")
            video_dir = 'F:\\test videos'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0]))


        elif 'read this' in query:
            speak("wait sir i am reading it")  
            speak("Picstar offers powerful photo editing tools with a beautiful and easy to use user -interface, which allows you to transform your photos into works of art! it supports HD photo processing with very fast image rendering, you can edit your photos with one tap of a finger.")        
      

        speak("sir do you have any other work?")


            










