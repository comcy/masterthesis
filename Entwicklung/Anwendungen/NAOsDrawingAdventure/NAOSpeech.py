# -*- encoding: UTF-8 -*-


"""
@file:
@subject:
"""


import logging

# Constants.
SPEECH_SERVICE = None

"""
@function: initSpeechService(SESSION)
@description: This function creates a 'SPEECH_SERVICE'-object based on the 'ALTextToSpeech'-module for the actual session.
"""
def initSpeechService(SESSION):
  global SPEECH_SERVICE
  SPEECH_SERVICE = SESSION.service("ALTextToSpeech")
  logging.info("Created speech service")


"""
@function: sayText(Text)
@description: This makes NAO say a Text given by the 'Text'-parameter.
"""
def sayText(Text):
    SPEECH_SERVICE.say(Text)
    logging.info('NAO said: "' +  Text + '"')