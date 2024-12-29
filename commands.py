from playsound3 import playsound
import random
# from pathlib import Path
import os
import re
import webbrowser
from sound import Sound

module_path = os.path.realpath(__file__)    
folder_comm = re.sub(r"\bcommands.py\b", "jarvis-remake", module_path)
audio_realpath = folder_comm.replace("main.py", "jarvis-remake")

audio_run = f"{audio_realpath}/run.wav"
audio_hello = [f"{audio_realpath}/greet1.wav", f"{audio_realpath}/greet2.wav"]
audio_completed = [f"{audio_realpath}/ok1.wav", f"{audio_realpath}/ok2.wav", f"{audio_realpath}/ok3.wav", f"{audio_realpath}/ok4.wav"]

def Hello():
    print(folder_comm)
    if audio_run and os.path.exists(audio_run):
        playsound(audio_run)
    else:
        print("Файл не найден")
def open_in_brouser():
    webbrowser.open('https://www.youtube.com/', new=2)
    rand_comleted = random.choice(audio_completed)
    if rand_comleted and os.path.exists(rand_comleted):
        playsound(rand_comleted)
    else:
        print("Файл не найден")
def open_brouser():
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    rand_comleted = random.choice(audio_completed)
    if rand_comleted and os.path.exists(rand_comleted):
        playsound(rand_comleted)
    else:
        print("Файл не найден")
def com_quit():
    rand_comleted = random.choice(audio_completed)
    if rand_comleted and os.path.exists(rand_comleted):
        playsound(rand_comleted)
    else:
        print("Файл не найден")
    quit()

def mute_sound():
    rand_comleted = random.choice(audio_completed)
    if rand_comleted and os.path.exists(rand_comleted):
        playsound(rand_comleted)
    else:
        print("Файл не найден")
    Sound.mute()
    
def unmute_sound():
    if Sound.is_muted:
        Sound.mute()
    rand_comleted = random.choice(audio_completed)
    if rand_comleted and os.path.exists(rand_comleted):
        playsound(rand_comleted)
    else:
        print("Файл не найден")
def not_found():
    playsound(f"{audio_realpath}/not_found.wav")
    

commands_main = {("привет", "хай"):Hello, 
                 ("пока", "до свидания"):com_quit,
                 ("открой ютуб", "включи ютуб", "ютуб"):open_in_brouser, 
                 ("открой браузер", "браузер", "гугл","хром"):open_brouser,
                 ("выключи звук","отруби звук", "выруби звук", "отключи звук"):mute_sound,
                 ("включи звук", "вруби звук", "включить звук"):unmute_sound
                 
                 
                 
                 
                 }