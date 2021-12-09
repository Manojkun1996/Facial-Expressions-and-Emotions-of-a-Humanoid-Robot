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

import time
import _thread

import time
import _thread
robot=Robot()
robot.connect()

mo_ro = command_list(
        motor(MotorId.eyelids, 0, 0.0),
        motor(MotorId.head_turn, 0.5, 0.0),
       
     )
eye_lid_close= command_list(    

    motor(MotorId.eyelids,1 , 0.5),
    wait_for_motors(),  # wait until previous motor command has finished
    wait(0.1),
    )


def the_test(name, wait):
   i = 0
   while i <= 10:
      time.sleep(wait)
      print("Running %s\n" %name)
      i = i + 1
      #robot.do(
         #mo_ro,
      
   print("%s has finished execution" %name)

def the_te(name, wait):
   i = 0
   while i <= 10:
      time.sleep(wait)
      print("Running %s\n" %name)
      i = i + 1
      #robot.do(
         #eye_lid_close,
        # )
   print("%s has finished execution" %name)

if __name__ == "__main__":
    
    _thread.start_new_thread(the_test, ("First Thread", 1))
    _thread.start_new_thread(the_te, ("Second Thread", 2))
   
