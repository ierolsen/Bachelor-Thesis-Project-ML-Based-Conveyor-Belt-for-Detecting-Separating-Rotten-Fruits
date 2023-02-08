import cv2
import numpy as np

from pyrebase import pyrebase
from firebase_secrets import SECRETS

import tensorflow as tf

# Initialize FireBase DB.
firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

# Load the trained model
model = tf.keras.models.load_model("model/model_080223")
print("model loaded")


cap = cv2.VideoCapture(0)

while True:
        
        ret, frame = cap.read() 
                        
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        """
        TODO:
        -> Add prediction function here.
            
        NOTE Here is the code:
            pred = model.predict(frame)
            if pred <= 0.5:
                print("Fresh")

            else:
                print("Rotten")
            ----------------------------------------------
        -> According to the result, update FireBase DB.
            
        NOTE Here is the code:
            data = {"open": True,
                    "close": False}
            result = db.child("motor-control").child("CONTROL").update(data)
            print(result)

            data = {"open": False,
                    "close": True}
            result = db.child("motor-control").child("CONTROL").update(data)
            print(result)
            ----------------------------------------------
        -> cv2.putText  label of the result to the frame
        """
        
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        

cap.release()
cv2.destroyAllWindows()
