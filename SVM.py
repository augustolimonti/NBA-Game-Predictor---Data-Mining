from preprocessing import Preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import svm

class SVMModel:

    def svm_model(X_train, y_train, X_test, y_test):
        svm_model = svm.SVC()
        svm_model.fit(X_train, y_train)
        accuracy = svm_model.score(X_test, y_test)
        # pred_y =svm_model.predict(self.X_test)
        # print(classification_report(self.y_test, pred_y))

        return accuracy

    def print_results(scores):
        sum = 0
        for score in scores:
            sum += score

        avg_accuracy = sum/len(scores)
        print("The average accuracy for 4 seasons using SVM is ", avg_accuracy)
