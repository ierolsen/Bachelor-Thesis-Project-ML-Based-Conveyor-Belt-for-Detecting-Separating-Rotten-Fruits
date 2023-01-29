from pyrebase import pyrebase
from firebase_secrets import SECRETS

firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()
db.child("motor-control")

data = {
    "CONTROL":{
        "detected": 0,
        "num_rotten": 0,
        "num_fresh": 0,
        "open": False,
        "close": True,
    }
}

# RUN IT ONCE, IT CREATES TABLE ON FIREBASE
db.set(data)

#FOR UPDATING THE DATA
#db.update(data)

#FOR DELETING A VALUE
# e.g. : db.child("CONTROL").child("DETECTED").remove()