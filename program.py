"""Jagadeesh M B
Sri Jayachamarajendra College of Engineering, Mysuru"""

import time
import cv2 
from flask import Flask, render_template, Response,request, make_response
import pyautogui
import numpy as np
import socket

"""Getting IP address of a laptop"""
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

"""Taking screenshot of a screen and converting into bytes"""
def gen():
    while(True):
        image = pyautogui.screenshot()
        img = np.array(image).astype(np.uint8) 
        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host=local_ip, port=8000)
    





    
