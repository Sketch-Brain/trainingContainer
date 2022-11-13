import logging

from app.trainWorker.model import create_model
from app.crud.containerCRUD import updateStatus
import tensorflow as tf
from app.trainWorker.sendRequest import sendResults, sendFiles

import numpy as np
import matplotlib.pyplot as plt

logger = logging.getLogger("trainer")


async def runMnistExperiment(db, userId, experiment_id, strExpId):
    #Load MNIST datasets
    try:
        fashion_mnist_dataset = tf.keras.datasets.fashion_mnist
        logger.info("run_trainings")
        (train_X,train_Y),(test_X,test_Y) = fashion_mnist_dataset.load_data()
        train_X, test_X = train_X / 255.0, test_X / 255.0

        train_X = train_X.reshape(-1, 28, 28, 1)
        test_X = test_X.reshape(-1, 28, 28, 1)

        # Created model load.
        model = await create_model()
        input_shape = (None,28,28,1)
        model.build(input_shape=input_shape)
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.summary()
        # Run MNIST training.
        history = model.fit(train_X, train_Y, epochs=1, validation_split=0.25, shuffle=True)

        loss, acc = model.evaluate(test_X, test_Y, verbose=0)
        acc = acc*100
        logger.info(f"acc : {acc}, loss : {loss}")
        await updateStatus(db=db, experiment_id=experiment_id,status="Finished")
        await sendResults(userId=userId, experimentId=strExpId, accuracy=acc)
        await sendFiles(userId=userId, experimentId=strExpId)
    except:
        import traceback
        traceback.print_exc()
        logger.info("Experiment error detected. Roll-back, Status Failed.")
        await updateStatus(db=db, experiment_id=experiment_id, status="Failed")