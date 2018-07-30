FROM python:3.5
RUN mkdir /files
WORKDIR /app
COPY . /app
RUN pip install SpeechRecognition
RUN pip install flask
