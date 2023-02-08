import argparse
import sys
from pathlib import Path

import keras
import tensorflow as tf
from model.xception import XceptionModel
from model.vgg16 import VGG16

sys.path.append(str(Path.cwd()))

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Parameters of XceptionModel")
    
    parser.add_argument("--size", type=int, help="size of image")
    parser.add_argument("--num-class", type=int, help="number of class")
    parser.add_argument("--activation", type=str, help="activation function")
    parser.add_argument("--loss", type=str, help="loss function")
    parser.add_argument("--save-path", type=str, help="save path for the model")
    parser.add_argument("--batch", type=int, help="batch size")
    parser.add_argument("--stopping-patience", type=int, help="early stopping patience")
    parser.add_argument("--train-path", type=str, help="traning path")
    parser.add_argument("--test-path", type=str, help="test path")
    parser.add_argument("--save-model", type=str, help="saving path of model")
    parser.add_argument("--save-weights", type=str, help="saving path of weights")
    parser.add_argument("--epochs", type=int, help="epochs")
    args = parser.parse_args()    
    

config = {
    "size": args.size,
    "number_of_class": args.num_class,
    "activation": args.activation,
    "loss": args.loss,
    "save_path": args.save_path,
    "batch": args.batch,
    "stopping_patience": args.stopping_patience,
    "train_path": args.train_path,
    "test_path": args.test_path,
    "save_model": args.save_model,
    "save_weights": args.save_weights,
    "epochs": args.epochs,
}


model = XceptionModel(config)
model.create_model()
model.train_model()
hist = model.hist
model.save_model()

"""
# VGG16
model = VGG16(config)
model.create_model()
model.train_model()
hist = model.hist
"""