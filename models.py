from preprocessing import Preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.tree import export_graphviz
from sklearn import svm
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from neural_network import Neural
from linear import LinearReg
from SVM import SVMModel
from mlp import MLP
from logistic import Logistic


class Models:

    def __init__(self, dataset):

        #testing data accuracy before applying model_selection
        self.winner = []

        for ind in dataset.index:
            # if ind == 1230:
            #     break
            if dataset['home_win_loss_at_home_percentage'][ind] > dataset['away_win_loss_at_away_percentage'][ind]:
                self.winner.append(1)
            else:
                self.winner.append(0)

        correct_pred = 0
        for ind in dataset.index:
            # if ind == 2460:
            #     break
            if dataset['winner'][ind] == self.winner[ind]:
                correct_pred +=1

        accuracy = correct_pred/len(self.winner)
        # print(accuracy)


        self.winners = dataset[['winner']]
        # print(self.winners)

        self.attributes = []
        for attribute in dataset:
            if attribute != 'winner':
                self.attributes.append(attribute)
        # print(self.attributes)

        season_predictions = ['2016', '2017', '2018', '2019']
        scores = []

        for season in season_predictions:
            if season == '2016':
                self.X_train = pd.DataFrame(dataset[:1845], columns = self.attributes)
                self.y_train = self.winners[:1845]
                self.X_test = pd.DataFrame(dataset[1845:2460], columns = self.attributes)
                self.y_test = self.winners[1845:2460]

            elif season == '2017':
                self.X_train = pd.DataFrame(dataset[1230:3075], columns = self.attributes)
                self.y_train = self.winners[1230:3075]
                self.X_test = pd.DataFrame(dataset[3075:3690], columns = self.attributes)
                self.y_test = self.winners[3075:3690]

            elif season == '2018':
                self.X_train = pd.DataFrame(dataset[2640:4305], columns = self.attributes)
                self.y_train = self.winners[2640:4305]
                self.X_test = pd.DataFrame(dataset[4305:4920], columns = self.attributes)
                self.y_test = self.winners[4305:4920]

            elif season == '2019':
                self.X_train = pd.DataFrame(dataset[3690:5535], columns = self.attributes)
                self.y_train = self.winners[3690:5535]
                self.X_test = pd.DataFrame(dataset[5535:6150], columns = self.attributes)
                self.y_test = self.winners[5535:6150]

            ######LINEAR REGRESSION MODEL#######
            # linear_regression_accuracy = LinearReg.linear(self.X_train, self.y_train, self.X_test, self.y_test)
            # print('For', season, 'we got this much', linear_regression_accuracy)
            # scores.append(linear_regression_accuracy)

            ######LOGISTIC REGRESSION MODEL######
            # logistic_accuracy = Logistic.log_model(self.X_train, self.y_train, self.X_test, self.y_test)
            # print('For', season, 'we got this much', logistic_accuracy)
            # scores.append(logistic_accuracy)

            ########DECISION TREE CLASSIFIER#######
            # decision_tree = DecisionTreeClassifier()
            #
            # decision_tree.fit(self.X_train, self.y_train)
            # y_pred = decision_tree.predict(self.X_test)
            # # print(y_pred)
            # print("Accuracy: ", metrics.accuracy_score(self.y_test, y_pred))

            ####SVM MODEL#######
            # svm_accuracy = SVMModel.svm_model(self.X_train, self.y_train, self.X_test, self.y_test)
            # print('The SVM model accuracy for the', season, 'season is', svm_accuracy)
            # scores.append(svm_accuracy)

            #######Multi-Perceptron CLASSIFIER#######
            # mlpc_accuracy = MLP.mlpc(self.X_train, self.y_train,self.X_test, self.y_test)
            # scores.append(mlpc_accuracy)
            # print('The Neural Network model accuracy for the', season, 'season is', mlpc_accuracy)

            #######DEEP NEURAL NETWORK LEARNING MODEL########
            neural = Neural.neural(self.X_train, self.y_train, self.X_test, self.y_test)
            scores.append(neural)


        # LinearReg.print_results(scores)
        Neural.print_results(scores)
        # MLP.print_results(scores)
        # Logistic.print_results(scores)
        # SVMModel.print_results(scores)
