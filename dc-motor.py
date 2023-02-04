from motor.motor import Motor

motor = Motor(Ena=2, In1=3, In2=4)

while True:
    motor.move_forward(speed=30, t=2)
    motor.stop()
    motor.move_backward(speed=70, t=2)
    motor.stop()
    
