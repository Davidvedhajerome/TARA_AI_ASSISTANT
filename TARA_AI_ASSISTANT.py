import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import requests
import subprocess
from tkinter import  filedialog
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import threading
open_app_flag = False

engine = pyttsx3.init()
newVoiceRate = 130
engine.setProperty('rate', newVoiceRate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak_and_append("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak_and_append("Good Afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak_and_append("Good Evening Sir")
    else:
        speak_and_append("Good Night Sir")
    speak_and_append("Tara at your service. Please tell me how can I help you?")

def screenshot():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img = pyautogui.screenshot()
        img.save(file_path)
        append_output(f"Screenshot saved to {file_path}")

def cpu():
    usage = str(psutil.cpu_percent())
    speak_and_append('CPU is at ' + usage + ' percent')
    battery = psutil.sensors_battery()
    speak_and_append('Battery is at ' + str(battery.percent) + ' percent')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak_and_append(audio):
    speak(audio)
    append_output(audio)

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak_and_append("The current time is " + Time)

def date():
    Date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak_and_append("Today's date is " + Date)

def joke():
    joke = pyjokes.get_joke()
    speak_and_append(joke)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        append_output("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        append_output("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        append_output(f" {query}\n")
    except Exception as e:
        append_output("Error: " + str(e))
        speak_and_append("Say that again please...")
        return "None"
    return query

def weather(city):
    api_key = "b52c66bcd330f1661de28426f176faac"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        temp_celsius = temp - 273.15
        result = f"The temperature in {city} is {temp_celsius:.2f} degrees Celsius with {weather_desc}."
        speak_and_append(result)
    else:
        speak_and_append("City not found")

def get_news():
    api_key = "81a16fa94dc54006bd497762913c248a"
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": "us",
        "pageSize": 5
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        if articles:
            speak_and_append("Here are the top news headlines")
            for article in articles[:5]:
                title = article["title"]
                description = article["description"]
                news = f"{title}\n{description}\n"
                speak_and_append(news)
        else:
            speak_and_append("No articles found")
    else:
        speak_and_append("Failed to fetch news data")

def open_application(app_name):
    app_mapping = {
        'notepad': 'notepad.exe',
        'calculator': 'calc.exe',
        'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        'word': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE',
        'excel': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',
        'powerpoint': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE',
        'paint': 'mspaint.exe',
        'file explorer': 'explorer.exe',
        'task manager': 'taskmgr.exe',
        'photos': 'C:\\Program Files\\Windows Photo Viewer\\PhotoViewer.dll',
        'calendar': 'C:\\Program Files\\Windows Calendar\\wincal.exe',
        'media player': 'C:\\Program Files\\Windows Media Player\\wmplayer.exe',
        'edge': 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
        'firefox': 'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
        'vlc': 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe',
    }
    try:
        if app_name in app_mapping:
            subprocess.Popen(app_mapping[app_name])
            speak_and_append(f"Opening {app_name}")
        else:
            speak_and_append(f"Application {app_name} not found in predefined list.")
    except Exception as e:
        speak_and_append(f"Failed to open {app_name}: {e}")


def process_query(query):
    if 'time' in query:
        time()
    elif 'wikipedia' in query:
        speak_and_append("Searching...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        append_output(results)
        speak(results)
    elif 'date' in query:
        date()
    elif 'offline' in query:
        quit()
    elif 'open in chrome' in query:
        speak_and_append("What should I open?")
        chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        search = takeCommand().lower()
        wb.get(chrome).open_new_tab(search + '.com')
    elif 'search in chrome' in query:
        speak_and_append("What should I search?")
        search = takeCommand().lower()
        wb.get('windows-default').open_new_tab(f"https://www.google.com/search?q={search}")
    elif 'logout' in query:
        os.system("shutdown -l")
    elif 'shutdown' in query:
        os.system("shutdown /s /t 1")
    elif 'restart' in query:
        os.system("shutdown /r /t 1")
    elif 'play songs' in query:
        song_dir = "C:\\Users\\LENOVO\\Music"
        songs = os.listdir(song_dir)
        os.startfile(os.path.join(song_dir, songs[0]))
        speak_and_append("Playing Songs")
    elif 'remember' in query:
        speak_and_append("What should I remember?")
        data = takeCommand().lower()
        speak_and_append("You told me to remember " + data)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as remember_file:
                remember_file.write(data)
    elif 'do you know' in query:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as remember_file:
                remember_data = remember_file.read()
                speak_and_append("You told me to remember " + remember_data)
    elif 'screenshot' in query:
        screenshot()
    elif 'cpu' in query:
        cpu()
    elif 'joke' in query:
        joke()
    elif 'weather' in query:
        speak_and_append("Please tell me the city name")
        city = takeCommand().lower()
        weather(city)
    elif 'news' in query:
        get_news()
    elif 'open application' in query:
        speak_and_append("Which application should I open?")
        app_name = takeCommand().lower()
        open_application(app_name)

def start_thread(mode):
    thread = threading.Thread(target=mode)
    thread.start()

def on_enter(event=None):
    mode = mode_var.get()
    if mode == "speech":
        start_thread(speak_process_query)
    elif mode == "text":
        start_thread(write_query)

C = 0

def speak_process_query():
    global C
    if C < 1:
        wishme()
    C += 1
    while True:
        query = takeCommand().lower()
        process_query(query)

def write_query():
    global C
    global open_app_flag
    if C < 1:
        wishme()
    C += 1
    remember_flag = False
    while True:
        query = query_entry.get().strip().lower()
        if query:
            if remember_flag:
                data = query
                if data:
                    speak_and_append("You told me to remember " + data)
                    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
                    if file_path:
                        with open(file_path, "w") as remember_file:
                            remember_file.write(data)
                    remember_flag = False
                query_entry.delete(0, tk.END)
            elif 'remember' in query:
                remember_flag = True
                speak_and_append("What should I remember?")
                query_entry.delete(0, tk.END)
            elif 'open application' in query:
                open_app_flag = True
                speak_and_append("Which application should I open?")
                query_entry.delete(0, tk.END)
                time.sleep(3)
            elif open_app_flag:
                app_to_open = query
                open_application(app_to_open)
                open_app_flag = False
                query_entry.delete(0, tk.END)


        else:
            process_query(query)
            query_entry.delete(0, tk.END)
        root.update()
def reset_app():
    global remember_flag, open_app_flag
    remember_flag = False
    open_app_flag = False
    query_entry.delete(0, tk.END)
def append_output(text):
    text_area.insert(tk.END, "Assistant: " + text + "\n")
    text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tara AI Assistant")
    frame = tk.Frame(root)
    frame.pack(pady=10)
    microphone_image = Image.open("D:\\Mic.png")
    microphone_image = microphone_image.resize((50, 50), Image.LANCZOS)
    microphone_icon = ImageTk.PhotoImage(microphone_image)
    microphone_label = tk.Label(frame, image=microphone_icon)
    microphone_label.pack(side=tk.LEFT, padx=10)
    mode_var = tk.StringVar(value="speech")
    speech_mode_button = tk.Radiobutton(frame, text="Speech Mode", variable=mode_var, value="speech")
    speech_mode_button.pack(side=tk.LEFT)
    write_mode_button = tk.Radiobutton(frame, text="Write Mode", variable=mode_var, value="text")
    write_mode_button.pack(side=tk.LEFT)
    query_entry = tk.Entry(frame, width=50)
    query_entry.pack(side=tk.LEFT)
    button = tk.Button(frame, text="Start", command=on_enter)
    button.pack(side=tk.RIGHT, padx=10)
    root.bind("<Return>", on_enter)
    text_area = scrolledtext.ScrolledText(root, height=20, width=80)
    text_area.pack()
    root.mainloop()
