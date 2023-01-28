from pyrebase import pyrebase
from firebase_secrets import SECRETS

firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

"""
    detected": 0,
    "num_rotten": 0,
    "num_fresh": 0,
    "open": False,
    "close": True,
"""

detected = db.child("motor-control").child("CONTROL").child("detected").get().val()
num_rotten = db.child("motor-control").child("CONTROL").child("num_rotten").get().val()
num_fresh = db.child("motor-control").child("CONTROL").child("num_fresh").get().val()
opening = db.child("motor-control").child("CONTROL").child("open").get().val()
closing = db.child("motor-control").child("CONTROL").child("close").get().val()