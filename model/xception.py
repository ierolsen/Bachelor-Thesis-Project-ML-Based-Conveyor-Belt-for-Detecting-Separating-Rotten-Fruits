from keras.models import Sequential
from keras.layers import Dense, Flatten, GlobalAveragePooling2D, Activation, Flatten, Dropout, BatchNormalization
from keras.applications.xception import Xception
from keras.applications.xception import preprocess_input
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from pathlib import Path
import numpy as np


class XceptionModel(object):

    def __init__(self, config):
        self.config = config
        self.model = None
        self.hist = None

    def create_model(self):
        size = self.config.get("size")
 
        model = Sequential()
        model.add(Xception(include_top=False, pooling='avg', weights="imagenet", input_shape=(size, size, 3)))
        model.add(Dense(512))
        model.add(Dropout(0.4))
        model.add(Dense(128))
        model.add(Dropout(0.4))
        model.add(Dense(64))
        model.add(Dropout(0.4))
        model.add(Dense(self.config.get("number_of_class"), activation='softmax'))
        model.layers[0].trainable=False

        model.compile(optimizer=Adam(lr=self.config.get("lr")), 
                      loss='sparse_categorical_crossentropy', 
                      metrics=['accuracy'])

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
                                     monitor='val_loss', 
                                     mode='min', 
                                     save_weights_only=True, 
                                     save_best_only=True, 
                                     verbose=1)

        batch = self.config.get("batch")
        size = self.config.get("size")

        datagen = ImageDataGenerator(preprocessing_function=preprocess_input,
                                     rescale=1./255.,
                                     shear_range=0.2,
                                     zoom_range=0.2, 
                                     horizontal_flip=True,
                                     rotation_range=45,
                                     validation_split=0.3)
        
        train_datagen = datagen.flow_from_directory(directory=self.config.get("train_path"),
                                                    target_size=(size,size),
                                                    color_mode='rgb',
                                                    batch_size=batch,
                                                    class_mode='sparse',
                                                    shuffle=True,
                                                    subset='training')

        valid_datagen = datagen.flow_from_directory(directory=self.config.get("train_path"),
                                                    target_size=(size,size),
                                                    color_mode='rgb',
                                                    batch_size=batch,
                                                    class_mode='sparse',
                                                    shuffle=True,
                                                    subset='validation')

        test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input,
                                          rescale=1./255.)

        test_datagen = test_datagen.flow_from_directory(directory=self.config.get("test_path"),
                                                        target_size=(size,size),
                                                        color_mode='rgb',
                                                        batch_size=batch,
                                                        class_mode='sparse')

        hist = self.model.fit_generator(generator=train_datagen,
                                        steps_per_epoch=train_datagen.n // batch,
                                        epochs=self.config.get("epochs"),
                                        validation_data=valid_datagen,
                                        validation_steps=valid_datagen.n // batch,
                                        verbose=1, 
                                        callbacks=[checkpoint, early_stop, reduce_lr])

        self.hist = hist