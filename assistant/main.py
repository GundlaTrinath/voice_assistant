import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import subprocess as sp
import pyautogui as auto
import webbrowser
import os
import pyjokes
import datetime as dt
import wikipedia as wk
from playsound import playsound
import requests
from bs4 import BeautifulSoup
import sys
from tkinter import *

listener=sr.Recognizer()
engine=pt.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
tab=1
def talk(talk):
    print(talk)
    engine.say(talk)
    engine.runAndWait()


def get_infor():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice=listener.listen(source,10,10)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        get_assis()

def get_info():
    result=get_infor()
    if result=='':
        get_info()
    return result

def wishes():
    hr = dt.datetime.now().strftime('%I')
    pm = dt.datetime.now().strftime('%p')
    hr = int(hr)
    if (hr < 12 and hr > 6 and pm == 'AM'):
        morning()
    elif (hr < 4 and pm == 'PM'):
        talk('Hey hai, good afternoon, how today is going on')
        cmd = get_info()
        p1 = ['good', 'better', 'fine', 'ok']
        n1 = ['bad', 'waste', 'boring', 'nothing']
        for i in p1:
            if i in cmd:
                talk('ohh, that good, i\'m playing a song makes your day more better')
                talk('Shall i play songs for you')
                info=get_info()
                if "no" in info:
                    talk("Ahh!, not a problem")
                else:
                    pw.playonyt('morning songs')
        for i in n1:
            if i in cmd:
                talk('ohh, that really bad, wait iam playing situational song for you')
                pw.playonyt('sad song')
        for i,j in p1,n1:
            if i not in p1 and j not in n1:
                talk('sorry i didn\'t understand')

    elif (hr < 9 and pm == 'PM'):
        talk('Hello sir, good evening')
        time = dt.datetime.now().strftime('%I:%M %p')
        talk('it\'s ' + time)
    elif (hr < 12 and pm == 'PM'):
        talk('Good night sir')
        time = dt.datetime.now().strftime('%I:%M %p')
        talk('it\'s ' + time)
        pw.playonyt('lali lali song')
        talk("Here is some music to for your better sleep")
    else:
        talk('hello sir, how can I help you')
    get_assis()

def temp():
    url = f"https://www.google.com/search?q=weather+in+hyderabad&rlz=1C1CHBF_enIN916IN916&oq=weather+in+hyderabad&aqs=chrome..69i57.8440j0j15&sourceid=chrome&ie=UTF-8"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    update = soup.find("div", class_="BNeawe").text
    talk(f'The current temperature in outside is ' + str(update))

def news():
    talk('fetching latest news, Please wait sir')
    main_url='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=853fd288a3784eaabd484d95eb211011'
    main_page=requests.get(main_url).json()
    articles=main_page['articles']
    head=[]
    day=['first','second','third','fourth','fifth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        talk('today '+day[i]+' news is. :'+head[i])

def list(names):
    if(names=='sandeep'):
        number='9502235033'
    elif(names=='goutham'):
        number='7095028981'
    elif(names=='brother'):
        number='7095722924'
    elif(names=='vijay'):
        number='9390680326'
    else:
        talk('Sorry sir, name is not in the list. Tell me the number')
        number=get_info()
    return '+91'+number

def morning():
    talk('good morning sir')
    time = dt.datetime.now().strftime('%I:%M %p')
    talk('it\'s '+time)
    temp()
    talk('had your breakfast?')
    cmd=get_info()
    if 'yes' in cmd:
        talk('ohh, that\'s great, looking today is cool.')
    elif 'no' in cmd:
        talk('ohh, what happened, wait iam getting it.')
        webbrowser.open('https://www.zomato.com/hyderabad/delivery?dishv2_id=835ef6c0b2999746e9a5bdc11b3e528c_2')
        talk('you can order now')
    else:
        talk('sorry sir, i didn\'t understand. what ever')
    news()
    webbrowser.open('https://youtu.be/EmRwe-oY3VQ')
    talk('Here is some music for your brighter day')
def asking(ask):
    global task_cmpt,task_do
    ask = ask.replace('alexa', '')
    if('time' in ask):
        time=dt.datetime.now().strftime('%I:%M %p')
        talk('current time is '+time)
        # show.config(text=time)
    elif ('search' in ask):
        search = ask.replace('search', '')
        talk('searching ' + search)
        pw.search(search)
    elif ('play' in ask):
        song = ask.replace('play', '')
        talk('playing' + song)
        pw.playonyt(song)
    elif('date' in ask):
        date=dt.datetime.now()
        date=date.date()
        talk('today date is '+str(date))
        ans=str(date)
        #show.config(text=ans)
    elif('calculate' in ask):
        cal=ask.replace('calculate','')
        cal=cal.split()
        try:
            if '+' in cal:
                result=int(cal[0])+int(cal[2])
                talk('Got it sir,your result is ' + str(result))
                ans=cal+str(result)
                #show.config(text=ans)
            elif 'into' in cal:
                result=int(cal[0])*int(cal[2])
                talk('Got it sir,your result is ' + str(result))
                ans = cal + str(result)
                # show.config(text=ans)
            elif 'by' in cal:
                result=int(cal[0])/int(cal[2])
                talk('Got it sir,your result is ' + str(result))
                ans = cal + str(result)
                # show.config(text=ans)
            elif '-' in cal:
                result=int(cal[0])-int(cal[2])
                talk('Got it sir,your result is ' + str(result))
                ans = cal + str(result)
                # show.config(text=ans)
        except:
            talk('sorry sir,please say like 3 + 4 or 5 into 8.')
    elif("what can you do" in ask):
        talk("I can do many things like telling news, playing songs, calculating, message through what's app, searching information and many more")
    elif('good' in ask):
        wishes()
    elif('work' in ask):
        task=[]
        talk('i can help in that')
        talk('Is it internship?')
        info=get_info()
        if "no" in info:
            talk('what the work you have')
            work_info=get_info()
            talk('can i help with google search')
            cmd=get_info()
            if 'no' in cmd:
                talk('ohhkay, ')
        else:
            task_cmpt=task[0]
            task_do=task[1]
            talk('ohhh ok then, I can help you')
            talk('i think your have completed upto '+task_cmpt)
            talk('now your task is to '+task_do)
            talk('is it correct?')
            info=get_info()
            if 'no' in info:
                talk('upto where your task complete')
                cmd=get_info()
                task[0]=cmd
                talk('Then what should you do')
                cmd=get_info()
                task[1]=cmd
            talk('ok, we have lot of work oh, ohhh!')
            talk('here is some info, i search in the google about your task')
            pw.search(task_do)
    elif('are you single' in ask):
        talk('hello brother, Iam machine, if you want to mingle. Go where ever u want, just leave me.')
    elif('play next song' in ask):
        auto.keyDown('shift')
        auto.press('n')
        auto.keyUp('shift')
    elif('sing' in ask):
        talk('ok, I am checking my vocal. Hey start music. ')
        playsound('C:/Users/thrived/Music/Ariana Grande - 7 rings.mp3')
        talk('how is it, I think you get shocked.')
    elif('waste' or 'bad')in ask:
        talk('okay, it\'s my bad')
    elif('today is my birthday' in ask):
        talk('Greetings from Alexa. Happy birthday to you!')
        pw.playonyt('happy birthday song')
    elif('switch window' in ask):
        global tab
        auto.keyDown('alt')
        for i in range(tab):
            auto.press('tab')
        auto.keyUp('alt')
        talk('Switching next window')
        tab=tab+1
    elif('switch tab' in ask):
        auto.keyDown('ctrl')
        auto.press('tab')
        auto.keyUp('ctrl')
        talk('switching next tab')
    elif('new tab' in ask):
        auto.keyDown('ctrl')
        auto.press('t')
        auto.keyUp('ctrl')
        talk('switching next tab')
    elif('joke' in ask):
        global clarify
        clarify='yes'
        while('yes' in clarify):
            ans=pyjokes.get_joke()
            talk(ans)
            talk('how is it sir? do you want more')
            clarify=get_info()
        talk('ok sir, as your wish')
    elif('volume' in ask):
        ask=ask.replace('volume','')
        if 'increase' in ask:
            auto.press('volumeup')
            talk('your volume increases')
        elif 'decrease' in ask:
            auto.press('volumedown')
            talk('your volume decrease')
        elif('mute' in ask):
            auto.press('volumemute')
            talk('volume muted')
    elif('screenshot' in ask):
        pw.take_screenshot()
        talk('screenshot was taken')
    elif('close tab' in ask):
        talk('closing tab')
        pw.close_tab(2)
    elif('news' in ask):
        news()
    elif('message' in ask):
        talk('whom do you want to message')
        name=get_info()
        number=list(name)
        talk('What message do you want to send')
        message=get_info()
        talk('Ok sir, sending message to'+message)
        pw.sendwhatmsg_instantly(number,message)
    elif('age' in ask):
        talk("It is my personal thing. Don't ask again.")
    elif('open whatsapp' in ask):
        talk('Opening whats app')
        webbrowser.open('https://web.whatsapp.com/')
    elif('open calculator' in ask):
        talk('Opening calculator')
        sp.call('Calc.exe')
    elif('close calculator' in ask):
        talk('Closing calculator')
        os.system('TASKKILL /F /IM Calculator.exe')
    elif('open chrome' in ask):
        talk('Opening chrome')
        webbrowser.open('https://google.com/')
    elif('open youtube' in ask):
        talk('Opening youtube')
        webbrowser.open('https://www.youtube.com/')
    elif('temperature' in ask):
        command=ask.split()
        length=len(command)-1
        comm=command[length]
        url = f"https://www.google.com/search?q=weather+in+{comm}&rlz=1C1CHBF_enIN916IN916&oq=weather+in+{comm}&aqs=chrome..69i57.8440j0j15&sourceid=chrome&ie=UTF-8"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        update = soup.find("div", class_="BNeawe").text
        talk(f'The current weather in {comm} is '+str(update))
    elif ('who are you' in ask):
        talk('''Do you have any short temper, haha ha,
        hey, just kidding.
        Iam Alexa''')
    elif('thank' in ask):
        talk('it\'s OK sir, I\'m always being smart.')
    elif('great' in ask):
        talk('Uhh hmm!, It\'s your pleasure.')
    elif('age' in ask):
        talk("It is my personal thing. Don't ask again.")
    elif('how old you are' in ask):
        talk("I was created in 2021. so, I’m still fairly young. But, I’ve learned so much! I hope, I’m wise beyond my years.")
    elif('ok bye' in ask):
        talk('ok, bye sir, if u want any help call me again')
        sys.exit()
    elif('what' in ask):
        wiki = wk.summary(ask,2)
        talk('According to wikipedia, '+wiki)
    elif('who' in ask):
        wiki = wk.summary(ask,2)
        talk('According to wikipedia, '+wiki)


def get_assis():
    while(True):
        command=get_infor()
        if 'alexa' in command:
            asking(command)
        else:
            pass


# get_assis()

# importing whole module
# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
# import datetime as dt
#
#
# root = Tk()
# root.title('Alexa')
# root.geometry("1500x1000")
# root.configure(bg="white")
#
# def time():
#     string = strftime('%H:%M:%S %p')
#     lbl.config(text=string)
#     lbl.after(1000, time)
#
#
# lbl = Label(root, font=('calibri', 40, 'bold'),background='white',foreground='black')
#
#
# lbl.pack(anchor='center')
# time()
#
# date = dt.datetime.now()
# label = Label(root, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20",background='white')
# label.pack(pady=20)
#
# show = Label(root, font=('calibri', 40, 'bold'),background='white',foreground='black',text='')
# show.pack(anchor='center')
# # wishes()
# button=Button(root,command=wishes,text="Start")
# button.pack()
# def quit():
#     root.quit()
#
# exit=Button(root,command=quit,text="Exit")
# exit.pack()
# mainloop()
wishes()
get_assis()
