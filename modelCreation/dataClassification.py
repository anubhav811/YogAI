from scipy import stats
from keras.callbacks import ModelCheckpoint
import itertools
from sklearn.metrics import confusion_matrix
import numpy as np
from keras.optimizers import Adam
from keras.layers.wrappers import TimeDistributed
from keras.layers import Conv1D, MaxPooling1D, LSTM
from keras.layers.pooling import GlobalAveragePooling1D
from keras.layers import Dense, Dropout, Flatten, BatchNormalization
from keras.models import Sequential
import keras
import matplotlib.pyplot as plt

XchTrain = np.load("trainX.npy")
YTrain = np.load("trainY.npy")
XchVal = np.load("valX.npy")
YVal = np.load("valY.npy")
XchTest = np.load("testX.npy")
YTest = np.load("testY.npy")
# making test and train labels one hot
YintTrain = np.int64(YTrain)
YhotTrain = np.zeros((YTrain.shape[0], 6))
YhotTrain[np.arange(YTrain.shape[0]), YintTrain] = 1

YintTest = np.int64(YTest)
YhotTest = np.zeros((YTest.shape[0], 6))
YhotTest[np.arange(YTest.shape[0]), YintTest] = 1

YintVal = np.int64(YVal)
YhotVal = np.zeros((YVal.shape[0], 6))
YhotVal[np.arange(YVal.shape[0]), YintVal] = 1

YhotTest = np.repeat(YhotTest[:, :, np.newaxis], 45, axis=2)
YhotTest = np.swapaxes(YhotTest, 1, 2)

YhotVal = np.repeat(YhotVal[:, :, np.newaxis], 45, axis=2)
YhotVal = np.swapaxes(YhotVal, 1, 2)

YhotTrain = np.repeat(YhotTrain[:, :, np.newaxis], 45, axis=2)
YhotTrain = np.swapaxes(YhotTrain, 1, 2)


def get_model():
    model = Sequential([
        TimeDistributed(Conv1D(16, 3, activation='relu',
                        padding="same"), input_shape=XchTrain.shape[1:]),
        TimeDistributed(BatchNormalization()),
        # TimeDistributed(MaxPooling1D()),
        TimeDistributed(Dropout(0.5)),
        #TimeDistributed(Conv1D(64,3, activation='relu',padding = "same")),
        BatchNormalization(),
        # TimeDistributed(Dropout(0.8)),
        TimeDistributed(Flatten()),
        # TimeDistributed(Dense(30,activation='softmax')),
        LSTM(20, unit_forget_bias=0.5, return_sequences=True),
        TimeDistributed(Dense(6, activation='softmax'))
    ])
    adam = Adam(lr=0.0001)
    model.compile(loss='categorical_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])
    return model


model = get_model()
filepath = "weights/" + "val1" + "-{epoch:02d}-{val_acc:.4f}.hdf5"
checkpoint = ModelCheckpoint(
    filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]
model_history = model.fit(XchTrain, YhotTrain, epochs=100, batch_size=32,
                          callbacks=callbacks_list, validation_data=(XchVal, YhotVal))
plt.plot(model_history.history['acc'])
plt.plot(model_history.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='lower right')
plt.show()
# plt.savefig('accHigh.svg')

# # Plot loss
plt.plot(model_history.history['loss'])
plt.plot(model_history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.show()
# plt.savefig('lossHigh.svg')
