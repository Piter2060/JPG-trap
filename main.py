import os
import numpy as np
import cv2, time
import zipfile
from datetime import datetime

pwd = os.getcwd()
files = []
date = datetime.now().isoformat(timespec="minutes")
date = date[0:-3] + date[-2::]

def zip(files_table):
    zip_name = str(date) + ".zip"
    print(zip_name)
    zf = zipfile.ZipFile(zip_name, mode='a')
    for file in files_table:
        zf.write(file)
    zf.close()

"""def clear(files_table):
    for file in files_table:
        os.remove(file)
    os.remove()"""




def cam(fr):
    import cv2
    camera_port = 0
    ramp_frames = fr
    camera = cv2.VideoCapture(camera_port)
    def get_image():
        retval, im = camera.read()
        return im

    for i in range(ramp_frames):
        temp = get_image()
    camera_capture = get_image()
    file = "test_image_" + str(fr) + ".jpg"
    files.append(file)
    cv2.imwrite(file, camera_capture)
    del (camera)
cam(0)
cam(1)
cam(2)
zip(files)