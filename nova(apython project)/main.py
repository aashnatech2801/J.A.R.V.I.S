import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "693c458b336746b9a88321b22750da5a"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if c.lower() == "open google" or c.strip() == "google":
        print("Opening Google")
        webbrowser.open("https://www.google.com")
    elif c.lower() == "open youtube" or "youtube" in c.lower():
        print("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif c.lower() == "open Linkedin" or "Linkedin" in c.lower():
        print("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com")
    elif c.lower() == "open facebook" or "facebook" in c.lower():
        print("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif c.lower()== "open github" or "github" in c.lower():
        print("Opening Github")
        webbrowser.open("https://www.github.com")
    elif c.lower() == "open instagram" or "instagram" in c.lower():
        print("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "play" in c.lower():   
       parts = c.lower().split(" ")
       if len(parts) > 1:
        song = parts[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            print(f"Sorry, I couldn't find {song} in the library")
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        data = r.json()
        articles = data["articles"]
        for article in articles:
            print(article["title"])

    else:
        print("unfortunately, I cannot process that command. Please try again.")
if __name__ == "__main__":
    speak("Initializing Jarvis, your personal assistant")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
              r.adjust_for_ambient_noise(source)
              print("Listening for wake word...")
              audio = r.listen(source, timeout=2, phrase_time_limit=5)
            
            word = r.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "jarvis":
                print("Yes, how can I assist you?")
            
                with sr.Microphone() as source:
                   print("Jarvis Activated...")
                   audio = r.listen(source)
                command = r.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)
        #except Exception as e:
        #    print(f"Sorry, I could not understand the audio. Error: {e}")
        except sr.UnknownValueError:
            print("Could not understand — try speaking more clearly")
        except sr.RequestError as e:
            print(f"Google API error: {e}")
        except OSError:
            print("Microphone not found")
            break
        except Exception as e:
            print(f"Error: {e}")
