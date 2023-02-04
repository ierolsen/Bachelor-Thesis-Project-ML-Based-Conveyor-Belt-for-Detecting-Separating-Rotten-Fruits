import cv2

from pyrebase import pyrebase
from firebase_secrets import SECRETS

firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

"""
data = {"open": True,
        "close": False}
result = db.child("motor-control").child("CONTROL").update(data)
print(result)

time.sleep(3)
data = {"open": False,
        "close": True}
result = db.child("motor-control").child("CONTROL").update(data)
print(result)
"""

#model = Xception(weights="model/model.h5")
#model.summary()

#model = Model.load_weights(filepath="model/model.hdf5")
#model = load_model(filepath="model/model.h5")
#model.summary()


cap = cv2.VideoCapture(0)

while True:
        
        ret, frame = cap.read()
        
        if ret == False:
                break
                        
        cv2.imshow("Video Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
cap.release()
cv2.destroyAllWindows()