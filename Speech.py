# Note: you need to be using OpenAI Python v0.27.0 for the code below to work

import sounddevice as sd
from scipy.io.wavfile import write
fs = 44100  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 

import openai
openai.api_key = "YOUR Openai.api.Key"
audio_file= open("output.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript.text)


Chat_completion =openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role":"user","content": transcript.text}])
print("GPT RESPONSE: "+Chat_completion.choices[0].message.content)
    
import pyttsx3

text_speech = pyttsx3.init()
answer = Chat_completion.choices[0].message.content
text_speech.say(answer)
text_speech.runAndWait()
