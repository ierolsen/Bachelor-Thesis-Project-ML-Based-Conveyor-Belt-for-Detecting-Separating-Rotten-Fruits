from time import sleep
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

import parameters_base # containes motor parameters
import control_parameters # contains the values for opening and closing the stepper motor

#define motor1
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
motor1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

motor1.motor_go(clockwise=parameters_base.cw_clockwise,
                steptype=parameters_base.cw_steptype,
                steps=parameters_base.cw_steps,
                stepdelay=parameters_base.cw_stepdelay,
                verbose=parameters_base.cw_verbose,
                initdelay=parameters_base.cw_initdelay)

motor1.motor_go(clockwise=parameters_base.ccw_clockwise,
                steptype=parameters_base.ccw_steptype,
                steps=parameters_base.ccw_steps,
                stepdelay=parameters_base.ccw_stepdelay,
                verbose=parameters_base.ccw_verbose,
                initdelay=parameters_base.ccw_initdelay)
