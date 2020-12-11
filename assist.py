import pyttsx3
import datetime
import speech_recognition as sr
import time
import pyjokes
import subprocess
import json
import requests
import os
import wikipedia
import webbrowser
import cv2
import wolframalpha
import winshell

engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def TakeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)
        try:
            print("Recognizing....")
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said: {statement}")
            speak(f"user said: {statement}")
        except Exception as e:
            print(e)
            speak("Pardon me, Speak again")
            return "None"
        return statement

def WishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !") 

	else:
		speak("Good Evening Sir !") 

	assname =("candy")
	speak("I am your Assistant")
	speak(assname)

def weather():
    api_key="d6f58ca327384c4ccb77f6b0c74ca0a4"
    base_url="https://api.openweathermap.org/data/2.5/weather?" # base_url variable to store url
    speak("whats the city name")
    city_name=TakeCommand()
    complete_url=base_url+"appid="+api_key+"&q="+city_name  #complete_url variable to store complete url address
    response = requests.get(complete_url)    #The response recorded are converted to json file 
    x=response.json()  #here data is converted to dict format
    if x["cod"]!="404":  #it checks whether city is found or not
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in kelvin unit is " +
                str(current_temperature) +
                "\n humidity in percentage is " +
                str(current_humidiy) +
                "\n description  " +
                str(weather_description))
        print(" Temperature in kelvin unit = " +
                str(current_temperature) +
                "\n humidity (in percentage) = " +
                str(current_humidiy) +
                "\n description = " +
                str(weather_description))

def click_img():
    video = cv2.VideoCapture(0)
    check,frame = video.read()
    cv2.imshow('capture',frame)
    cv2.imwrite('capture.png',frame)
    cv2.waitKey(0)
    video.release()
    cv2.destroyAllWindows()

def news():
    url = ('http://newsapi.org/v2/everything?q=apple&from=2020-12-08&to=2020-12-08&sortBy=popularity&apiKey=c5035009c68b4686899f43b2a1cd3ef1')
    i=3
    try: 
        response = requests.get(url) 
    except: 
        engine.say("can, t access link, plz check you internet ") 
    news = json.loads(response.text) 
    for new in news['articles']:
        i+=1
        if i==3:
            break
        else:
            print("##############################################################\n") 
            print(str(new['title']), "\n") 
            speak(str(new['title'])) 
            print('______________________________________________________\n') 
            print(str(new['description']), "\n") 
            speak(str(new['description']))  
            print("..............................................................") 
            time.sleep(2)

def quiet():
    speak("Your personal assistant is shutting down")
    print("Your personal assistant is shutting down")
    time.sleep()

def start():
    clear = lambda: os.system('cls')
    speak("Loading your assistant")
    print("Loading your assistant")
    WishMe()

    while True:
        speak("Tell Me, How can I help you?")
        print("Tell Me, How can I help you?")
        statement=TakeCommand().lower()
        
        if statement==0 or statement=='':
            continue

        if "bye" in statement or "stop" in statement:
            quiet()
            break
            
        if 'youtube' in statement:
            webbrowser.open("youtube.com")
            speak("here is your YouTube")

        elif 'google' in statement:
            webbrowser.open("google.com")
            speak("here is your Google")
        
        elif 'time' in statement:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif 'date' in statement:
            strTime =  datetime.datetime.now().strftime('%Y-%m-%d')
            speak(f"the date is {strTime}")

        # masti with assistant

        elif 'how are you' in statement:
            speak("I am good sir, tell me about you")
            if 'fine' in statement or 'good' in statement:
                speak("its good to know that")
        
        elif 'made you' in statement or 'created you' in statement or 'is your invertor' in statement:
            speak("I have been created by Kritika")

        elif 'joke' in statement:
            speak(pyjokes.get_joke())

        elif 'reason of your existence' in statement or 'why are you created' in statement or 'why you came to world' in statement:
            speak("I have been created as an minor project by Kritika")


        elif "weather" in statement:
            weather()

        elif 'search' in statement or 'play' in statement:
            statement = statement.replace("search","")
            statement = statement.replace("play", "")
            webbrowser.open(statement)
            time.sleep(10)
        
        elif "camera" in statement or "take a photo" in statement:
            click_img()

        elif 'news' in statement:
            news()

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=TakeCommand()
            app_id="GGAAPU-P7HPQJT5Y2"
            client = wolframalpha.Client('GGAAPU-P7HPQJT5Y2')
            res = client.query(question)
            print(type(res))
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "calculate" in statement:   
            app_id = "GGAAPU-P7HPQJT5Y2"
            client = wolframalpha.Client(app_id)
            indx = statement.lower().split().index('calculate') 
            statement = statement.split()[indx + 1:] 
            res = client.query(' '.join(statement)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer)

        elif "restart" in statement:
            speak("Restarting")
            subprocess.call(['shutdown','/r'])

        elif "hibernate" in statement or 'sleep' in statement:			
            speak("Hibernating")
            subprocess.call(['shutdown','/h'])

        elif 'log off' in statement or 'signout' in statement:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'shutdown system' in statement:
                speak("Hold on! The pc is shutting down")
                subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in statement:
            winshell.recycle_bin().empty(empty(confirm=True, show_progress=True, sound=True))	
            speak("Recycle bin recycled")

        elif "don't listen" in statement or "stop listening" in statement:
            speak("for how much time you don't want to listen me")
            a=int(TakeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in statement or 'locate' in statement:
            statement=statement.replace("where is","")
            location=statement
            speak("user asked to locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/"+location+"")

        else:
            speak("opening")
            webbrowser.open(statement)
            time.sleep(5)