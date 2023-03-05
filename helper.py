import cv2
from PIL import Image, ImageDraw, ImageFont
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

def update_rottens(db, value):
    """
    Updater of Rotten Fruit Numbers.
    Args:
        db: FireBase DataBase
        value (int): 0 (0 is for beginning)
    """
    data = {"num_rotten": value}
    db.child("motor-control").child("CONTROL").update(data)

def update_fresh(db, value):
    """
    Updater of Fresh Fruit Numbers.
    Args:
        db: FireBase DataBase
        value (int): 0 (0 is for beginning)
    """
    data = {"num_fresh": value}
    db.child("motor-control").child("CONTROL").update(data)

def reset_db(db):
    """
    This function resets FireBase. 
    It should work when the code stops.

    Args:
        db : FiraBase DataBase
    """
    data = {"num_rotten": 0,
            "num_fresh": 0, 
            "run": False}
    db.child("motor-control").child("CONTROL").update(data)
    

def draw_borderline(frame, pt1, pt2, pt3, pt4, color=(0, 255, 0), thickness=2):
    """
    pt1-------pt2
    |         |
    |         |
    |         |
    |         |
    |         |
    pt3-------pt4
    (150, 0) -> pt1
    (466, 0) -> pt2
    (0, 480) -> pt3
    (640, 480) -> pt4
    """
    cv2.line(frame, pt1, pt2, color, thickness)
    cv2.polylines(frame, [np.array([[pt1[0], pt1[1]], 
                                    [pt3[0], pt3[1]]])], True, color, thickness)
        
    cv2.polylines(frame, [np.array([[pt2[0], pt2[1]], 
                                    [pt4[0], pt4[1]]])], True, color, thickness)
    cv2.line(frame, pt3, pt4, color, thickness)

def getMouseCoordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print the x,y coordinates of the point clicked
        print(f"Coordinates: ({x}, {y})")

"""
cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')

# Click desired points and get coordinates
#cv2.setMouseCallback('frame', getMouseCoordinates) 


while True:

    ret, frame = cap.read()
 
    #draw_borderline(frame, pt1=(150, 0), pt2=(466, 0), pt3=(0, 480), pt4=(640, 480))
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Release the camera and destroy the windows
cap.release()
cv2.destroyAllWindows()
"""