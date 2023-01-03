import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.say("hello sir what can i do for you")
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)
    except:
        pass
    return command


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
    elif 'who'in command:
        person = command.replace('whoa', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date'in command:
        talk('No i am not interested')
    elif 'are you single'in command:
        talk('YES sir i am single just like you')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'saurabh' in command:
        talk('Hey Saurabh!, Please drink one more pag')
    else:
        talk('Please say the command again.')
while True:
   run_alexa()
   