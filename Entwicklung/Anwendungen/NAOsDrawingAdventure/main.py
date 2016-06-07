# -*- encoding: UTF-8 -*-

"""
@file: NAOsDrawingAdventure.py
@authors: Christian Silfang
@subject: Getting the Aldebaran robot NAO to draw the shapes it takes with its front camera using image processing and the NAOqi Python SDK API.

General annotations:
The drawing table which NAO needs for drawings should have a height of 35-40 cm. During development NAOs transport case was used as drawing table.
"""


import qi
import logging
import NAOLoghandler
import NAOMotion
import NAOSpeech
import NAOSensor
import NAOVision


## Before starting the script do settings here
# NAO URL service connection via tcp
URL = "tcp://nao.local:9559"

# Path to the logfile, directory 'log' must exist !!!
LOGFILEPATH = 'log/NAOsDrawingAdventure.log'

# NAO local current session object
SESSION = None


"""
@function: mainController
@description: This is the main function for controlling the script 'NAOsDrawingAdventures'.
"""
def mainController():

    ## Following enumeration is for understanding the structure
    ## of the script (flow chart) and for debugging reasons

    ## 1) Setup NAO before beginning of the script

    NAOMotion.turnOffAutonomousLife()

    ## 1.1) Say welcome text for users an give instructions.
    NAOSpeech.sayText("Hello, my name is Nao. I am now ready for using the NAO Drawing Adventure.")
    NAOSpeech.sayText("Use my arm touch sensors to control my gestures.") ## TODO welcome text for arm sensors
    NAOSpeech.sayText("Use my head sensors for taking some pictures. Start with the forehead sensor to disable my head stiffness.") ## TODO add the other stuff

    ## 2) Bring arms in position

    ## LHand on back side touch: bring both arms up in the air
    subscriberLHandBack = NAOSensor.MEMORY_SERVICE.subscriber("HandLeftBackTouched")
    subscriberLHandBack.signal.connect(NAOSensor.onLHandBackSideTouched)

    ## TODO RHand back side: bring right hand in drawing position

    ## TODO: opening hand!
    ## TODO DEBUG: RHand on left side touch: bring in drawing position
    subscriberRHandLeft = NAOSensor.MEMORY_SERVICE.subscriber("HandRightLeftTouched")
    subscriberRHandLeft.signal.connect(NAOSensor.onRHandLeftSideTouched)

    ## TODO RHand right side: closing hand

    ## 4) React on touching head front-/backsensors
    ##      - event handling in NAOSensor module
    ##      - commands only available by touching NAO

    ## ForeHeadTouch for disable HeadStiffness
    subscriberForehead = NAOSensor.MEMORY_SERVICE.subscriber("FrontTactilTouched")
    subscriberForehead.signal.connect(NAOSensor.onForeheadTouched)

    ## BackHeadTouch for disable HeadStiffness
    subscriberBackhead = NAOSensor.MEMORY_SERVICE.subscriber("RearTactilTouched")
    subscriberBackhead.signal.connect(NAOSensor.onBackheadTouched)

    ## 5) Take picture

    ## MiddleHeadTouch for taking a picture
    subscriberMiddlehead = NAOSensor.MEMORY_SERVICE.subscriber("MiddleTactilTouched")
    subscriberMiddlehead.signal.connect(NAOSensor.onMiddleheadTouched)

    ## 6) Image processing -> Algorithm for calculating drawing

    ## 7) Open hand for pen -> React on sensor touching

    ## 8) Close hand

    ## 9) Re-Draw the image


    ## 10) Keep program alive
    while True:
        pass

"""
@function: initConnection()
@description: This method is initializing all connections to NAO via services
"""
def initConnection():
    global SESSION
    SESSION = qi.Session()
    SESSION.connect(URL)

    ## init motion services
    NAOMotion.initAutonomousMoveService(SESSION)
    NAOMotion.initMotionService(SESSION)

    ## init memory service
    NAOSensor.initMemoryService(SESSION)

    # init vision service
    NAOVision.initVisionService(SESSION)

    ## init speech service
    NAOSpeech.initSpeechService(SESSION)


if __name__ == '__main__':

    ## Header of the app
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("| Welcome to NAOs drawing adventures:                                                                     |")
    print("| If some errors occur please read the setup module and look for correct settings of the scripts.         |")
    print("| The whole process is described by NAO. He is talking to giving advices and comands for using the script |")
    print("-----------------------------------------------------------------------------------------------------------\n")

    ## Create logfile and start logging
    NAOLoghandler.initLogfile()

    ## Initialize connection with NAO
    initConnection()

    ## Start the main-app
    mainController()

    ## Close logfile for quit logging
    NAOLoghandler.endLogfile()
    ## Footer of the app

    print("\n-----------------------------------------------------------------------------------------------------------")
    print("> END                                                                                                     |")
    print("-----------------------------------------------------------------------------------------------------------\n")