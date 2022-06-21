from numpy import take
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# engine.say('I love potatoes')
engine.runAndWait()

my_mic = sr.Microphone(device_index=1)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with my_mic as source:
            print("Listening to you...")
            #listens to voice from source which is computer microphone
            voice = listener.listen(source)
            #command connects what we said on voice to google search
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'fantasia' in command:
                command = command.replace("fantasia", "")
                print(command)
            # else:
            #     print(command)
            
    except:
        print("Something fuckey wuckey is going on")
    return command

def run():
    command = take_command()
    print(command)
    #plays youtube videos
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        #setting how clock will look, 12 hour clock, minutes, p = am/pm
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
        print(time)
    # info look up (person)
    elif 'who is' in command:
        person = command.replace('who is', '')
        #number is amount of sentences
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info) 
    elif 'what is' in command:
        thing = command.replace('what is', '')
        #number is amount of sentences
        try:
            info = wikipedia.summary(thing, 3)
            print(info)
            talk(info) 
        # if ambiguous error, take the first option
        except wikipedia.DisambiguationError as e:
            s = e.options[0]
            p = wikipedia.summary(s, 3)
            print(p)
            talk(p)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        quit
    else:
        talk('Please say the command again')

#to keep running multiple statements
# while True:           
run()