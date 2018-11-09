#Code adapted from: https://www.hackster.io/mjrobot/video-streaming-web-server-ef11e3

import cv2
from flask import Flask, render_template, Response
# Raspberry Pi camera module (requires picamera package, developed by Miguel Grinberg)
from video_handler import VideoHandler
app = Flask(__name__)
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
def gen(camera):
    """Video streaming generator function."""
    for frame in camera.grabFrame():
        cv2.imwrite('tmp/t.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('tmp/t.jpg', 'rb').read() + b'\r\n')
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(VideoHandler()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
