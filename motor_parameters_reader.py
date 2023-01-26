from pyrebase import pyrebase
from firebase_secrets import SECRETS

firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

#CW
cw_clockwise = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("RIGHT").child("clockwise").get().val()

cw_steptype = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("RIGHT").child("steptype").get().val()

cw_steps = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("RIGHT").child("steps").get().val()

cw_stepdelay = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("RIGHT").child("stepdelay").get().val()

cw_verbose = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("RIGHT").child("verbose").get().val()

cw_initdelay = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("RIGHT").child("initdelay").get().val()
#############################

#CCW
ccw_clockwise = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("LEFT").child("clockwise").get().val()

ccw_steptype = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("LEFT").child("steptype").get().val()

ccw_steps = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("LEFT").child("steps").get().val()

ccw_stepdelay = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("LEFT").child("stepdelay").get().val()

ccw_verbose = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("LEFT").child("verbose").get().val()

ccw_initdelay = db.child("motor-config").child("STEPPER_MOTOR_PARAMETERS").child("LEFT").child("initdelay").get().val()
#############################