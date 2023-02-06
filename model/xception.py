import keras
from keras.layers import Dense, GlobalAveragePooling2D
from keras.applications.xception import Xception
from keras.models import Model, save_model
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from pathlib import Path


class XceptionModel(object):

    def __init__(self, config):
        self.config = config
        self.model = None
        self.hist = None

    def create_model(self):
        size = self.config.get("size")

        base_model = Xception(include_top=False, weights="imagenet", input_shape=(size, size, 3))

        x = GlobalAveragePooling2D()(base_model.output)
        predictions = Dense(self.config.get("number_of_class"), activation=self.config.get("activation"))(x)

        model = Model(inputs=base_model.input, outputs=[predictions])

        model.compile(optimizer=keras.optimizers.Adam(),
                      loss=self.config.get("loss"), 
                      metrics=[keras.metrics.BinaryAccuracy()])

        self.model = model

    def train_model(self):
        Path(self.config.get("save_path")).parent.mkdir(parents=True, exist_ok=True)

        reduce_lr = ReduceLROnPlateau(monitor='val_loss',
                                      factor=0.1,
                                      patience=3,
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

        datagen = ImageDataGenerator(samplewise_center=True,
                                     rotation_range=10,
                                     zoom_range=0.1,
                                     width_shift_range=0.1,
                                     height_shift_range=0.1,
                                     horizontal_flip=True,
                                     vertical_flip=True,
                                     validation_split=0.3)

        train_datagen = datagen.flow_from_directory(directory=self.config.get("train_path"),
                                                    target_size=(size,size),
                                                    color_mode='rgb',
                                                    batch_size=batch,
                                                    class_mode="binary",
                                                    shuffle=True,
                                                    subset='training')

        valid_datagen = datagen.flow_from_directory(directory=self.config.get("train_path"),
                                                    target_size=(size,size),
                                                    color_mode='rgb',
                                                    batch_size=batch,
                                                    class_mode="binary",
                                                    shuffle=True,
                                                    subset='validation')

        test_datagen = ImageDataGenerator(rescale=1./255.)

        test_datagen = test_datagen.flow_from_directory(directory=self.config.get("test_path"),
                                                        target_size=(size,size),
                                                        color_mode='rgb',
                                                        batch_size=batch,
                                                        class_mode='binary')

        hist = self.model.fit_generator(generator=train_datagen,
                                        steps_per_epoch=train_datagen.n // batch,
                                        epochs=self.config.get("epochs"),
                                        validation_data=valid_datagen,
                                        validation_steps=valid_datagen.n // batch,
                                        verbose=1, 
                                        callbacks=[checkpoint, early_stop])

        self.hist = hist

    def save_model(self):
        self.model.save(self.config.get("save_model"))
        print(f"model saved there: {self.config.get('save_model')}")

        self.model.save_weights(self.config.get("save_weights"))
        print(f"weights saved there: {self.config.get('save_weights')}")