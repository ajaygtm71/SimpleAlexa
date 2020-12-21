import os, random, webbrowser
import pyttsx3, speech_recognition as sr, pywhatkit, datetime, wikipedia, pyjokes, smtplib


listener = sr.Recognizer()
listener.pause_threshold=1
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning!")

    elif 12 <= hour < 17:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("I am Alexa. Please tell me how I may help you!")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def take_command():
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
        try:
            print("Recognizing...")
            query = listener.recognize_google(voice,language='en-in')
            query = query.lower()
            if 'alexa' in query:
                query = query.replace('alexa', '')
        except Exception as e:
            print("Please repeat...")
            return "none"
        return query


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a boyfriend')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        _joke = pyjokes.get_joke()
        print(_joke)
        talk(_joke)
    elif 'gmail' in command:
        try:
            talk("What should I say?")
            content = take_command()
            to = "yourEmail@gmail.com"
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            talk("Sorry, I am not able to send this email")
    elif 'open music' in command:
        music_dir = 'D:\\Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))
    elif 'open google' in command:
        webbrowser.open("google.com")
    else:
        talk('Please say the command again.')


if __name__ == '__main__':
    wishMe()
    while True:
        run_alexa()

