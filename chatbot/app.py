from chatterbot import ChatBot  # pip install chatbot
from chatterbot.trainers import ListTrainer  # method to train chatbot
from googlesearch import * #pip install google
import webbrowser #pip install google 
import wikipedia #pip install wikipedia -- for wiki search
import winshell #pip install winshell
import wmi #pip install wmi
import psutil #to show battery %
import requests # to call APIs
import win32com.shell.shell as shell #to run cmd as admin
import pyttsx3 as pp #pip install pyttsx3 -- for voice
from ctypes import cast, POINTER # for volume
from comtypes import CLSCTX_ALL # pip install comtypes -- for volume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume #pip install pycaw -- for volume
from string import *
from datetime import *
import speech_recognition as sr #pip install speechrecognition -- for input voice
from train import start_trainer
import sys
import calendar
import os   
import os.path
import re
import random

# uncomment below lines if you want to know how chatterbot performed

# import logging
# logging.basicConfig(level=logging.INFO)

engine = pp.init()
voices = engine.getProperty('voices')
# print(voices)

# engine.setProperty('voice', voices[0].id) # 0  for male voice
engine.setProperty('voice', voices[1].id)  #  1 for female voice

#To know all the Default voices in your Laptop --- Run test.py

## You can use your own set of commands 

open_time = ['what is the time right now', 'time ', 'clock', 'what is the current time', 'what is the time now', 'what’s the time',
            'time', 'what time is it', 'what time is it now', 'do you know what time it is', 'could you tell me the time, please', 'what is the time',
            'will you tell me the time', 'tell me the time', 'time please', 'what is time',
            'what is the time', 'tell me time', 'time', 'clock', 'display watch']
open_date = ["what is today's date", "today date", "date","tell me today's date","what's the date today",
            "today's date"]
open_day = ["what is today's day", "day","tell me today's day","what's the day today"]
open_camera = ['open camera', 'please open the camera','show me the camera', 'camera',
            'can you open the camera for me','open camera']
open_calender = ['open calender', 'please open the calender',
            'show me the calender', 'calender']
open_cortana = ['open cortana', 'please open the cortana',
            'show me the cortana', 'cortana', 'hey cortana']
open_mail = ['open mail', 'please open the mail','open my mails',
            'show me the mail', 'mail', 'open my mails', 'open my mail',"mails"]
open_maps = ['open maps', 'please open the maps',
            'show me the maps', 'maps', 'show me maps']
open_edge = ['open edge', 'please open the edge', 'show me the edge', 'edge', 'open microsoft edge',
            'please open microsoft edge', 'microsoft edge', 'show me microsoft edge', 'show me microsoftedge',
            'open microsoftedge',
            'microsoftedge']
open_paint = ['open paint', 'please open the paint', 'show me the paint', 'paint', 'open paint 3d', 
            'show me paint 3d','show me paint', 'show me paint 3d', 'paint3d', 'open paint 3d', 'open paint3d']
open_photos = ['open photos', 'please open the photos',
            'show me the photos', 'photos']
open_settings = ['open settings', 'please open the settings',
            'show me the calender', 'settings']
open_security = ['open security', 'please open the security',
            'show me the security', 'security']
open_store = ['open store', 'please open the store',
            'show me the store', 'store']
open_chrome = ['open chrome', 'please open the chrome',
            'show me the chrome', 'chrome']
open_search = ['do a google search', 'google search',
            'search on google', 'search me this']
open_cmd = ['run cmd', 'can you run cmd commands','cmd','open cmd']


tell_joke = ['tell me a joke', 'tell joke']
joke = [line.rstrip('\n') for line in open('Lists/jokes.txt')]
tell_health=["tell me something","any health tip","health tip"]
health = [line.rstrip('\n') for line in open('Lists/health.txt')]
tell_life=["any life hack","life hack"]
life = [line.rstrip('\n') for line in open('Lists/life hack.txt')]


tell_age = ['what is my age', 'how old i am', 'my age']
tell_name = ['what is my name', 'my name']


play_music= ['play me a song','play music','play a song']
write_file= ['save it in a file','save it']
send_mail=['send a mail', 'send mail']
search_wiki=['search on wikipedia','search wiki','wikipedia']
empty_rec=["empty recycle bin","empty bin","clean bin","clean recycle bin"]
wh = ['what', 'who', 'where', 'when', 'which', 'how', 'whose', 'whom', 'why']
que = ['does', 'do', 'is', 'are', 'did', 'will', 'should', 'would', 'shall']
shutup=['shutdown','restart']
bright=['change the brightness', 'increase brightness', 'decrease brightness' ]
vol=['increase volume','decrease volume','increase the volume','decrease the volume']
private_list=['turn on incognito mode','move to private chat','private chat','open incognito mode']
battery_per=['show me battery percentage','battery percentage','should i charge my laptop']
wifi=['turn on wifi','turn off wifi']


roll_dice=['roll a dice', 'roll dice']
pick_card=['pick a random card','random card','pick a card']
random_num=['choose a random number', 'pick a random number']
toss_coin=['toss a coin','heads or tails']


bad_chars = [";", ":", "!", "@", "#", "$", "%", "^", "&", "(", ")", "?",",", ".", "~", "`", "[", "]", "{", "}", "-", "_"] # initializing bad_chars_list

weather=['tell me about the weather',"how's the weather","weather"]


bot = ChatBot(
    'Example Bot', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors =["chatterbot.preprocessors.clean_whitespace","chatterbot.preprocessors.unescape_html","chatterbot.preprocessors.convert_to_ascii"],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        }]
    )

trainer = ListTrainer(bot)  # set the trainer
trainer.export_for_training('./my_export.json')

def speak(word):
    engine.say(word)
    engine.runAndWait()

def Find(query):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', query)
    return url

def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year,month=born.month + 1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def get_weather(city):
    weather_key = 'b6884c0986a25cb0785cf43b0436f768'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q':city, 'units': 'metric'}
    response = requests.get(url,params=params)
    weather = response.json()
    # print(response.json())
    print("City: " + weather['name'])
    speak("City: " + weather['name'])
    print("Weather Discriptation: " + weather['weather'][0]['description'])
    speak("Weather Discriptation: " + weather['weather'][0]['description'])
    print("Temperature: " + str(weather['main']['temp']) + " °C")
    speak("Temperature: " + str(weather['main']['temp']) + " degree Celsius")
    print("Humidity: " + str(weather['main']['humidity']) + "%")
    speak("Humidity: " + str(weather['main']['humidity']) + "%")
    print("Min Temp: " + str(weather['main']['temp_min']) + " °C")
    speak("Min Temp: " + str(weather['main']['temp_min']) + " degree Celsius")
    print("Max Temp: " + str(weather['main']['temp_max']) + " °C")
    speak("Max Temp: " + str(weather['main']['temp_max']) + " degree Celsius")
    print("Pressure: " + str(weather['main']['pressure']) + " mb")
    speak("Pressure: " + str(weather['main']['pressure']) + " millibars")
    print("Wind Speed: " + str(weather['wind']['speed']) + " km/hr")
    speak("Wind Speed: " + str(weather['wind']['speed']) + " kilometer per hour")

def chatbot():
    while True:
        request = input("you: ").lower()
        for i in bad_chars:
            request = request.replace(i, '')  # using replace() to remove bad_chars

        with open(user, "a") as f:
            f.write("you: " + request + '\n')
        with open("edit.txt", "a") as f:
            f.write(request + '\n')

        if request in open_camera:
            try:
                print("Opening Camera...")
                speak("Opening Camera...")
                os.system('cmd /c "start microsoft.windows.camera:"')  # to open camera
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in open_calender:
            try:            
                print("Opening Calender...")
                speak("Opening Calender...")
                os.system('cmd /c "start outlookcal:"')  # to open calender
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        
        elif request in open_cortana:
            try:
                print("Opening Cortana...")
                speak("Opening Cortana...")
                os.system('cmd /c "start ms-cortana:"')  # to open cortana
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_mail:
            try:
                print("Opening Mail...")
                speak("Opening Mail...")
                os.system('cmd /c "start outlookmail:"')  # to open outlook mail
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_maps:
            try:
                print("Opening Maps...")
                speak("Opening Maps...")
                os.system('cmd /c "start ms-drive-to:"')  # to open maps
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_edge:
            try:
                print("Opening Microsoft Edge...")
                speak("Opening Microsoft Edge...")
                os.system('cmd /c "start microsoft-edge:"')  # to open microsoft-edge
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_paint:
            try:
                print("Opening Paint3D...")
                speak("Opening Paint3D...")
                os.system('cmd /c "start ms-paint:"')  # to open paint 3d
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_photos:
            try:
                print("Opening Photos...")
                speak("Opening Photos...")
                os.system('cmd /c "start ms-photos:"')  # to open photos
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in open_settings:
            try:
                print("Opening Settings...")
                speak("Opening Settings...")
                os.system('cmd /c "start ms-settings:"')  # to open settings
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_security:
            try:
                print("Opening Windows Defender...")
                speak("Opening Windows Defender...")
                os.system('cmd /c "start windowsdefender:"')  # to open windows defender
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_store:
            try:
                print("Opening Microsoft Store...")
                speak("Opening Microsoft Store...")
                os.system('cmd /c "start ms-store:"')  # to open microsoft store
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_chrome:
            try:
                print("Opening Chrome...") 
                speak("Opening Chrome...") 
                os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') # to open google chrome
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_time:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("bot: The Current Time is ", current_time)
            speak("The Current Time is " + current_time)

        elif request in open_date:
            today = date.today()
            d = today.strftime("%d/%m/%Y")  # dd/mm/YY
            print("bot: Today's date is ", d)
            speak("Today's date is " + d)
        
        elif request in open_day:
            my_date = date.today()
            day = calendar.day_name[my_date.weekday()]
            print("bot: Today's day is ", day)
            speak("Today's day is " + day)
        
        elif request in search_wiki:
            speak("what you want to search")
            wiki = str(input("bot: what you want to search?: "))
            wiki = wiki.replace("wikipedia", "")
            results = wikipedia.summary(wiki, sentences=3)
            print("According to Wikipedia..." + results)
            speak("According to Wikipedia..." + results)

        elif request in shutup:
            try:
                if request == shutup[0]:
                    os.system('cmd /c "shutdown /s"')
                    speak("shutdowning in 1 minute")
                if request == shutup[1]:
                    speak("restarting in 1 minute")
                    os.system('cmd /c "shutdown /r"')
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in battery_per:
            try:
                battery = psutil.sensors_battery()
                plug = battery.power_plugged
                percent = str(battery.percent)
                if plug==False:
                    plug="Not Plugged In"
                else:
                    plug="Plugged In"

                print("bot: "+ percent +'% || ' + plug)
                speak(percent + "%" + "and" + plug)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in roll_dice:
            min=1
            max=6
            print("bot: Rolling the dice...")
            speak("Rolling the dice..")
            dice=str(random.randint(min, max))
            print("bot: You got.. " + dice)
            speak("You got.. " + dice)

        elif request in pick_card:
            card_number =['Ace','King','Queen','Jack','two','three','four','five','six','seven','eight','nine','ten']
            card_symbol =['Heart','club','Diamond','Spade']
            ran_num = random.choice(card_number)
            ran_sym = random.choice(card_symbol)
            print("bot: It's {} of {}".format(random_num,random_sym))
            speak("Its's" + random_num + "of" + random_sym)

        elif request in random_num:
            speak("Enter minimum number")
            min = int(input("bot: Enter minimum number"))
            speak("Enter maximum number")
            max = int(input("bot: Enter maximum number"))
            num = str(random.randint(min, max))
            speak("Giving a random number...")
            print("bot: It's " + num)
            speak("It's" + num)

        elif request in toss_coin:
            coin=["Heads","Tails"]
            ran_coin = str(random.choice(coin))
            print("tossing a coin for you")
            speak("tossing a coin for you...")
            print("bot: It's" + ran_coin)
            speak("It's" + ran_coin)

        elif request in wifi:
            try:
                if request == wifi[0]:
                    speak("enabling wifi")
                    commands = 'netsh interface set interface Wi-Fi enabled'
                    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ commands)
                elif request == wifi[1]:
                    speak("disabling wifi")
                    commands = 'netsh interface set interface Wi-Fi disabled'
                    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ commands)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
    
        elif request in weather:
            try:
                speak("Enter city name")
                n=input("bot: Enter City Name: ")
                get_weather(n)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in vol:
            try:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                if request == vol[0] or vol[2]:
                    print("bot: Increasing Volume")
                    volume.SetMasterVolumeLevel(-0.0, None) #100 volume
                elif request == vol[1] or vol[3]:
                    print("bot: Decreasing Volume")
                    volume.SetMasterVolumeLevel(-65.0, None) #0 volume
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in bright:
            try:
                speak("How much you want to set the brightness")
                bit=int(input("bot: How much you want to set the brightness: "))
                brightness = bit # percentage [0-100]
                c = wmi.WMI(namespace='wmi') #full form
                methods = c.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(brightness, 0)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in open_search:
            try:
                speak("what you want to search on google")
                query = input("bot: what you want to search on google - ")
                chrome_path = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s'
                if len(Find(query)) == 0:
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=%s" % query)
                else:
                    s = Find(query)[0]
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open(s)
            except Exception:
                print("bot: Sorry, Cannot search due to slow internet")
                speak("Sorry, cannot search due to slow internet")

        elif request in open_cmd:
            speak("write your cmd command here: ")
            command = input("bot: Write your cmd command here: ")
            os.system('cmd /c "{}"'.format(command))

        elif request in tell_age:
            c = []
            c = dob.split("/")
            YY = int(c[2])
            mm = int(c[1])
            dd = int(c[0])
            year = str(calculateAge(date(YY, mm, dd)))
            print("bot: your age is " + year + " years")
            speak("your age is " + year + " years")

        elif request in tell_name:
            print("hello,", user)
            speak("hello " + str(user))

        elif request in play_music:
            PATH = "Songs\\"
            folder=os.listdir(PATH) # To randomly play a song
            file=random.choice(folder)
            ext3=['.mp3']
            while file[-4:] not in ext3:
                file=random.choice(folder)
            else:
                os.startfile("Songs\\" + file)
                speak("Playing "+ file)
                print('bot: Playing : ' + file)

        elif request in write_file:
            try:
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    audio=r.listen(source)
                write = r.recognize_google(audio)
                with open('newfile.txt', "a") as f:
                    f.write(write)
                print("bot: Contents of file are:")
                speak("Contents of file are")
                written = open('newfile.txt', 'r').readlines()
                for i in written:
                    print(i)
                    speak(i)
            except Exception:
                print("Sorry, Something went wrong")
                speak("Sorry, Something went wrong")

        elif request in tell_joke:
            ran_joke = str(random.choice(joke))
            print("bot: {}".format(ran_joke))
            speak(ran_joke + " haha haha")

        elif request in tell_health:
            ran_health = str(random.choice(health))
            print("bot: {}".format(ran_health))
            speak(ran_health)
        
        elif request in tell_life:
            ran_life = str(random.choice(life))
            print("bot: {}".format(ran_life))
            speak(ran_life)

        elif request in private_list:
            private_chatbot()
        
        elif request in empty_rec:
            try:
                print("bot: cleaning the Recyclebin")
                speak("cleaning the Recycle bin")
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

            except Exception:
                print("bot: Sorry, Something Went Wrong")
                speak("Sorry, Something Went Wrong")

        elif request == "" or request == " ":
            print("bot: you didn't wrote anything. write something please.")
            speak("you didn't wrote anything. write something please.")

        elif any(word in request for word in wh) or any(word in request for word in que):
            response = bot.get_response(request)
            if response.confidence < 1:
                print("bot: sorry, i don't know that. Do you know that?")
                speak("sorry, i don't know that. Do you know that?")
                user_response = input("you: ").lower()
                for i in bad_chars:
                    # using replace() to remove bad_chars
                    user_response = user_response.replace(i,'')
                if user_response == "yes":
                    print('bot: please input the correct one')
                    speak("please input the correct one")
                    correct_response = input("you: ").lower()
                    with open('files/learn_response.txt', "a") as f:
                        f.write(str(request) + '\n')
                        f.write(str(correct_response) + '\n')
                    learn = open('files/learn_response.txt', "r").readlines()
                    trainer.train(learn)
                    print('Response added to bot!')
                    speak("Response added to bot!")
                else:
                    print("bot: Ok,No problem")
                    speak("Okay.. No problem")
            else:
                response = bot.get_response(request)
                print("bot: " + str(response))
                speak(response)
                with open(user, "a") as f:
                    f.write("bot: " + str(response) + '\n')
                with open("edit.txt", "a") as f:
                    f.write(request + '\n')

        else:
            response = bot.get_response(request)
            print("bot: " + str(response))
            speak(response)
            with open(user, "a") as f:
                f.write("bot: " + str(response) + '\n')
            with open("edit.txt", "a") as f:
                f.write(request + '\n')

def private_chatbot():
    print("welcome, You are in the private mode now - No user data will be saved during chats")
    speak("welcome, You are in the private mode now - No user data will be saved during chats")
    while True:
        request = input("you: ").lower()
        for i in bad_chars:
            request = request.replace(i, '')  # using replace() to remove bad_chars

        if request in open_camera:
            try:
                print("Opening Camera...")
                speak("Opening Camera...")
                os.system('cmd /c "start microsoft.windows.camera:"')  # to open camera
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in open_calender:
            try:            
                print("Opening Calender...")
                speak("Opening Calender...")
                os.system('cmd /c "start outlookcal:"')  # to open calender
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        
        elif request in open_cortana:
            try:
                print("Opening Cortana...")
                speak("Opening Cortana...")
                os.system('cmd /c "start ms-cortana:"')  # to open cortana
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_mail:
            try:
                print("Opening Mail...")
                speak("Opening Mail...")
                os.system('cmd /c "start outlookmail:"')  # to open outlook mail
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_maps:
            try:
                print("Opening Maps...")
                speak("Opening Maps...")
                os.system('cmd /c "start ms-drive-to:"')  # to open maps
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_edge:
            try:
                print("Opening Microsoft Edge...")
                speak("Opening Microsoft Edge...")
                os.system('cmd /c "start microsoft-edge:"')  # to open microsoft-edge
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_paint:
            try:
                print("Opening Paint3D...")
                speak("Opening Paint3D...")
                os.system('cmd /c "start ms-paint:"')  # to open paint 3d
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in open_photos:
            try:
                print("Opening Photos...")
                speak("Opening Photos...")
                os.system('cmd /c "start ms-photos:"')  # to open photos
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in open_settings:
            try:
                print("Opening Settings...")
                speak("Opening Settings...")
                os.system('cmd /c "start ms-settings:"')  # to open settings
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_security:
            try:
                print("Opening Windows Defender...")
                speak("Opening Windows Defender...")
                os.system('cmd /c "start windowsdefender:"')  # to open windows defender
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_store:
            try:
                print("Opening Microsoft Store...")
                speak("Opening Microsoft Store...")
                os.system('cmd /c "start ms-store:"')  # to open microsoft store
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_chrome:
            try:
                print("Opening Chrome...") 
                speak("Opening Chrome...") 
                os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') # to open google chrome
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
            
        elif request in open_time:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("bot: The Current Time is ", current_time)
            speak("The Current Time is " + current_time)

        elif request in open_date:
            today = date.today()
            d = today.strftime("%d/%m/%Y")  # dd/mm/YY
            print("bot: Today's date is ", d)
            speak("Today's date is " + d)
        
        elif request in open_day:
            my_date = date.today()
            day = calendar.day_name[my_date.weekday()]
            print("bot: Today's day is ", day)
            speak("Today's day is " + day)
        
        elif request in search_wiki:
            speak("what you want to search")
            wiki = str(input("bot: what you want to search?: "))
            wiki = wiki.replace("wikipedia", "")
            results = wikipedia.summary(wiki, sentences=3)
            print("According to Wikipedia..." + results)
            speak("According to Wikipedia..." + results)

        elif request in shutup:
            try:
                if request == shutup[0]:
                    os.system('cmd /c "shutdown /s"')
                    speak("shutdowning in 1 minute")
                if request == shutup[1]:
                    speak("restarting in 1 minute")
                    os.system('cmd /c "shutdown /r"')
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in battery_per:
            try:
                battery = psutil.sensors_battery()
                plug = battery.power_plugged
                percent = str(battery.percent)
                if plug==False:
                    plug="Not Plugged In"
                else:
                    plug="Plugged In"

                print("bot: "+ percent +'% || ' + plug)
                speak(percent + "%" + "and" + plug)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in roll_dice:
            min=1
            max=6
            print("bot: Rolling the dice...")
            speak("Rolling the dice..")
            dice=str(random.randint(min, max))
            print("bot: You got.. " + dice)
            speak("You got.. " + dice)

        elif request in pick_card:
            card_number =['Ace','King','Queen','Jack','two','three','four','five','six','seven','eight','nine','ten']
            card_symbol =['Heart','club','Diamond','Spade']
            ran_num = random.choice(card_number)
            ran_sym = random.choice(card_symbol)
            print("bot: It's {} of {}".format(random_num,random_sym))
            speak("Its's" + random_num + "of" + random_sym)

        elif request in random_num:
            speak("Enter minimum number")
            min = int(input("bot: Enter minimum number"))
            speak("Enter maximum number")
            max = int(input("bot: Enter maximum number"))
            num = str(random.randint(min, max))
            speak("Giving a random number...")
            print("bot: It's " + num)
            speak("It's" + num)

        elif request in toss_coin:
            coin=["Heads","Tails"]
            ran_coin = str(random.choice(coin))
            print("tossing a coin for you")
            speak("tossing a coin for you...")
            print("bot: It's" + ran_coin)
            speak("It's" + ran_coin)

        elif request in wifi:
            try:
                if request == wifi[0]:
                    speak("enabling wifi")
                    commands = 'netsh interface set interface Wi-Fi enabled'
                    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ commands)
                elif request == wifi[1]:
                    speak("disabling wifi")
                    commands = 'netsh interface set interface Wi-Fi disabled'
                    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ commands)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
    
        elif request in weather:
            try:
                speak("Enter city name")
                n=input("bot: Enter City Name: ")
                get_weather(n)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in vol:
            try:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                if request == vol[0] or vol[2]:
                    print("bot: Increasing Volume")
                    volume.SetMasterVolumeLevel(-0.0, None) #100 volume
                elif request == vol[1] or vol[3]:
                    print("bot: Decreasing Volume")
                    volume.SetMasterVolumeLevel(-65.0, None) #0 volume
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")
        
        elif request in bright:
            try:
                speak("How much you want to set the brightness")
                bit=int(input("bot: How much you want to set the brightness: "))
                brightness = bit # percentage [0-100]
                c = wmi.WMI(namespace='wmi') #full form
                methods = c.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(brightness, 0)
            except Exception:
                print("bot: Sorry, something went wrong")
                speak("Sorry, something went wrong")

        elif request in open_search:
            try:
                speak("what you want to search on google")
                query = input("bot: what you want to search on google - ")
                chrome_path = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s'
                if len(Find(query)) == 0:
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=%s" % query)
                else:
                    s = Find(query)[0]
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open(s)
            except Exception:
                print("bot: Sorry, Cannot search due to slow internet")
                speak("Sorry, cannot search due to slow internet")

        elif request in open_cmd:
            speak("write your cmd command here: ")
            command = input("bot: Write your cmd command here: ")
            os.system('cmd /c "{}"'.format(command))

        elif request in tell_age:
            print("bot: I can't tell your age as i don't know you")
            speak("bot: I can't tell your age as i don't know you")

        elif request in tell_name:
            print("bot: I can't tell your name as i don't know you")
            speak("bot: I can't tell your name as i don't know you")

        elif request in play_music:
            PATH = "Songs\\"
            folder=os.listdir(PATH) # To randomly play a song
            file=random.choice(folder)
            ext3=['.mp3']
            while file[-4:] not in ext3:
                file=random.choice(folder)
            else:
                os.startfile("Songs\\" + file)
                speak("Playing "+ file)
                print('bot: Playing : ' + file)

        elif request in write_file:
            try:
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    audio=r.listen(source)
                write = r.recognize_google(audio)
                with open('newfile.txt', "a") as f:
                    f.write(write)
                print("bot: Contents of file are:")
                speak("Contents of file are")
                written = open('newfile.txt', 'r').readlines()
                for i in written:
                    print(i)
                    speak(i)
            except Exception:
                print("Sorry, Something went wrong")
                speak("Sorry, Something went wrong")

        elif request in tell_joke:
            ran_joke = str(random.choice(joke))
            print("bot: {}".format(ran_joke))
            speak(ran_joke + " haha haha")

        elif request in tell_health:
            ran_health = str(random.choice(health))
            print("bot: {}".format(ran_health))
            speak(ran_health)
        
        elif request in tell_life:
            ran_life = str(random.choice(life))
            print("bot: {}".format(ran_life))
            speak(ran_life)

        elif request in private_list:
            private_chatbot()
        
        elif request in empty_rec:
            try:
                print("bot: cleaning the Recyclebin")
                speak("cleaning the Recycle bin")
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

            except Exception:
                print("bot: Sorry, Something Went Wrong")
                speak("Sorry, Something Went Wrong")

        elif request == "" or request == " ":
            print("bot: you didn't wrote anything. write something please.")
            speak("you didn't wrote anything. write something please.")

        elif any(word in request for word in wh) or any(word in request for word in que):
            response = bot.get_response(request)
            if response.confidence < 1:
                print("bot: sorry, i don't know that. Do you know that?")
                speak("sorry, i don't know that. Do you know that?")
                user_response = input("you: ").lower()
                for i in bad_chars:
                    # using replace() to remove bad_chars
                    user_response = user_response.replace(i,'')
                if user_response == "yes":
                    print('bot: please input the correct one')
                    speak("please input the correct one")
                    correct_response = input("you: ").lower()
                    with open('files/learn_response.txt', "a") as f:
                        f.write(str(request) + '\n')
                        f.write(str(correct_response) + '\n')
                    learn = open('files/learn_response.txt', "r").readlines()
                    trainer.train(learn)
                    print('Response added to bot!')
                    speak("Response added to bot!")
                else:
                    print("bot: Ok,No problem")
                    speak("Okay.. No problem")
            else:
                response = bot.get_response(request)
                print("bot: " + str(response))
                speak(response)

        else:
            response = bot.get_response(request)
            print("bot: " + str(response))
            speak(response)


you = input("bot: Want to turn on incognito mode? [Press Yes or y] or else Continue to chatbot?: ").lower()
for i in bad_chars:
    you = you.replace(i, '')  # using replace() to remove bad_chars

try:
    if (you == 'yes') or (you == 'y'):
        private_chatbot()
    else:
        print("Bot: Welcome...")
        user = input("Write your name: ")
        dob=input("Enter your date of birth (dd/mm/YY): ")

        if os.path.isfile(user) == True: # to read previous chats for register user
            f = open(user, "r")
            for i in f:
                print(i,end="")
            f.close()
            print("bot: Welcome back, {}".format(user))
            speak("Welcome back.." + user)
            chatbot()
        else:
            speak("hello," + user)
            print("welcome," + user)
            chatbot()

except Exception:
    print("An error occured")


# ----------------------------------------------------------------------------------

# private chat
# open Apps -- System
# time
# date
# day
# random number
# random card
# heads or tails
# roll a dice
# turn on/off wifi
# jokes
# health tips
# life hacks
# screen brightness
# screen volume
# battery %  & plug state 
# shutdown & restart
# empty recycle bin
# show previous user chat
# play a song
# google search -- both url and word
# wikipedia search
# learn user input
# user age & name 
# auto write in a file
# weather
