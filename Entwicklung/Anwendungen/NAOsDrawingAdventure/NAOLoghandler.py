# -*- encoding: UTF-8 -*-

"""
@file: NAOLoghandler.py
@authors: Christian Silfang
@subject: This module is for logging the whole NAO application.
"""

import datetime
import os.path
import logging
import main

## Set properties for the logger
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") # get current time

"""
@function: init_logfile()
@description: Initialize a logfile for every program start.
"""
def initLogfile():
    logtext = "NEW Log"
    logging.basicConfig(filename=main.LOGFILEPATH, level=logging.INFO)
    if os.path.isfile(main.LOGFILEPATH) == True:
        file = open(main.LOGFILEPATH, 'a+')
        file.write("\n\n>>>   " + timestamp + ":   " + logtext + "\n")
        file.close()

def endLogfile():
    logtext = "END Log"
    logging.basicConfig(filename=main.LOGFILEPATH, level=logging.INFO)
    if os.path.isfile(main.LOGFILEPATH) == True:
        file = open(main.LOGFILEPATH, 'a+')
        file.write("<<<   " + logtext + "\n\n")
        file.close()