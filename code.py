import binascii #imports the necessary libraries
import board
import busio
import digitalio
import time
import pwmio

from dabble import Dabble

dabble = Dabble(board.GP0, board.GP1, debug=True) # defines hardware and assigns to

from adafruit_motor import motor #Imports a function from the adafruit_motor libraryf


left_motor_forward = board.GP15 #Initializes the variable left_motor_forward and attaches it to GP.12
left_motor_backward = board.GP7 #Initializes the variable left_motor_backward and attaches it to GP.12
right_motor_forward = board.GP6
right_motor_backward = board.GP8

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) # tells the hat the motor is an output
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Lc = pwmio.PWMOut(right_motor_backward , frequency=10000)
pwm_Ld = pwmio.PWMOut(right_motor_forward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) # Configuration line(it's required)
Left_Motor_speed = 0 # intiates the variable for the left motor and it starts at 0
Right_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
Right_Motor_speed = 0

def backward():
    Left_Motor_speed = .7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed= .7
    Right_Motor.throttle = Right_Motor_speed
def stop():
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed= 0
    Right_Motor.throttle = Right_Motor_speed
def foward():
    Left_Motor_speed = -.7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed= -.7
    Right_Motor.throttle = Right_Motor_speed
def right():
    Left_Motor_speed = .7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed= -.7
    Right_Motor.throttle = Right_Motor_speed
def left():
    Left_Motor_speed = -.7
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed= .7
    Right_Motor.throttle = Right_Motor_speed



while True:
    message = dabble.read_message()
    if (message != None):
        #print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            backward()
            print("Move both motors forward")
        elif (message.down_arrow_pressed):
            foward()
            print("Move both motors backward")
        elif (message.right_arrow_pressed):
            right()
            print("Move left motor forward and right motor backward")
        elif (message.left_arrow_pressed):
            left()
            print("Move left motor backward and right motor forward")
        elif (message.no_direction_pressed):
            print("Stop both motors")
            stop()
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise arm")
        elif (message.circle_pressed):
            print("Lower arm")
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        #elif (message.no_action_pressed):
        #    print("No action")
        #else:
        #    print("Something crazy happened with action!")
