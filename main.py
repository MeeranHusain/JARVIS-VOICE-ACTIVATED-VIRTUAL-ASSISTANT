import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    command = c.lower().strip()

    if command.startswith("open "):
        website = command.replace("open ", "", 1).strip()

        # Website name ko URL me convert karo
        url = f"https://www.{website}.com"

        print(f"Opening: {url}")
        webbrowser.open(url)
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

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

                speak("Yes, say...")

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
            
            