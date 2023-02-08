import cv2
from PIL import Image
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

# TODO:
# Define a function here which updates the values on FiraBase. 
# It will take place inside the loop.
# According to the values on DB, DC-Motor will run.


cap = cv2.VideoCapture(0)

while True:
        
        ret, frame = cap.read() 
        
        # Converting into RGB
        im = Image.fromarray(frame, 'RGB')

        # Resizing
        im = im.resize((224,224))
        img_array = np.array(im)

        # 4-dimensional tensor
        img_array = np.expand_dims(img_array, axis=0)

        # Predict the class of the fruit
        pred = model.predict(img_array)
    
        # Check if the prediction is 0 or 1
        if np.round(pred) == 1:
            cv2.putText(frame, "Rotten", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Fresh", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
     
        """
        TODO:
        Update the values on DB.  
        NOTE Here is the code:
            data = {"open": True,
                    "close": False}
            result = db.child("motor-control").child("CONTROL").update(data)
            print(result)

            data = {"open": False,
                    "close": True}
            result = db.child("motor-control").child("CONTROL").update(data)
            print(result)
        """
        
        cv2.imshow("Fresh & Rotten Fruit Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        

cap.release()
cv2.destroyAllWindows()
