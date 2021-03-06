import cv2


class VideoHandler(object):
    def __init__(self, camera_index=0):
        self.handler = cv2.VideoCapture(camera_index)


    def grabFrame(self):
        while(True):
            ret, image = self.handler.read()
            if ret == True:
                yield cv2.imencode('.jpg', image)[1].tobytes()
            else:
                return False
