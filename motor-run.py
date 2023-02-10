from motor.motor import Motor
from pyrebase import pyrebase
from firebase_secrets import SECRETS

# Initialize FireBase
firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

# Get value of run (True of False) from FiraBase
run = db.child("motor-control").child("CONTROL").child("run").get().val()

# Define the DC-motor
motor = Motor(Ena=2, In1=3, In2=4)

while True:
    
    if run == True:
        print(run)
        motor.move_backward(speed=50, t=0.60)
        motor.stop()
        motor.move_forward(speed=50, t=0.48)
        motor.stop()
        break