import os
import time

from feature_engineering import *
from models.model import *



def load_pickle(MODEL_PICKLE_PATH):
      model = pickle.load(open(MODEL_PICKLE_PATH, 'rb'))
      return model

def main(df, MODEL_PICKLE_PATH):
    data = featureEngineering(df)
    cat_df = data.createDummies()
    # target = data.createTarget()
    # cleanedData = data.mergeDf(cat_df, target)
    X = cat_df.values
    print("testing", X)
    # return X
    # X = arr[:,0:-1]
    # Y = arr[:,-1]
    # print(cleanedData.head(3))
    
    model = load_pickle(MODEL_PICKLE_PATH)
    m = LogisticRegressionModel(model)
    print("model loaded")
    pred = m.predict(X)
    score = m.predict_probability(X)
    # print("pred", pred[0])
    # print("score", score)
    # m.compute_accuracy()
    return pred, score



