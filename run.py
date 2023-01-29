from pyrebase import pyrebase
from firebase_secrets import SECRETS

import time

firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()


data = {"open": True,
        "close": False}
result = db.child("motor-control").child("CONTROL").update(data)
print(result)

time.sleep(3)
data = {"open": False,
        "close": True}
result = db.child("motor-control").child("CONTROL").update(data)
print(result)