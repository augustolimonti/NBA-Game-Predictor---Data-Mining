from preprocessing import Preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.neural_network import MLPClassifier

class MLP:

    def mlpc(X_train, y_train, X_test, y_test):
        mlpc = MLPClassifier(hidden_layer_sizes = (8,8,8,8,8,8,8), max_iter = 200)
        mlpc.fit(X_train, y_train)
        accuracy = mlpc.score(X_test, y_test)

        return accuracy

    def print_results(scores):
        sum = 0
        for score in scores:
            sum += score

        avg_accuracy = sum/len(scores)
        print("The average accuracy for 4 seasons using MLP is ", avg_accuracy)
