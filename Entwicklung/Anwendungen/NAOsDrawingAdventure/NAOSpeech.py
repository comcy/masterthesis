# -*- encoding: UTF-8 -*-


"""
@file:
@subject:
"""


import logging

SPEECH_SERVICE = None


"""
@function:
@description:
"""
def initSpeechService(SESSION):
  global SPEECH_SERVICE
  SPEECH_SERVICE = SESSION.service("ALTextToSpeech")
  logging.info("Created speech service")


"""
@function: sayText()
@description: This method is for calling a defined saying
"""
def sayText(Text):
    SPEECH_SERVICE.say(Text)
    logging.info('NAO said: "' +  Text + '"')