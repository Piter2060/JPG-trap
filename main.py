import os
import numpy as np
import cv2, time
import zipfile

pwd = os.getcwd()
files = []

def zip(files_table):
    zf = zipfile.ZipFile('zipfile_write.zip', mode='a')
    for file in files_table:
        zf.write(file)
    zf.close()

def cam(fr):
    import cv2
    camera_port = 0

    # Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = fr

    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    camera = cv2.VideoCapture(camera_port)

    # Captures a single image from the camera and returns it in PIL format
    def get_image():
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = camera.read()
        return im

    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in range(ramp_frames):
        temp = get_image()
    camera_capture = get_image()
    file = "test_image_" + str(fr) + ".jpg"
    files.append(file)
    cv2.imwrite(file, camera_capture)
    del (camera)
cam(0)
cam(15)
cam(30)
zip(files)