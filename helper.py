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

def get_contour(frame):
    blur = cv2.medianBlur(src=frame, ksize=3)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    _, thresholded_video = cv2.threshold(src=gray, thresh=70, maxval=255, type=cv2.THRESH_BINARY_INV)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(thresholded_video, cv2.MORPH_OPEN, kernel=kernel, iterations=7)
    sure_bg = cv2.dilate(opening, kernel, iterations=1)
    dist_transform = cv2.distanceTransform(src=sure_bg, distanceType=cv2.DIST_L2, maskSize=3)
    ret2, sure_fg = cv2.threshold(dist_transform, 0.2 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret3, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 10
    markers[unknown == 255] = 0
    markers = cv2.watershed(frame, markers)
    frame[markers == -1] = [0, 255, 255]
    _, contour, hierarchy = cv2.findContours(image=markers.copy(), mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)
    return contour, hierarchy

def getMouseCoordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print the x,y coordinates of the point clicked
        print(f"Coordinates: ({x}, {y})")


cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')

# Click desired points and get coordinates
#cv2.setMouseCallback('frame', getMouseCoordinates) 


while True:

    ret, frame = cap.read()
 
    #draw_borderline(frame, pt1=(150, 0), pt2=(466, 0), pt3=(0, 480), pt4=(640, 480))
    
    contour, hierarchy = get_contour(frame)
    
    for cnt in contour:

            (x, y, w, h) = cv2.boundingRect(cnt)
            area = cv2.contourArea(cnt)

            if area > 100:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 1)
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Release the camera and destroy the windows
cap.release()
cv2.destroyAllWindows()
