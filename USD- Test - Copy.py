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

# Define a function for the thread

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("{}: {} : {}".format( threadName, time.ctime(time.time()),"This is from name function\n"))

mo_ro = command_list(
        motor(MotorId.eyelids, 0, 0.0),
        motor(MotorId.head_turn, 0.5, 0.0),
        )
eyelid_close = command_list(
        motor(MotorId.eyelids, 1, 0.0),
        )
      
def constant_thread(delay,):
    count = 0
    while True:
        count += 1
        time.sleep(delay)
        #robot.do
        mo_ro,
        
def thread_function(delay,X):
   
    count = 0
    while count < X:
       try:
          x=input("motorid ")
          y=float(input("Enter the Motor position(0.0 -1.0) " ))
          z=float(input("Enter the time delay(0.0 -1.0))" ))
          count += 1
          time.sleep(delay)
          #robot.do
          move_robot(x,y,z)
       except Exception as ex:
         print(type(ex).__name__, ex.args)
#THREAD CALLING
try:
    _thread.start_new_thread( constant_thread, (1,x,y,z) )
    _thread.start_new_thread( thread_function, (2,X,) )
except Exception as ex:
   print(type(ex).__name__, ex.args)

while 1:
   pass
        



   

