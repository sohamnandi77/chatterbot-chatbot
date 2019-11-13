from chatterbot import ChatBot  # import the chatbot
from chatterbot.trainers import ListTrainer  # method to train chatbot
from googlesearch import *
import webbrowser
from string import *
from datetime import *
from train import start_trainer
import calendar
import os
import os.path
import re
import random

# import logging
# logging.basicConfig(level=logging.INFO)

open_time = ['what is the time right now', 'time ', 'clock', 'what is the current time', 'what is the time now', 'what’s the time',
             'time', 'what time is it', 'what time is it now', 'do you know what time it is', 'could you tell me the time, please', 'what is the time',
             'will you tell me the time', 'tell me the time', 'time please', 'what is time',
             'what is the time', 'tell me time', 'time', 'clock', 'display watch']
open_date = ["what is today's date", "today date", "date"]
open_day = ["what is today's day", "day"]
open_camera = ['open camera', 'please open the camera',
               'show me the camera', 'camera']
open_calender = ['open calender', 'please open the calender',
                 'show me the calender', 'calender']
open_cortana = ['open cortana', 'please open the cortana',
                'show me the cortana', 'cortana', 'hey cortana']
open_mail = ['open mail', 'please open the mail',
             'show me the mail', 'mail', 'open my mails', 'open my mail']
open_maps = ['open maps', 'please open the maps',
             'show me the maps', 'maps', 'show me maps']
open_edge = ['open edge', 'please open the edge', 'show me the edge', 'edge', 'open microsoft edge',
             'please open microsoft edge', 'microsoft edge', 'show me microsoft edge', 'show me microsoftedge', 'open microsoftedge',
             'microsoftedge']
open_paint = ['open paint', 'please open the paint', 'show me the paint', 'paint', 'open paint 3d', 'show me paint 3d',
              'show me paint', 'show me paint 3d', 'paint3d', 'open paint 3d', 'open paint3d']
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
open_firefox = ['open firefox', 'please open the firefox',
                'show me the firefox', 'firefox']
open_search = ['do a google search', 'google search',
               'search on google', 'search me this']
tell_age = ['what is my age', 'how old i am', 'my age']
tell_name = ['what is my name', 'my name']
open_cmd = ['run cmd', 'can you run cmd commands']
tell_joke = ['tell me a joke', 'tell joke']
joke = [line.rstrip('\n') for line in open('jokes.txt')]
bad_chars = [";", ":", "!", "@", "#", "$", "%", "^", "&", "(", ")", "?",",", ".", "~", "`", "[", "]", "{", "}", "-", "_"] # initializing bad_chars_list

bot = ChatBot(
    'Example Bot', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        }])

trainer = ListTrainer(bot)  # set the trainer

def signup():
    dob = input("Enter your date of birth in (YY/mm/dd): ")
    
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
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def chatbot():
    while True:
        request = input("you: ").lower()
        for i in bad_chars:
            request = request.replace(i, '')  # using replace() to remove bad_chars
        request_que = request.split(" ")
        with open(user, "a") as f:
            f.write("bot: " + request + '\n')
        with open("edit.txt", "a") as f:
            f.write(request + '\n')
        if request in open_camera:
            print("Opening Camera...")
            os.system('cmd /c "start microsoft.windows.camera:"')  # to open camera
        elif request in open_calender:
            print("Opening Calender...")
            os.system('cmd /c "start outlookcal:"')  # to open calender
        elif request in open_cortana:
            print("Opening Cortana...")
            os.system('cmd /c "start ms-cortana:"')  # to open cortana
        elif request in open_mail:
            print("Opening Mail...")
            os.system('cmd /c "start outlookmail:"')  # to open outlook mail
        elif request in open_maps:
            print("Opening Maps...")
            os.system('cmd /c "start ms-drive-to:"')  # to open maps
        elif request in open_edge:
            print("Opening Microsoft Edge...")
            os.system('cmd /c "start microsoft-edge:"')  # to open microsoft-edge
        elif request in open_paint:
            print("Opening Paint3D...")
            os.system('cmd /c "start ms-paint:"')  # to open paint 3d
        elif request in open_photos:
            print("Opening Photos...")
            os.system('cmd /c "start ms-photos:"')  # to open photos
        elif request in open_settings:
            print("Opening Settings...")
            os.system('cmd /c "start ms-settings:"')  # to open settings
        elif request in open_security:
            print("Opening Windows Defender...") # to open windows defender
            os.system('cmd /c "start windowsdefender:"')
        elif request in open_store:
            print("Opening Microsoft Store...")
            os.system('cmd /c "start ms-store:"')  # to open microsoft store
        elif request in open_chrome:
            print("Opening Chrome...") # to open google chrome
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        elif request in open_firefox:
            print("Opening firefox...") # to open firefox (use \\ for files in user's folder)
            os.startfile('C:\\Users\\soham\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
        elif request in open_time:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("bot: The Current Time is ", current_time)
        elif request in open_date:
            today = date.today()
            d = today.strftime("%d/%m/%Y")  # dd/mm/YY
            print("bot: Today's date is ", d)
        elif request in open_day:
            my_date = date.today()
            day = calendar.day_name[my_date.weekday()]
            print("bot: today's day is ", day)
        elif request in open_search:
            try:
                query = input("bot: what you want to search on google - ")
                chrome_path = r'C:\\Users\\soham\\AppData\\Local\\Mozilla Firefox\\firefox.exe %s'
                if len(Find(query)) == 0:
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=%s" % query)
                else:
                    s = Find(query)[0]
                    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                        webbrowser.open(s)
            except Exception:
                print("bot: sorry due to low connectivity issues")

        elif request in tell_age:
            c = []
            c = dob.split("/")
            YY = int(c[0])
            mm = int(c[1])
            dd = int(c[2])
            print("bot: your age is", calculateAge(date(YY, mm, dd)), "years")
        elif request in tell_name:
            print("hello,", user)

        elif request in open_cmd:
            command = input("write your cmd command here: ")
            os.system('cmd /c "{}"'.format(command))

        elif request in tell_joke:
            print("bot: {}".format((random.choice(joke))))
       
        elif request == "":
            print("bot: you didn't wrote anything. write something please.")

        else:
            response = bot.get_response(request)
            print("bot: " + str(response))
            with open(user, "a") as f:
                f.write("bot: " + str(response) + '\n')
            with open("edit.txt", "a") as f:
                f.write(request + '\n')


                

user = input("write your name: ")
if os.path.isfile(user) == True:
    f = open(user, "r")
    for i in f:
        print(i,end="")
    f.close()
    print("bot: Welcome back {}".format(user))
    chatbot()
else:
    signup()
    chatbot()

# os.rename('user.txt','hello.txt')
# unit conversion - pint
# weather api
# file search
# .exe file
# seurity issues
# flask -- html+css+flask
#      -- dark mode
#      -- private mode
#      -- emoji
# tkinter -- input voice button (google recoginition)
#        -- private mode
#        -- improve GUI
