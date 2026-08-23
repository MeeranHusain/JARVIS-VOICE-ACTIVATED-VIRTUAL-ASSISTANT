import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from dotenv import load_dotenv
load_dotenv()
newsapi = os.getenv("NEWSDATA_API_KEY")

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    command = c.lower().strip()

    # ================= for opening websites =================
    if command.startswith("open "):
        website = command.replace("open ", "", 1).strip()

        # Website name ko URL me convert karo
        url = f"https://www.{website}.com"

        print(f"Opening: {url}")
        webbrowser.open(url)
    
    # ================= for music commands =================
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    # ================= for news commands =================
    elif "news" in c.lower():
        newsurl = f"https://newsdata.io/api/1/latest?apikey={newsapi}&country=in&language=en"
        r = requests.get(newsurl)
        # print(r.json())
        if r.status_code == 200:
            data = r.json()
            articles = data.get("results", [])
            
            if not articles:
                speak("Sorry, I could not find any Indian news.")
                return

            speak("Here are the latest Indian news headlines.")

            for article in articles[:5]: 
                headline = article.get("title")
                print(f"Headline: {headline}\n")
                speak(headline)
        
        else:
            print("News API Error:", r.status_code)
            speak("Sorry, I could not fetch the news.")

    else:
        print(f"Unknown command: {c}")


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:

        try:
            # Listen for wake word
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            print("Recognizing...")

            word = recognizer.recognize_google(audio)

            print(f"You said: {word}")

            if word.lower().strip() == "jarvis":

                speak("Yes, how can I assist you?")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                print("Recognizing command...")
                command = recognizer.recognize_google(audio)

                print(f"Command: {command}")

                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out...")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Google Speech Recognition error: {e}")

        except Exception as e:
            print(f"Error: {e}")
            
            