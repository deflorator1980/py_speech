from flask import Flask
import speech_recognition as sr

app = Flask(__name__)

def speech():
    r = sr.Recognizer()
    harvard = sr.AudioFile('hz.wav')
    # harvard = sr.AudioFile('english.wav')
    with harvard as source:
        audio = r.record(source)
    return r.recognize_google(audio)

@app.route('/')
def index():
    text = speech()
    return text

app.run(host='0.0.0.0', debug=True)   # reboot the page by changing
