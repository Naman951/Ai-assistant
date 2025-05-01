import speech_recognition as sr
import pyttsx3
import datetime
import time

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

#listen and recognize voice command
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:...", command)
        return command.lower()
    except sr. UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
    
# Intent detection (basic)
def process_command(command):
    if "time" in command:
        return "time"
    elif "remind me" in command or "reminder" in command:
        return "reminder"
    elif "exit" in command or "stop" in command:
        return "exit"
    else:
        return "unknown"
    
# Execute intent
def execute_command(intent, command):
    if intent == "time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif intent == "reminder":
        speak("What should I remind you about?")
        reminder = get_voice_input()
        speak("In how many seconds should I remind you?")
        try:
            seconds = int(get_voice_input())
            speak(f"Okay, I will remind you to '{reminder}' in {seconds} seconds.")
            time.sleep(seconds)
            speak(f"Reminder: {reminder}")
        except ValueError:
            speak("Sorry, I didn't understand the time duration.")
    elif intent == "unknown":
        speak("I'm not sure how to help with that.")
    elif intent == "exit":
        speak("Goodbye!")
        exit()

# Main loop
def run_assistant():
    speak("Hello, how can I help you?")
    while True:
        command = get_voice_input()
        if command == "":
            continue
        intent = process_command(command)
        execute_command(intent, command)

# Run the assistant
if __name__ == "__main__":
    run_assistant()

           