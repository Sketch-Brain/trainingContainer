from tensorflow.python.keras import layers
from tensorflow.python.keras import models

def create_model():
    # Created model source.
    # This is an examples.
    model = models.Sequential([
        layers.Conv2D(filters=16,strides=(1,1),padding="valid",use_bias=True,kernel_initializer="glorot_uniform",bias_initializer="zeros",kernel_size=(3,3)),
        layers.Conv2D(filters=32,strides=(1,1),padding="valid",use_bias=True,kernel_initializer="glorot_uniform",bias_initializer="zeros",kernel_size=(3,3)),
        layers.Conv2D(filters=64, strides=(1, 1), padding="valid", use_bias=True, kernel_initializer="glorot_uniform",
                      bias_initializer="zeros", kernel_size=(3, 3)),
        layers.Flatten(),
        layers.Dense(units=128, activation='relu'),
        layers.Dense(units=10, activation='softmax')
    ])

    return model