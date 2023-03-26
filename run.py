import cv2
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np

from pyrebase import pyrebase
from motor.firebase_secrets import SECRETS

import tensorflow as tf

from helper import run_motor, stop_motor, update_rottens, update_fresh, reset_db

# Initialize FireBase DB.
firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
db = firebase.database()

# Load the trained model
model = tf.keras.models.load_model("model/model_080223")
print("model loaded")

# Set the threshold values for each class
FRESH_THRESHOLD = 0.3
ROTTEN_THRESHOLD = 0.5

# Set values for counting
rotten_value = 0
fresh_value = 0

### CUSTOM FONT SETTINGS ###
FONT_PATH = 'fonts/NotoSans-Black.ttf'
FONT_SIZE = 32
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
############################

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
    prediction = model.predict(frame_array)
    
    #print(prediction)

    # Classify the frame based on the thresholds
    if prediction >= ROTTEN_THRESHOLD:        
        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil)
        draw.rectangle(((8, 50), (140, 100)), fill=(0, 0, 255))
        draw.text((10, 50), "ROTTEN", font=font, fill=(255, 255, 255))
        frame = np.array(img_pil)

        # FireBase Updater function to run the motor
        run_motor(db)

        # Number of Rotten Fruits updater on FiraBase
        rotten_value += 1
        update_rottens(db, rotten_value)
        
        # FireBase Updater function to stop the motor
        stop_motor(db)
        
    elif prediction >= FRESH_THRESHOLD:       
        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil)
        draw.rectangle(((8, 50), (110, 100)), fill="green")
        draw.text((10, 50), "FRESH", font=font, fill=(255, 255, 255))
        frame = np.array(img_pil)
        
        # Number of Fresh Fruits updater on FiraBase
        fresh_value += 1
        update_fresh(db, fresh_value)

    else:
        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil)
        draw.rectangle(((8, 50), (170, 100)), fill=(0,165,255))
        draw.text((10, 50), "NO FRUIT", font=font, fill=(255, 255, 255))
        frame = np.array(img_pil)
        
        
    # Show the frame
    cv2.imshow("Fresh & Rotten Fruit Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

# Reset DataBase
reset_db(db)
print("DataBase Reseted!")