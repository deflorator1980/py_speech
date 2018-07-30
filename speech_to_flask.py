from flask import Flask, render_template, request
from werkzeug import secure_filename
import speech_recognition as sr


app = Flask(__name__)

def speech():
    r = sr.Recognizer()
    harvard = sr.AudioFile('file.wav')
    with harvard as source:
        audio = r.record(source)
    # return r.recognize_google(audio)
    return r.recognize_sphinx(audio)

@app.route('/')
def upload():
   return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
       f = request.files['file']
       f.save(secure_filename("file.wav"))
       text = speech()
       return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
