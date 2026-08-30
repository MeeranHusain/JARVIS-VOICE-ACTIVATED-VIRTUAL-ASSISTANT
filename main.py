import speech_recognition as sr
import webbrowser
import pyttsx3
# import musicLibrary
import yt_dlp
import requests
import os
from dotenv import load_dotenv
import ollama

load_dotenv()

newsapi = os.getenv("NEWSDATA_API_KEY")
api_key = os.getenv("OLLAMA_API_KEY")

recognizer = sr.Recognizer()

client = ollama.Client(host="https://ollama.com", headers={"Authorization": f"Bearer {api_key}"})

# ================= Text-to-Speech Function =================
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ================= AI Process Function =================
def aiProcess(command):
    response = client.chat(
        model="gpt-oss:20b-cloud",
        messages=[
            {
                "role": "system",
                "content": "You are Jarvis, a helpful virtual assistant."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return response["message"]["content"]


# ================= Command Processing Function =================
def processCommand(c):
    command = c.lower().strip()

    # ================= for opening websites =================
    if command.startswith("open "):
        website = command[5:].strip()

        if not website:
            speak("Please tell me which website you want to open.")
            return

        # Direct URL
        if website.startswith(("http://", "https://")):
            url = website
            print(f"Opening: {url}")
            webbrowser.open(url)

        # Domain name
        elif "." in website and " " not in website:
            url = f"https://{website}"
            print(f"Opening: {url}")
            webbrowser.open(url)

        # Website name
        else:
            search_url = (
                "https://www.google.com/search?q="
                + website.replace(" ", "+")
            )

            print(f"Searching website: {website}")
            webbrowser.open(search_url)
    
    # ================= for music commands =================
    # elif command.startswith("play "):
    #     song = command[5:].strip()

    #     if song in musicLibrary.music:
    #         link = musicLibrary.music[song]
    #         webbrowser.open(link)
    #     else:
    #         speak("Sorry, I could not find that song.")
    
    elif command.startswith("play "):
        song = command[5:].strip()

        if song:
            speak(f"Searching for {song}")

            try:
                ydl_opts = {
                    "quiet": True,
                    "extract_flat": True,
                    "noplaylist": True
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    result = ydl.extract_info(
                        f"ytsearch1:{song}",
                        download=False
                    )

                if result and result.get("entries"):
                    video = result["entries"][0]
                    video_url = video["url"]

                    print(f"Playing: {video.get('title')}")
                    webbrowser.open(video_url)

                else:
                    speak("Sorry, I could not find that song.")

            except Exception as e:
                print("Music Error:", e)
                speak("Sorry, I could not play that song.")

        else:
            speak("Please tell me which song you want to play.")
        
    # ================= for news commands =================
    elif "news" in command:
        newsurl = f"https://newsdata.io/api/1/latest?apikey={newsapi}&country=in&language=en"
        try:
            r = requests.get(newsurl, timeout=10)
        except requests.RequestException as e:
            print("News API Error:", e)
            speak("Sorry, I could not connect to the news service.")
            return
        
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
        # ================= for AI commands =================
        response = aiProcess(command)
        print(f"Jarvis: {response}")
        speak(response)

# ================= Main Loop =================
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

            if "jarvis" in word.lower():

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
            

            