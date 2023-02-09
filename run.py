import cv2
import time
from PIL import Image
import numpy as np

from pyrebase import pyrebase
from motor.firebase_secrets import SECRETS

import tensorflow as tf

from helper import run_motor, stop_motor

# Initialize FireBase DB.
firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

# Load the trained model
model = tf.keras.models.load_model("model/model_080223")
print("model loaded")


cap = cv2.VideoCapture(0)

while True:
        
        ret, frame = cap.read() 
        
        # Converting into RGB
        frame_array = Image.fromarray(frame, 'RGB')

        # Resizing
        frame_array = frame_array.resize((224,224))
        frame_array = np.array(frame_array)

        # 4-Dimensional Tensor
        frame_array = np.expand_dims(frame_array, axis=0)

        # Predict the class of the fruit
        pred = model.predict(frame_array)
    
        # Check if the prediction is 0 or 1
        if np.round(pred) == 1:
            cv2.putText(frame, "Rotten", (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
            # FireBase Updater function to run the motor
            run_motor(db)
            # ! Motor can't get variable fast on FireBase. Fix it!
            
            # TODO: Add Counter for rotten fruits.
            # TODO: Update the values of counted fruits on FireBase
        else:
            #cv2.putText(frame, "Fresh", (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
            
            # FireBase Updater function to stop the motor
            stop_motor(db)
                  
        cv2.imshow("Fresh & Rotten Fruit Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        

cap.release()
cv2.destroyAllWindows()
