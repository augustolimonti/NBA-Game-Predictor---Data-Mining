from preprocessing import Preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.layers import Dropout


class Neural:

    def neural(X_train, y_train, X_test, y_test):
        model = Sequential()
        model.add(Dense(8, input_dim=8, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(8, input_dim=8, activation='relu'))
        model.add(Dense(8, input_dim=8, activation='relu'))
        model.add(Dense(8, input_dim=8, activation='relu'))
        model.add(Dense(8, input_dim=8, activation='relu'))
        # model.add(Dense(8, input_dim=8, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size = 10)

        val_loss, val_acc = model.evaluate(X_test, y_test)
        print('Accuracy of second Nueral Network:', val_acc)

        return val_acc


    def print_results(scores):
        sum = 0
        for score in scores:
            sum += score

        avg_accuracy = sum/len(scores)
        print("The average accuracy for 4 seasons using Neural Network is ", avg_accuracy)
