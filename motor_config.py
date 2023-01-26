from pyrebase import pyrebase
from firebase_secrets import SECRETS

firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()
db.child("motor-config")

data = {
    "STEPPER_MOTOR":{
        
        "RIGHT": {
            "clockwise": True,
            "steptype": "Full",
            "steps": 250,
            "stepdelay": int(8)*.0004,
            "verbose": False,
            "initdelay": .05
        },
        
        "LEFT":{
            "clockwise": False,
            "steptype": "Full" ,
            "steps": 250,
            "stepdelay": int(8)*.0004,
            "verbose": False,
            "initdelay": .05
            }
    }
    }

# RUN IT ONCE, IT CREATES TABLE ON FIREBASE
#db.set(data)

#FOR UPDATING THE DATA
db.update(data)