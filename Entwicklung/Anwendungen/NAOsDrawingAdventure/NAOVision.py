# -*- encoding: UTF-8 -*-


import logging
import cv2
from PIL import Image
from naoqi import ALProxy
from io import BytesIO

VISION_SERVICE = None
VIDEO_CLIENT = None

## initialize
eyes = None  # TODO not needed?
PIL_COLOR_SPACE = "RGB"
RESOLUTION = 2  # VGA
COLOR_SPACE = 11  # RGB
FPS = 30
IMAGE_FORMAT = "PNG"

"""
@function: initVisionService()
@description: Connect with the vision service
"""


def initVisionService(SESSION):  # WORKS !!!
    global VISION_SERVICE
    VISION_SERVICE = SESSION.service("ALVideoDevice")
    logging.info('Created VISION_SERVICE')


def subscribeCam():
    global VIDEO_CLIENT
    VIDEO_CLIENT = VISION_SERVICE.subscribe("NAO_CAM", RESOLUTION, COLOR_SPACE, FPS)  # subscribe to "NAO_CAM"
    logging.info('subscribe NAO_CAM')


def unssubscribeCam():
    VISION_SERVICE.unsubscribe(VIDEO_CLIENT)
    logging.info('unsubscribe NAO_CAM')


"""
@function: captureImage
@description: Use NAO's camera to detect the shape to draw. Uses
PIL at first, then uses Canny Edge Detection via OpenCV.
"""


def captureImage():
    nao_image = VISION_SERVICE.getImageRemote(VIDEO_CLIENT)  # capture image from "NAO_CAM"
    logging.info('capture image')

    ## get image properties
    image_width = nao_image[0]
    image_height = nao_image[1]
    binarray = nao_image[6]

    ## save original captured image in directory
    buffer = BytesIO(binarray).read()
    image = Image.frombytes(PIL_COLOR_SPACE, (image_width, image_height), buffer)
    image.save("img/original_image.png", "PNG")
    image.show()

    w, h = image.size
    image.crop((0, 10, w, h - 10)).save("img/original_image.png")

    frame = cv2.imread("img/original_image.png")
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    cannyImage = cv2.Canny(blur, 10, 100)

    logging.info('feature extraction of image')

    cv2.imwrite("img/canny_image.png", cannyImage)

    # TODO Show canny image
    # cannyImage.show()
