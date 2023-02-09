from pyrebase import pyrebase
from motor.firebase_secrets import SECRETS


# Initialize FireBase DB.
firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()


def run_motor(db):
    """
    FireBase DataBase updater. It will run when a rotten fruit is detected. 
    It will cause DC-Motor run.
    Args:
        db: FireBase DataBase
    """
    data = {"run": True}
    db.child("motor-control").child("CONTROL").update(data)    

def stop_motor(db):
    """
    FireBase DataBase updater.
    It will stop to DC-Motor run.
    Args:
        db: FireBase DataBase
    """
    data = {"run": False}
    db.child("motor-control").child("CONTROL").update(data)

def count_rottens(db):
    pass