"""
Author: Sylvain Verdy
Contact: sylvain.verdy.pro@gmail.com
"""

import tensorflow as tf

from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras import Model


class CNN(Model):
    def __init__(self):
        super(CNN,self).__init__()
        self.conv1 = Conv2D(32,3, activation="relu", input_shape=(32,32,3))
        self.maxpool1 = MaxPooling2D((2,2))
        self.conv2 = Conv2D(64, 3, activation="relu")
        self.flatten = Flatten()
        self.dense1 = Dense(128, activation = "relu")
        self.dense2 = Dense(10)
    
    def call(self, x):
        x = self.conv1(x)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.flatten(x)
        x = self.dense1(x)
        return self.dense2(x)


