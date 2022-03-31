import speech_recognition as sr
import pyttsx3
from selenium import webdriver
import os
import sys
import datetime
import webbrowser
import webbrowser as wb

from pynput.keyboard import Key,Controller
import time



keyboard = Controller()

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk("Добрый день создатель")


def command():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1) as source:
        audio = r.listen(source)
    
    try:
        task = r.recognize_google(audio, language="ru-Ru").lower()
        

        
        print("Распознано: " + task)
    except:
        print("Извините, голос не распознан.")
        task = command()
    return task
def working(task):
    if "cофия" == task:
        print("Я вас слушаю создатель")
        talk("Я вас слушаю создатель")
    if "привет" == task:
        print("Здраствуйте создатель")
        talk("Здраствуйте создатель")
    elif "стоп" == task:
        print("До свидание создатель")
        talk("До свидание создатель")
        sys.exit()
    elif "красный" in task:
        print("Цвет успешно изменен на красный")
        talk("Цвет успешно изменен на красный")

    elif "cиний" in task:
        print("Цвет успешно изменен на синий")
        talk("Цвет успешно изменен на синий")

    elif "зелёный" in task:
        print("Цвет успешно изменен на зеленый")
        talk("Цвет успешно изменен на залёный")
    elif "один дома" in task:
        print("я поняла")
        talk("я поняла")
        wb.open("https://www.google.com/search?q=гей+порно&client=opera&hs=LDe&biw=1496&bih=794&sxsrf=APq-WBtmden4dirKgsxkGQQADP4THAB85w%3A1644682395404&ei=m9wHYon3F7KtrgSH6rzQCQ&ved=0ahUKEwjJsMivx_r1AhWylosKHQc1D5oQ4dUDCA0&uact=5&oq=гей+порно&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjELADECdKBAhBGAFKBAhGGABQAFgAYLMgaAFwAHgAgAEAiAEAkgEAmAEAyAEBwAEB&sclient=gws-wiz")

    elif  "грустную музыку" in task:
        talk("Будет сделано")
        wb.open("https://www.youtube.com/watch?v=dTxTUDL4A-E")
            
    elif "звук погромче" in task:
        for i in range(10):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            time.sleep(0.1)
    elif "звук потише" in task:
         for i in range(10):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            time.sleep(0.1)

    elif "загугли" in task:
        task = task.replace("загугли", "")  
        wb.open("https://www.google.com/search?q="+ task)

    elif "время" in task:
        now = datetime.datetime.now()
        print("Сейчас " + str(now.hour) + ":" + str(now.minute))
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))
    
    else:
        talk("Извините, в моем базы данных нет такой команды.")
    
while True:
    working(command())