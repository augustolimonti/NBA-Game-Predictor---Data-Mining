from preprocessing import Preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

class Logistic:

    def log_model(X_train, y_train, X_test, y_test):
        logistic_model = LogisticRegression(random_state=0).fit(X_train, y_train)
        accuracy = logistic_model.score(X_test, y_test)

        return accuracy

    def print_results(scores):
        sum = 0
        for score in scores:
            sum += score

        avg_accuracy = sum/len(scores)
        print("The average accuracy for 4 seasons using logistics regression is ", avg_accuracy)
