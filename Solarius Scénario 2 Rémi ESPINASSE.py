#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Mon 31 May 2021
# Author: Espinasse Rémi
# Description: Solarius project step 1
# Python Version 3.6

import time
import random
from adafruit_servokit import ServoKit
from adafruit_circuitplayground.express import cpx

kit = ServoKit(channels=8)

def initial_pos():

    kit.servo[4].angle = pitch
    time.sleep(1)
    kit.servo[1].angle = yaw
    time.sleep(1)
    return(pitch, yaw)

def rot_lyaw(yaw):

    yaw = yaw - 1

    kit.servo[1].angle = yaw
    time.sleep(1)
    return(yaw)

def rot_ryaw(yaw):

    yaw = yaw + 1

    kit.servo[1].angle = yaw
    time.sleep(1)
    return(yaw)

def rot_upitch(pitch):

    pitch = pitch + 1

    kit.servo[4].angle = pitch
    time.sleep(1)
    return(pitch)

def rot_dpitch(pitch):

    pitch = pitch - 1

    kit.servo[4].angle = pitch
    time.sleep(1)
    return(pitch)

while True:

    pitch = 45
    yaw = 0

    global pitch
    global yaw

    initial_pos(pitch, yaw)

    if cpx.light > 0:
        time.sleep(60)
    else:
        random.choice(rot_lyaw(yaw),rot_ryaw(yaw),
            rot_dpitch(pitch),rot_upitch(pitch))
