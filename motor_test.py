from pyrebase import pyrebase
from firebase_secrets import SECRETS
import time

firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

data = {"run": True}
result = db.child("motor-control").child("CONTROL").update(data)
print(result)

time.sleep(3)
data = {"run": False}
result = db.child("motor-control").child("CONTROL").update(data)
print(result)
