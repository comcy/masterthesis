# -*- encoding: UTF-8 -*-


"""
@file:
@subject:
"""


import numpy as np
from naoqi import ALModule, ALProxy
import main
import NAOSpeech
import NAOMotion
import NAOVision
import logging


MEMORY_SERVICE = None

TouchCount = 0

"""
@function: initMemoryService()
@description: Connect with the memory proxy
"""
def initMemoryService(SESSION):
    global MEMORY_SERVICE
    MEMORY_SERVICE = SESSION.service("ALMemory")
    logging.info('Created memory service')


"""
@function: onForeheadTocuhed(event)
@description: Returns a vector of pairs (name, bool) indicating if forehead is currently touched
"""
def onForeheadTouched(event):
    # value is 1 when pressed, 0 when released
    if event == 1:
        NAOMotion.disableHeadstiffness()
        NAOSpeech.sayText("Please, turn my head. Take a picture by pressing my middle head.")
        logging.info('Forehead touched')


"""
@function: onBackheadTouched(event)
@description: Returns a vector of pairs (name, bool) indicating if backhead is currently touched
"""
def onBackheadTouched(event):
    # value is 1 when pressed, 0 when released
    if event == 1:
        NAOMotion.enableHeadstiffness()
        NAOSpeech.sayText("My head is stiff again.")
        logging.info('Backhead touched')

"""
@function: onMiddleheadTouched(event)
@description: Returns a vector of pairs (name, bool) indicating if middlehead is currently touched
"""
def onMiddleheadTouched(event):
    # value is 1 when pressed, 0 when released
    if event == 1:
        NAOSpeech.sayText("I will take your picture")
        # NAOVision.takePicture()
        logging.info('Middlehead touched')

        NAOVision.capture_image()
        #NAOVision.subscribeCAM()

        #NAOVision.unssubsribeCAM()


"""
@function: onRHandLeftSideTouched(event)
@description: Returns a vector of pairs (name, bool) indicating if rhand left side is currently touched
"""
def onRHandLeftSideTouched(event):
    # value is 1 when pressed, 0 when released
    if event == 1:
        NAOSpeech.sayText("I open my hand!")
        NAOMotion.bringRArmInDrawposition()
        logging.info('RHand left side touched')

"""
@function: onLHandBackSideTouched(event)
@description: Returns a vector of pairs (name, bool) indicating if middlehead is currently touched
"""
def onLHandBackSideTouched(event):
    # value is 1 when pressed, 0 when released
    if event == 1:
        NAOSpeech.sayText("I raise my arms!")
        NAOMotion.bringArmsInStartPosition()
        logging.info('LHand back side touched')