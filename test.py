from hr_little_api.robot import Robot

robot = Robot()
robot.connect()

text = input("Enter your sentence: ")

print (robot.say(text))

from hr_little_api.robot import Animation

robot.animate(Animation.poke_tounge)
robot.animate(Animation.right_arm_point)
robot.animate(Animation.sleep)
robot.animate(Animation.wake_up)

from hr_little_api.functional import say, go_crazy, poke_tounge, right_arm_point, walk_forward
from hr_little_api.functional import say, motor, close_mouth, command_list, wait_for_motors_and_speaking, \
    head_turn_middle, neutral_eyebrows, frown_eyebrows, head_turn_right, head_turn_left, poke_tounge, wait, \
    raise_eyebrows, wait_for_motors
from hr_little_api.robot import Robot, MotorId


robot.do(
    raise_eyebrows(),
    head_turn_left(),
    wait_for_motors(),
    wait(0.2),

    frown_eyebrows(),
    head_turn_right(),
    wait_for_motors(),
    wait(0.3),

     go_crazy(),

     poke_tounge(),

)
