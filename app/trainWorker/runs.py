import logging

from app.trainWorker.model import create_model
import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

logger = logging.getLogger("trainer")

async def runMnistExperiment(userId):
    #Load MNIST datasets
    mnist_dataset = tf.keras.datasets.mnist
    logger.info("run_trainings")
    (train_X,train_Y),(test_X,test_Y) = mnist_dataset.load_data()
    train_X, test_X = train_X / 255.0, test_X / 255.0

    train_X = train_X.reshape(-1, 28, 28, 1)
    test_X = test_X.reshape(-1, 28, 28, 1)

    # Created model load.
    model = create_model()
    input_shape = (None,28,28,1)
    model.build(input_shape=input_shape)
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.summary()
    # Run MNIST training.
    history = model.fit(train_X, train_Y, epochs=30, validation_split=0.25)
