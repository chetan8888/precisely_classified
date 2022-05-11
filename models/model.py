# import numpy as np
# import pandas as pd
import pickle
from sklearn.metrics import  accuracy_score
# from sklearn.linear_model import LinearRegression




class LogisticRegressionModel:
    def __init__(self, model) -> None:
        self.model = model

    def load_pickle(MODEL_PICKLE_PATH) -> None:
      model = pickle.load(open(MODEL_PICKLE_PATH, 'rb'))
      return model

    # def _fit(self) -> None:
    #     X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    #     y = np.dot(X, np.array([1, 2])) + 3
    #     self.model = LinearRegression().fit(X, y)
    #     print('score: ', self.model.score(X, y))


    def predict(self, df) -> None:
        y_pred_log = self.model.predict(df)
        # print("predict", y_pred_log)
        return y_pred_log

    def predict_probability(self, df) -> None:
        score = self.model.predict_proba(df)
        # print("score", score)
        return round(score[0][1], 2)  

    def compute_accuracy(self,y_test, y_pred_log) -> None:
        acc = accuracy_score(y_test, y_pred_log)
        return acc