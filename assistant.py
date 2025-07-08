import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import pyjokes
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:  # Use device_index=0 or 1 based on your mic
            r.adjust_for_ambient_noise(source, duration=1)
            speak("I'm listening...")
            audio = r.listen(source, timeout=6, phrase_time_limit=6)
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except sr.WaitTimeoutError:
        speak("You were silent. Try again.")
    except sr.UnknownValueError:
        speak("Sorry, I didn’t understand that.")
    except sr.RequestError:
        speak("Speech service is not responding.")
    return ""

def run_assistant():
    command = take_command()
    if not command:
        return

    if 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time}")

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A, %d %B %Y')
        speak(f"Today is {date}")

    elif 'who is' in command or 'what is' in command:
        topic = command.replace('who is', '').replace('what is', '')
        info = wikipedia.summary(topic, sentences=1)
        speak(info)

    elif 'search for' in command:
        search_query = command.replace('search for', '')
        speak(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif 'open instagram' in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif 'open gmail' in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'weather' in command:
        city = command.replace('weather', '')
        speak(f"Showing weather for {city}")
        webbrowser.open(f"https://www.google.com/search?q=weather+{city.strip()}")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif 'stop' in command or 'shutdown' in command or 'exit' in command:
        speak("Shutting down. Goodbye!")
        exit()

    else:
        speak("Sorry, I didn’t get that. Try another command.")

# Start assistant
speak("Hello! I am your personal assistant.")
while True:
    run_assistant()
