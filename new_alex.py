import pyttsx3 as pt
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import random
import os
import geocoder
import cv2
# this part is to define the voices and its properties

engine = pt.init('sapi5')
voices = engine.getProperty('voices')       # get voices extract the voices
engine.setProperty('voice',voices[1].id)    # set voice or choose voice male or female
print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hours = int(datetime.datetime.now().hour)
    speak('hey There!')
def capture():

    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('I\'M LISTENING...')
        rec.non_speaking_duration = 0.5
        audio = rec.listen(source, phrase_time_limit=3)
    try:
        print('hey')
        a = rec.recognize_google(audio, language='en-in')
        print(a)
        return a
    except Exception as e:
        speak('Sorry, I could not understand what you said.')
def system(query):
    print('im in current')
    if 'current directory' in query:
        audio = os.getcwd()
        speak(audio)
        print(audio)
    if 'list of directory' in query:
        audio = os.listdir()
        print(audio)
        speak(audio)
    if 'create a directory' in query:
        speak('enter the directory name')
        name = input()
        parent = os.getcwd()
        audio = os.path.join(parent,name)
        os.makedirs(audio)
        print(audio)
        speak(audio)
        os.system('chrome')
        speak('directory created successfully')
    if 'remove directory' in query or 'delete this directory' in query:
        speak('enter the directory name that you want to remove')
        name=input()
        parent = os.getcwd()
        audio = os.path.join(parent, name)
        os.rmdir(audio)
        audio = os.getcwd()
        print(audio)
        speak(audio)
        speak('directory removed successfuly')
def arthmetic(query):
    print('im in arthmatic')
    b = query.split()
    c = []
    for i in b:
        if i.isdigit():
            c.append(int(i))
    if 'add' in query or 'plus' in query or '+' in query:
        print('im in cond')
        audio=sum(c)
        speak(audio)
        print(audio)
    if 'minus' in query or 'subtract' or '-' in query:
        sub = c[0]
        for i in range(1,len(c)):
            sub=sub-c[i]
        audio=sub
        speak(audio)
def location():
    g = geocoder.ip('me')
    audio = g.latlng
    print(audio)
    speak(audio)

def introduce(query):
    print('im in introduce funx')
    try:
        if 'about your boss' in query or 'who is your developer' in query:
            audio='shaik is my developer and boss, he is extremely talented and very good looking and still single maybe i am only one who about him i love him more than anyone in this world'
            speak(audio)
            print(audio)
        elif 'introduce' in query or 'introduction' in query or 'yourself' in query or 'your name' in query or 'made you' in query or 'created you' in query or 'who are you' in query:
            audio='this is a bot which is made by unemployed graduate from green hills engineering college '
            speak(audio)
        elif 'abhishek' in query or 'Veer' in query:
            audio='are you talking about veer yes he is an gandu and ass hole chutiya'
            speak(audio)
        elif 'your boss' in query or 'introduce your boss' in query:
            audio='you are talking about shaik right?'
            speak(audio)
        elif 'operations you can perform' in query:
            audio='i am bot i can control your setting and made your work easier and fast, i can search anything on google and give you best result in an instance time, i can open folders'
            speak(audio)
            print(audio)

    except:
        speak('i cant hear you')
def room(query):
    if 'saif khan room' in query:
        speak('saif khan  from uttar pradesh 420')
        return
    elif 'sachin room' in query:
        speak('room 420')
        return

    elif 'pandit room' in query:
        speak('room 410')
        return
    elif 'khana khane ka time' in query:
        audio = 'breakfast at 10 o clock'
        audio1 = 'lunch at 2 o clock'
        audio2 = 'dinner at 9 o clock'
        print(audio)
        print(audio1)
        print(audio2)
        speak(audio)
        speak(audio1)
        speak(audio2)


def time(query):
    audio = datetime.datetime.now()
    audio = str(audio)
    n=len(audio)
    print(audio[11:n-7])
def face(query):
    speak('click "q" for quitting from the webcam')
    print('click "q" for quitting from the webcam')
    vid = cv2.VideoCapture(0)

    while (True):
        ret, cam = vid.read()
        cv2.imshow('frame', cam)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()

def greeting():
    b = int(datetime.datetime.now().hour)

    if b >= 0 and b < 12:
        speak("Good Morning! ")

    elif b >= 12 and b < 17:
        speak("Good Afternoon! ")

    else:
        speak("Good evening! ")

def passw(query):
    a = query
    if "can you generate a password" in a or "generate password" in a:
        speak("okay just wait for a second")
        x = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        y = ["0","1","2","3","4","5","6","7","8","9"]
        z = ["@", "#", "$", "%", "&", "*","+"]
        m = random.choices(x,k=4)
        n = random.choices(y,k=2)
        o = str(z[random.randint(0,6)])
        sum = ""
        num = ""
        for i in m:
            sum = sum+i
        for j in n:
            num = num+j
        m = sum+o+num
        print(m)
        speak("Password is "+m)


def funx(query):
    a = query

    if "youtube" in a:
        speak("opening youtube for you")
        webbrowser.open("www.youtube.com")

    if "linkedin" in a:
        speak("opening linkedin for you")
        webbrowser.open("www.linkedin.com")

    if "twitter" in a:
        speak("opening twiter for you")
        webbrowser.open("www.twitter.com")

    if "instagram" in a:
        speak("opening instagram for you")
        webbrowser.open("www.instagram.com")

    if "facebook" in a:
        speak("opening facebook for you")
        webbrowser.open("www.facebook.com")

    if "wikipedia" in a:
        a = a.replace("wikipedia", "")
        res = wikipedia.summary(a, sentences=3)
        speak("according to wikipedia")
        print(res)
        speak(res)
def ent(query):
    a=query
    if "game" in a:
        print("okay lets play a game there is only one rule, you have to speak only one word")
        speak("okay lets play a game there is only on rule ,you have to speak only one word")
        speak("choose between stone paper and scissor")
        b = capture().lower()
        options=["stone","paper","scissor"]
        comp=random.choice(options)

        user=b

        speak("computer chose"+ comp)

        if comp == "stone" and user == "paper":
            print("you   won")
            speak("you   won")

        elif comp == "stone" and user == "scissor":
            print("you  lose")

        elif comp == "paper" and user == "stone":
            print("you  lose")
            speak("you  lose")

        elif comp =="paper" and user == "scissor":
            print("you  win")
            speak("you  win")

        elif comp == "scissor" and user =="stone":
            print("you   won")
            speak("you   won")

        elif comp == "scissor" and user =="paper":
            print("you  lose")
            speak("you  lose")


        else:
            print("its  a  draw")
            speak("its  a  draw")


def co(query):
    if "flip a coin" or "toss" in query:
        speak("okay let me toss a coin for you")
        b = ["head","tails"]
        print(random.choice(b)+"it is")
        speak(random.choice(b)+"it is")

def bind(a):
    if a==1:
        introduce(query)
    if a==2:
        time(query)
    if a==3:
        arthmetic(query)
    if a==4:
        system(query)
    if a==5:
        location()
    if a==6:
        face(query)
    if a==7:
        room(query)
    if a==8:
        funx(query)
    if a == 9:
        co(query)
    if a==10:
        ent(query)
    if a == 11:
        passw(query)
if __name__=="__main__":
    greeting()
    wishme()
    a = capture()
    query = a.lower()
    print(query)
    c = {'saif khan room':7,'sachin room':7,'pandit room':7,'khana khane ka time':7,'open':8,'game':10,'generate password':11,'generate a password':11,'flip a coin':9,'toss':9}
    for key in c.keys():
        if key in query:
            bind(c[key])
            break
    a = {'introduce':1,'introduction':1 , 'yourself':1, 'your name':1,'made you':1,'created you':1,'who are you':1,'abhishek':1,'time':2,'your boss':1,'operations you can perform':1,'add':3,'plus':3,'minus':3,'subtract':3,'multiply':3,'into':3,'divide':3,'+':3,'-':3,'who is your developer':1}
    for key in a.keys():
        if key in query:
            bind(a[key])
            break
    b = {'current directory':4,'list of directory':4,'create a directory':4,'remove directory':4,'delete this directory':4,'my location':5,'open webcam':6}
    for key in b.keys():
        if key in query:
            bind(b[key])
            break
