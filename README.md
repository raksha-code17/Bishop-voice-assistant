# Bishop Voice Assistant

Bishop is a simple voice-controlled virtual assistant built with Python. It listens for a wake word, responds with speech, opens websites, plays music, and performs basic commands.

## Features

* Wake word activation using **"Bishop"**
* Open popular websites:

  * Google
  * YouTube
  * LinkedIn
  * Instagram
* Play songs from a custom music library
* Tell the current time
* Voice responses using text-to-speech
* Basic command handling and error management

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Webbrowser
* Datetime

## Project Structure

Bishop/
│
├── main.py
├── musiclibrary.py
├── README.md

## Installation

Install dependencies:
pip install SpeechRecognition pyttsx3 pyaudio

## Running the Assistant

Start the program:
python main.py

When Bishop says it is listening, say:
Bishop

Then give commands such as:

Open Google
Open YouTube
Play believer
What is the time
Help
Exit

## Example Music Library

music = {
    "humnava" : "https://youtu.be/pP12RCC6Nss?si=hFHWM9jeDHY-ljpT",
    "kali kali zulfon ke" : "https://youtu.be/o-7b6ctrQX0?si=ungmw930V3cUPCiP"
}

## Future Improvements

* Weather information
* AI-powered conversations
* WhatsApp messaging
* Application launching
* Battery monitoring
* Wikipedia search
* Graphical User Interface (GUI)

## Author
Developed by Raksha Gajeshwar

