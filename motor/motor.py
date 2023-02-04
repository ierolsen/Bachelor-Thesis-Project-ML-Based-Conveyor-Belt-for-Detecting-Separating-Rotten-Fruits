import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor():
    def __init__(self, Ena, In1, In2):
        """
        Pins of Raspberry Pi
        Args:
            Ena (int): Enable
            In1 (int): Input 1
            In2 (int): Input 2
        """
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.Ena,100) # frequency: 100
        self.pwm.start(0)
        
    def move_forward(self, speed=50, t=1):
        """
        This function is for running to motor forward. Contains parameters of DC-Motor. 
        Args:
            speed (int, optional): Speed of the motor 0-100. Defaults to 50.
            t (int, optional): Time for running the motor. Defaults to 1.
        """
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed) # speed%
        sleep(t)

    def move_backward(self, speed=50, t=1):
        """
        This function is for running to motor backward. Contains parameters of DC-Motor. 
        Args:
            speed (int, optional): Speed of the motor 0-100. Defaults to 50.
            t (int, optional): Time for running the motor. Defaults to 1.
        """
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed) # speed%
        sleep(t)
        
    def stop(self, t=0):
        """
        It is a function for stopping the motor.
        pwm.ChangeDutyCycle() must get 0 for stopping.

        Args:
            t (int, optional): time. Defaults to 0.
        """
        self.pwm.ChangeDutyCycle(0)
        sleep(t)

