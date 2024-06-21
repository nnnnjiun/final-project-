## To run server: python whisper_server.py
## To run client: python post_audio.py

import requests

url = "http://127.0.0.1:5000/audio"
#url = "http://192.168.0.162:5000/audio"
#url = "https://bf73-35-247-137-211.ngrok-free.app/audio"

#my_audio = {'audio': open("audio1.flac", "rb")}
#my_audio = {'audio': open("audio2.mp3", "rb")}
#my_audio = {'audio': open("audio3.mp4", "rb")}
#my_audio = {'audio': open("hello_howareyou.mp4", "rb")}

# python ../gTTS.py "早安你好" zh
my_audio = {'audio': open("gTTS.mp3", "rb")}

r = requests.post(url, files=my_audio)

print(r.text)
f=open('./docs/llm-papers/schedule.txt','w+')
f.write(r.text)