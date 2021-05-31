#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Mon 31 May 2021
# Author: Espinasse Rémi
# Description: Solarius project step 1
# Python Version 3.6

import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)

def initial_pos():

    kit.servo[4].angle = pitch
    time.sleep(1)
    kit.servo[1].angle = yaw
    time.sleep(1)
    return(pitch, yaw)

def forward(pitch, yaw):

    pitch = pitch + 1
    yaw = yaw + 2

    kit.servo[4].angle = pitch
    time.sleep(1)
    kit.servo[1].angle = yaw
    time.sleep(1)
    return(pitch, yaw)

def reverse(pitch, yaw):

    pitch = pitch - 1
    yaw = yaw + 2

    kit.servo[4].angle = pitch
    time.sleep(1)
    kit.servo[1].angle = yaw
    time.sleep(1)

while True:

    pitch = 45
    yaw = 0

    global pitch
    global yaw

    initial_pos(pitch, yaw)
    while pitch <= 90:
        forward(pitch, yaw)
    while yaw <= 180:
        reverse(pitch, yaw)

    print("END OF THE TEST")

    try_again = str(input("Do you want to try again? Y/N\t"))

    if try_again == "N":
        print("END")
        break
