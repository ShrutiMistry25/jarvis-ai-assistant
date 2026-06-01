import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np
import platform
import pyttsx3


chatStr = ""
chat_messages = [
    {"role": "system", "content": "You are Jarvis, a helpful virtual assistant."}
]
openai_usable = True
# https://youtu.be/Z3ZAJoi4x6Q
def ensure_api_key():
    return bool(apikey and not apikey.startswith("Your-Open-AI"))


def fallback_response(query):
    text = query.lower()
    if "how are you" in text:
        return "I am fine, sir. I am currently running without an OpenAI key."
    if "your name" in text or "who are you" in text:
        return "I am Jarvis, your personal assistant. Set an OpenAI key for smarter responses."
    if "time" in text:
        return "I can tell you the time if you ask me, but I am not connected to OpenAI right now."
    return "I cannot answer that fully until you configure an OpenAI API key."


def chat(query):
    global chatStr, chat_messages, openai_usable
    if not ensure_api_key() or not openai_usable:
        response = fallback_response(query)
        print("[Fallback mode]", response)
        safe_say(response)
        return response


    chat_messages.append({"role": "user", "content": query})
    openai.api_key = apikey
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_messages,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except openai.error.RateLimitError:
        openai_usable = False
        error_text = "OpenAI quota exceeded. Please check your plan and billing details."
        safe_say(error_text)
        response = fallback_response(query)
        safe_say(response)
        return response
    except openai.error.OpenAIError as e:
        openai_usable = False
        safe_say(f"OpenAI request failed")
        response = fallback_response(query)
        safe_say(response)
        return response
    except Exception as e:
        openai_usable = False
        safe_say("Unexpected error contacting OpenAI")
        response = fallback_response(query)
        safe_say(response)
        return response

    answer = response["choices"][0]["message"]["content"].strip()
    safe_say(answer)
    chat_messages.append({"role": "assistant", "content": answer})
    chatStr += f"Harry: {query}\n Jarvis: {answer}\n"
    return answer


def ai(prompt):
    global openai_usable
    if not ensure_api_key():
        warning = (
            "OpenAI API key is not configured. "
            "Please set apikey in config.py or use OPENAI_API_KEY in your environment."
        )
        print(warning)
        say("I cannot access OpenAI without an API key.")
        return

    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful virtual assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except openai.error.RateLimitError:
        openai_usable = False
        safe_say("OpenAI quota exceeded")
        return
    except openai.error.OpenAIError as e:
        openai_usable = False
        safe_say("OpenAI request failed")
        return
    except Exception as e:
        openai_usable = False
        safe_say("Unexpected error contacting OpenAI")
        return

    answer = response["choices"][0]["message"]["content"].strip()
    text += answer
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    filename = ''.join(prompt.split('intelligence')[1:]).strip() or "response"
    with open(f"Openai/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

def say(text):
    if platform.system() == "Windows":
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        os.system(f'say "{text}"')

def safe_say(text):
    try:
        say(text)
    except Exception as e:
        print(f"Speech error: {e}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except KeyboardInterrupt:
            print("Listening interrupted by user.")
            raise
        except Exception:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        try:
            query = takeCommand()
        except KeyboardInterrupt:
            print("User interrupted listening. Exiting.")
            break
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            if platform.system() == "Windows":
                if os.path.exists(musicPath):
                    os.startfile(musicPath)
                else:
                    say("I cannot find the music file.")
            else:
                os.system(f"open {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {minute} minutes")

        elif "open facetime".lower() in query.lower():
            if platform.system() == "Darwin":
                os.system(f"open /System/Applications/FaceTime.app")
            else:
                say("FaceTime is only available on Mac.")

        elif "open pass".lower() in query.lower():
            if platform.system() == "Darwin":
                os.system(f"open /Applications/Passky.app")
            else:
                say("Passky is only available on Mac.")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





        # say(query)