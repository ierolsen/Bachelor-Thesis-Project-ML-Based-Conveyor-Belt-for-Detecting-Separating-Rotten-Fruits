from time import sleep
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

import motor_parameters_reader as mpr # containes motor parameters
import motor_control_reader as mcr # contains the values for opening and closing the stepper motor

#define motor1
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
motor1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


if __name__ == "__main__":
    
    while True:

        if mcr.opening == True and mcr.closing==False:
            
            motor1.motor_go(clockwise=mpr.cw_clockwise,
                            steptype=mpr.cw_steptype,
                            steps=mpr.cw_steps,
                            stepdelay=mpr.cw_stepdelay,
                            verbose=mpr.cw_verbose,
                            initdelay=mpr.cw_initdelay)
            
            motor1.motor_go(clockwise=mpr.ccw_clockwise,
                            steptype=mpr.ccw_steptype,
                            steps=mpr.ccw_steps,
                            stepdelay=mpr.ccw_stepdelay,
                            verbose=mpr.ccw_verbose,
                            initdelay=mpr.ccw_initdelay)