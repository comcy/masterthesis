# -*- encoding: UTF-8 -*-


import logging
import cv2
from PIL import Image
from naoqi import ALProxy

VISION_SERVICE = None
VIDEO_CLIENT = None

## initialize
eyes = None # TODO not needed?
PIL_COLOR_SPACE = "RGB"
RESOLUTION = 2   #VGA
COLOR_SPACE = 11  #RGB
FPS = 30
IMAGE_FORMAT = "PNG"

"""
@function: initVisionService()
@description: Connect with the vision service
"""
def initVisionService(SESSION): # WORKS !!!
    global VISION_SERVICE
    VISION_SERVICE = SESSION.service("ALVideoDevice")
    logging.info('Created vision service')


def subscribeCAM():
  global VIDEO_CLIENT
  VIDEO_CLIENT = VISION_SERVICE.subscribe("NAO_CAM", RESOLUTION, COLOR_SPACE, FPS) # subscribe to "NAO_CAM"
  nao_image = VISION_SERVICE.getImageRemote(VIDEO_CLIENT) # capture image from "NAO_CAM"

  logging.info('subscribe CAM')

  ## get image properties
  image_width = nao_image[0]
  image_height = nao_image[1]
  buffer = nao_image[6]

  ## save original captured image in directory
  image = Image.fromstring(PIL_COLOR_SPACE, (image_width, image_height), buffer)
  image.save("img/original_image.png", IMAGE_FORMAT)
  image.show()

  logging.info('take picture')


def unssubsribeCAM():
  VISION_SERVICE.unsubscribe(VIDEO_CLIENT)
  logging.info('unsubscribe CAM')

"""
@function: capture_image
@description: Use NAO's camera to detect the shape to draw. Uses
PIL at first, then uses Canny Edge Detection via OpenCV.
"""
def capture_image():     ## TODO This method works !!!!

  video_proxy = ALProxy("ALVideoDevice", "192.168.1.105", 9559) ## for debugging reasons use a fixed ip address/port

  ## capturing the image
  video_client = video_proxy.subscribe("NAO_CAM", RESOLUTION, COLOR_SPACE, FPS) # subscribe to "NAO_CAM"
  nao_image = video_proxy.getImageRemote(video_client) # capture image from "NAO_CAM"
  video_proxy.unsubscribe(video_client) # release "NAO_CAM"

  ## get image properties
  image_width = nao_image[0]
  image_height = nao_image[1]
  buffer = nao_image[6]

  ## save original captured image
  image = Image.frombytes(PIL_COLOR_SPACE, (image_width, image_height), buffer)
  image.save("img/original_image.png", IMAGE_FORMAT)

  image.show() # show captured image

  w, h = image.size
  image.crop((0, 10, w, h-10)).save("img/original_image.png")

  frame = cv2.imread("img/original_image.png")
  gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
  blur = cv2.GaussianBlur(gray, (3,3), 0)
  cannyImage = cv2.Canny(blur, 10, 100)

  cv2.imwrite("img/canny_image.png", cannyImage)
