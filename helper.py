import cv2
import numpy as np

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

def getMouseCoordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print the x,y coordinates of the point clicked
        print(f"Coordinates: ({x}, {y})")

rect_points = np.array([[(145, 10), (145, 105), (472, 105), (472, 10)]])

"""
cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', getMouseCoordinates)


while True:

    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Release the camera and destroy the windows
cap.release()
cv2.destroyAllWindows()
"""