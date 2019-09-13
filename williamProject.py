# -*- coding: utf-8 -*-

import os, time
from pygame import mixer
from flask import Flask, render_template, request

app = Flask(__name__,static_url_path = "", static_folder = ".")

def playsong():
   mixer.init()
   mixer.music.load('/home/j040n3t0/Documentos/python-learn/williamProject/f1.mp3')
   mixer.music.load('/home/j040n3t0/Documentos/python-learn/williamProject/f1.mp3')
   mixer.music.play()
   time.sleep(15)
   mixer.music.stop()

@app.route('/')
def index_default():
	return render_template('index.html')

#//rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#//background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    playsong()
    return "nothing"

if __name__ == '__main__':
	app.run(debug = True, host="0.0.0.0", port=5000)
