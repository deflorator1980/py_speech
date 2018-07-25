import speech_recognition as sr
r = sr.Recognizer()
# harvard = sr.AudioFile('hz.wav')
harvard = sr.AudioFile('english.wav')
with harvard as source:
    audio = r.record(source)
print(r.recognize_google(audio))

