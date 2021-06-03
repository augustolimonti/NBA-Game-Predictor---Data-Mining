from preprocessing import Preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

class LinearReg:

    def linear(X_train, y_train, X_test, y_test):

        linear_regression = linear_model.LinearRegression()

        linear_regression.fit(X_train, y_train)
        y_pred = linear_regression.predict(X_test)

        y_prediction = []
        for y in y_pred:
            if y >= 0.5:
                y_prediction.append(1)
            else:
                y_prediction.append(0)

        # print(len(y_prediction))
        # print(len(self.y_test))

        y_final_test = []
        for y in y_test.index:
            y_final_test.append(y_test['winner'][y])

        correct_pred = 0
        for i in range(len(y_prediction)):
            if y_final_test[i] == y_prediction[i]:
                correct_pred +=1
                # i += 1
        accuracy = correct_pred / len(y_prediction)

        return accuracy


    def print_results(scores):
        sum = 0
        for score in scores:
            sum += score

        avg_accuracy = sum/len(scores)
        print("The average accuracy for 4 seasons using linear regression is ", avg_accuracy)
