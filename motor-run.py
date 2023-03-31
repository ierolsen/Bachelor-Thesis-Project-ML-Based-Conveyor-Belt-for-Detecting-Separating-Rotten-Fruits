from motor.motor import Motor
from pyrebase import pyrebase
from firebase_secrets import SECRETS

# Initialize FireBase
firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

# Define motor
motor = Motor(Ena=2, In1=3, In2=4)

while True:
    
    # Get value of run (True of False)
    run = db.child("motor-control").child("CONTROL").child("run").get().val()
    
    if run == True:
        motor.move_forward(speed=100, t=.8)
        motor.stop(.5)
        motor.move_forward(speed=100, t=.2)
        motor.move_backward(speed=100, t=1.05)
        motor.stop()
        
    else:
        continue