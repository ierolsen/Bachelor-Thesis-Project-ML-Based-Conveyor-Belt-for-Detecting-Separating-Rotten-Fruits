import cv2

#from pyrebase import pyrebase
#from firebase_secrets import SECRETS

import keras
import tensorflow as tf

#firebase = pyrebase.initialize_app(SECRETS["FIREBASE"])
#db = firebase.database()

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

"""
def binary_accuracy(y_true, y_pred):
    return keras.metrics.binary_accuracy(y_true, tf.round(y_pred))

dependencies = {
    'binary_accuracy': binary_accuracy,
    'config': {'name': binary_accuracy, 
               'dtype':'float32', 
               'threshold': 0.5}
}

model = keras.models.load_model("model/model_060223.h5", custom_objects=dependencies)
"""

import tensorflow as tf

class BinaryAccuracy(tf.keras.metrics.Metric):
    def __init__(self, name='binary_accuracy', dtype=tf.float32, threshold=0.5, **kwargs):
        super(BinaryAccuracy, self).__init__(name=name, dtype=dtype, **kwargs)
        self.threshold = threshold
        self.accuracy = self.add_weight(name='accuracy', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.where(y_pred > self.threshold, 1, 0)
        values = tf.math.equal(y_true, y_pred)
        values = tf.cast(values, self.dtype)
        if sample_weight is not None:
            sample_weight = tf.cast(sample_weight, self.dtype)
            sample_weight = tf.convert_to_tensor(sample_weight)
            values = tf.multiply(values, sample_weight)
        self.accuracy.assign_add(tf.reduce_mean(values))

    def result(self):
        return self.accuracy

    def get_config(self):
        config = {
            'threshold': self.threshold,
            'dtype': str(self.dtype),
        }
        base_config = super(BinaryAccuracy, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

dependencies = {
    'BinaryAccuracy': BinaryAccuracy
}

model = keras.models.load_model("model/model_060223.h5", custom_objects=dependencies)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

#model.summary()

cap = cv2.VideoCapture(0)

while True:
        
        ret, frame = cap.read()
        
        if ret == False:
                break
        
        """
        TODO:
        Prediction function will come here. 
        -> The frame will be predicted by the trained model.
        -> According to the result, FireBase variables will change
        -> DC-Motor will run by the value of the variables on FireBase
        """
                        
        cv2.imshow("Video Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
cap.release()
cv2.destroyAllWindows()
