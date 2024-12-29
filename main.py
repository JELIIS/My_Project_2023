import json
from vosk import Model, KaldiRecognizer
import commands
import os
import re
import pyaudio

script_path = os.path.realpath(__file__)   
model_path = re.sub(r"\bmain.py\b", "small_model", script_path)
model = Model(model_path)

rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]



for text in listen():
    n = False
    for command_name in commands.commands_main:
        for i in command_name:
            if i == text:
                n = True
                command_function = commands.commands_main[command_name]()
    if n == False:
        commands.not_found()
    print(text)


    