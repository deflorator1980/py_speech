FROM python:3.6
RUN mkdir /files
WORKDIR /app
COPY . /app
RUN pip install SpeechRecognition
RUN apt-get update && \
apt-get install -y swig && \
apt-get install -y python-pyaudio && \
apt-get install -y libpulse-dev && \
apt-get install -y libasound2-dev
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install pocketsphinx
RUN pip install flask
