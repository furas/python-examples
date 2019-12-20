#!/usr/bin/env python3 

# date: 2019.12.11
# 

from flask import Flask, request, send_file
from gtts import gTTS

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def t2s():
    print(request)
    text = request.get_json()
    print(text)
    obj = gTTS(text = text, slow = False, lang = 'en')    
    obj.save('audio.wav')
    return send_file('audio.wav')

if __name__ == "__main__":
    app.run()
