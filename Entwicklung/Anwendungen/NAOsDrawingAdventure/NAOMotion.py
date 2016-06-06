# -*- encoding: UTF-8 -*-


import time
import logging


AUTONOMOUSMOVES_SERVICE = None
MOTION_SERVICE = None


"""
@function: initAutonomousMoveProxy()
@description: Connect with the motion proxy
"""
def initAutonomousMoveService(SESSION):
    global AUTONOMOUSMOVES_SERVICE
    AUTONOMOUSMOVES_SERVICE = SESSION.service("ALAutonomousMoves")
    logging.info('Created autonomous move service')


"""
@function: initMotionProxy()
@description: Connect with the motion proxy
"""
def initMotionService(SESSION):
    global MOTION_SERVICE
    MOTION_SERVICE = SESSION.service("ALMotion")
    logging.info('Created motion service')


######## turn off autonomo ###############
def turnOffAutonomousLife():
  AUTONOMOUSMOVES_SERVICE.setBackgroundStrategy("none")

"""
@function: disableHeadstiffness()
@description: Disables NAOs head stiffness.
"""
def disableHeadstiffness():
  MOTION_SERVICE.setStiffnesses("Head", 0.0)
  logging.info('Head stiffness disabled')


"""
@function: enableHeadstiffness()
@description: Enables NAOs head stiffness.
"""
def enableHeadstiffness():
  MOTION_SERVICE.setStiffnesses("Head", 1.0)
  logging.info('Head stiffness enabled')


"""
@function: bring_rarm_in_drawposition()
@description: Brings the right arm in drawing position and the left arm straight up.
"""
def bringRArmInDrawposition():
  effector = ["RArm"]
  path = [0.39121198654174805, -0.03839196264743805, 0.7132680416107178,
          0.9603259563446045, 0.7884340286254883, 0.7547999620437622]
  MOTION_SERVICE.setAngles(effector, path, 0.3)
  #MOTION_PROXY.angleInterpolationWithSpeed(effector, path, 0.3)


"""
@function: bring_arms_in_position()
@description: Brings both arms in an straight up position for init.
"""
def bringArmsInStartPosition():
  effectors = ["LArm","RArm"]
  path = [[-1.716588020324707, 0.11500804126262665, -0.1150919571518898,
           -0.03490658476948738, -1.4542739391326904, 0.7563999891281128],
          [-1.6628141403198242, 0.09506604075431824, 1.1704000234603882,
           0.07367396354675293, 0.48470205068588257, 0.7555999755859375]]
  for i in range(len(path)):
    MOTION_SERVICE.setAngles(effectors[i], path[i], 0.2)
    #MOTION_PROXY.angleInterpolationWithSpeed(effectors[i], path[i], 0.2)
    time.sleep(4)


"""
@function: draw(points)
@description: Draws the shape seen by NAO with the right arm.
"""
# def draw(points):
#   effector = "RArm"
#
#   path = lookup_table(points)
#
#   for i in range(len(path)):
#     Setup.MOTION_PROXY.angleInterpolationWithSpeed(effector, path[i], 0.2)
#     time.sleep(2)
