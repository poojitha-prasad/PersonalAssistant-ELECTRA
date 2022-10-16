from flask import Flask,render_template,request,url_for

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import requests
import time
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def submit():
    if request.method =="POST":
        def talk(text):
            engine.say(text)
            engine.runAndWait()
            if engine._inLoop:
                engine.endLoop()

        def weather():
            api_key = "3c4cb362ae6675a190df76a2274d6d1d"
            final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
            result = requests.get(final_URL)
            data = result.json()
            temperature = ((data['main']['temp']) - 273.15)
            temperature = round(temperature)
            description = data['weather'][0]['description']
            print("Current weather description: " + description)
            print("Current temperature: " + str(temperature) + " degree celsius")
            talk("Current weather description: " + description + "   Current temperature: " + str(temperature) + " degree celsius")

        def run_electra():

            print(command)

            if 'hai' in command or 'hello' in command:

                talk('hai ,how can i help you')

            elif 'how are you' in command:
                talk('I am fine,Thank you')

            elif 'good morning' in command:
                talk(command + '  have a great day')

            elif 'good night' in command:
                talk(command + '  sweet dreams')

            elif 'good evening' in command or 'good afternoon' in command:
                talk('Thanks You too')

            elif 'good bye' in command:
                talk('have a good day , see you later')

            elif 'time' in command:
                times = datetime.datetime.now().strftime('%I:%M %p')
                print("Current time is " + times)
                talk("Current time is " + times)
            elif 'date' in command:
                date = datetime.datetime.now().strftime('%D')
                print("Current date is " + date)
                talk("Current date is " + date)

            elif 'weather' in command:
                talk("Enter Your city: ")





            elif 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)


            elif 'open youtube' in command:
                webbrowser.open_new_tab("https://www.youtube.com")
                talk('Youtube is open now')
                time.sleep(5)
            elif 'open google' in command:
                webbrowser.open_new_tab("https://www.google.com")
                talk('Google is open now')
                time.sleep(5)
            elif 'open gmail' in command:
                webbrowser.open_new_tab("gmail.com")
                talk('Google mail is open now')
                time.sleep(5)

            elif 'search' in command:
                s_result = command.replace('search', '')
                s_info = webbrowser.open_new_tab(s_result)
                talk(s_info)

            elif 'wikipedia' in command or 'who' in command or 'what' in command:
                talk('Searching wikipedia...')
                result = command.replace('wikipedia', '')
                info = wikipedia.summary(result, 1)
                talk('According to wikipedia')
                print(info)
                talk(info)


            else:
                talk('Please say the command again.')



        while True:
            if engine._inLoop:
                engine.endLoop()
            try:


                if 'microphone' in request.form:
                    with sr.Microphone() as source:
                        print('listening...')
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        command = command.lower()
                        if 'electra' in command:
                            command = command.replace('electra', '')
                        run_electra()
                        break
                elif 'keyboard' in request.form :
                    type = request.form['type']
                    command = type.lower()
                    run_electra()
                    break

                elif 'citye' in request.form :
                    city = request.form['typec']
                    weather()
                    break

                elif 'citys' in request.form :
                    with sr.Microphone() as source:
                        voice = listener.listen(source)
                        city = listener.recognize_google(voice)
                        city = city.lower()
                        if 'electra' in city:
                            city = city.replace('electra', '')
                        weather()
                        break


                else:
                    talk('Please select a source.')

            except:
                pass






    else:
        return render_template('htm.html')

    if engine._inLoop:
        engine.endLoop()



if __name__ =='__main__':
    app.run(debug=True)
