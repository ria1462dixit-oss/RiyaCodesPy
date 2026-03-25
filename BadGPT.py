import pyttsx3
from datetime import datetime

def speak(text):
    print("AI Bot:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


speak(" I am your Assistant for the day. Type 'exit' to end.\n")

abusive_words = ["idiot", "stupid", "dumb", "shut up"]
abuse_count = 0

while True:
    user_input = input("You: ").lower()
  
    if any(word in user_input for word in abusive_words):
        abuse_count += 1

        if abuse_count == 1:
            speak("Please be respectful. Kindly stay within limits.")

        elif abuse_count == 2:
            speak("This is your second warning. Avoid abusive language.")

        else:
            speak("You are a swine")


    elif "hello" in user_input or "hi" in user_input:
        speak("Hello! I am Oliver")

    elif "how are you" in user_input:
        speak("I am functioning perfectly. What about you?")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "your name" in user_input:
        speak("My name is Oliver, your assistant.")

    elif "thank" in user_input:
        speak("You're welcome!")

    elif "bored" in user_input: speak("We could chat… I’m quite interesting, you know.")

    elif "exit" in user_input:
        speak("Goodbye! Try not to miss me too much 😄!")
        break

    else:
        speak("I did not understand that. Try something else.")