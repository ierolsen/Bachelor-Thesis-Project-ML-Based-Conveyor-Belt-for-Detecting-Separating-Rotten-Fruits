from keras.optimizers import Adam
from keras.applications.xception import Xception
from keras import Model, layers
from keras.losses import CategoricalCrossentropy
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
from keras.metrics import AUC
from pathlib import Path
import numpy as np
import cv2

class XceptionModel(object):
    
    def __init__(self, config):
        self.config = config
        self.model = model
        self.hist = hist
        
    def create_model(self):
        size = self.config.get("size")
        number_of_class = self.config.get("number_of_class")
        
        base_model = Xception(include_top=False, weights="imagenet", input_shape=(size, size, 3))
        x = layers.Flatten()(base_model.output)
        x = layers.Dense(1024)(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dense(512)(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dense(128)(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dense(64)(x)
        x = layers.BatchNormalization()(x)
        predictions = layers.Dense(number_of_class, activation="softmax")(x)
        
        model = Model(inputs=base_model.input, outputs=[predictions])
        
        loss = CategoricalCrossentropy(label_smoothing=self.config.get("label_smoothing"))
        
        model.compile(loss=loss, 
                      optimizer=Adam(lr=self.config.get("lr")), 
                      metrics=["accuracy"])
        
        self.model = model
        
    
    def train_model(self):
        Path(self.config.get("save_path")).parent.mkdir(parents=True, exist_ok=True)
        
        reduce_lr = ReduceLROnPlateau(monitor='val_loss',
                                      factor=0.1,
                                      patience=2,
                                      min_lr=1e-14,
                                      verbose=1)

        early_stop = EarlyStopping(monitor='val_loss', 
                                   patience=self.config.get("stopping_patience"), 
                                   verbose=1,
                                   restore_best_weights=True)

        checkpoint = ModelCheckpoint(filepath=self.config.get("save_path"), 
                                     monitor='val_loss', mode='min', 
                                     save_weights_only=True, 
                                     save_best_only=True, 
                                     verbose=1)
              
        batch = self.config.get("batch")
        
        datagen = ImageDataGenerator(rescale=1./255,
                                     shear_range=0.2,
                                     zoom_range=0.2,
                                     horizontal_flip=True,
                                     rotation_range=45,
                                     validation_split=0.3)
        
        size = self.config.get("size")
        train_datagen = datagen.flow_from_directory(directory=self.config.get("train_path"),
                            target_size = (size,size),
                            color_mode='rgb',
                            batch_size=batch,
                            class_mode = 'sparse',
                            subset='training')
        
        valid_datagen = datagen.flow_from_directory(directory=self.config.get("test_path"),
                                                   target_size = (size,size),
                                                   color_mode='rgb',
                                                   batch_size=batch,
                                                   class_mode='sparse',
                                                   subset='validation')
        
        hist = self.model.fit_generator(train_datagen,
                                        steps_per_epoch=train_datagen.n//batch,
                                        epochs=self.config.get("epochs"),
                                        validation_data=valid_datagen,
                                        validation_steps=valid_datagen.n//batch,
                                        verbose=1,
                                        callbacks=[reduce_lr, early_stop, checkpoint])

        self.hist = hist

