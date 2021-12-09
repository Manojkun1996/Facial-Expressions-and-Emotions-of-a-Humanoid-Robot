from hr_little_api.functional import say, motor, close_mouth, command_list, wait_for_motors_and_speaking, \
    head_turn_middle, neutral_eyebrows, frown_eyebrows, head_turn_right, head_turn_left, poke_tounge, wait, \
    raise_eyebrows, wait_for_motors, move_robot, eye_lid_close, eye_lid_open, reset_motors
from hr_little_api.robot import Robot, MotorId
from hr_little_api.robot import Robot, Animation
from hr_little_api.builders import MotorId
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List
from hr_little_api.builders import MotorCommandBuilder, SayCommandBuilder, \
    WalkCommandBuilder, MotorId, WalkDirection, WaitCommandBuilder, WaitType, CallbackCommandBuilder, CallbackType, \
    CommandListBuilder
from threading import Thread
from multiprocessing import Process
import time
import os

import _thread
import time
robot = Robot()
robot.connect()
# Define a function for the thread


def print_time(threadname, delay):

    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{}: {} : {}".format(threadname, time.ctime(time.time()), "This is from name function\n"))
      

def constant_thread(delay, x, y, z):
    count = 0
    while True:
        count += 1
        time.sleep(delay)
        robot.do(
           move_robot(x,y,z),
        )
def thread_function(delay,X):
   
    count = 0
    while count < X:
       try:
          x=input("motorid ")
          y=float(input("Enter the Motor position(0.0 -1.0) " ))
          z=float(input("Enter the time delay(0.0 -1.0))" ))
          count += 1
          time.sleep(delay)
          robot.do(
             move_robot(x,y,z),
             )
       except Exception as ex:
         print(type(ex).__name__, ex.args)
       
'''DUMMY FUNCTION - USE ORIGINAL 1'''
def move_robot(x,y,z) -> MotorCommandBuilder:
    """ Move Robot to the desired position

    """
    return command_list(
        #reset_motors(),
        motor(getattr(MotorId,x), y, z),
        #wait_for_motors(),  # wait until previous motor command has finished
    )


# Create two threads as follows
X = int(input("how many times you want to give command "))
print("lip_corners, eyebrows, eyelids ,head_pitch ,head_turn ,mouth")

x=input("motorid first thread ")
y=float(input("Enter the Motor position(0.0 -1.0)  first thread " ))
z=float(input("Enter the time delay(0.0 -1.0))  first thread " ))
#THREAD CALLING
try:
    _thread.start_new_thread( constant_thread, (1,x,y,z) )
    _thread.start_new_thread( thread_function, (2,X,) )
except Exception as ex:
   print(type(ex).__name__, ex.args)

while 1:
   pass
        

robot.disconnect()

   

