import pandas as pd

COLUMNS = "['age', 'job', 'education', 'default', 'balance', 'housing', 'loan']"


class featureEngineering:
    '''
    Input should be a df 
    with columns (['age', 'job', 'education', 'default', 'balance', 'housing', 'loan'], dtype='object')
    '''
    
    def __init__(self, df):
        self.df = df

    def createDummies(self):
        cat_df_dummies = pd.get_dummies( self.df, columns=['job', 'education'])
        cat_df_dummies['housing'] = cat_df_dummies['housing'].map({'yes': 1, 'no': 0})
        cat_df_dummies['default'] = cat_df_dummies['default'].map({'yes': 1, 'no': 0})
        cat_df_dummies['loan'] = cat_df_dummies['loan'].map({'yes': 1, 'no': 0})
        print(cat_df_dummies.head(3))
        print("shape", cat_df_dummies.shape)
        print("columns", cat_df_dummies.columns)
        return cat_df_dummies

    def createTarget(self):
        target = pd.DataFrame(self.df['y'])
        target = target['y'].map({'yes': 1, 'no': 0})
        return target

    def mergeDf(self, cat_df_dummies, target):
        cleaned_dataset = pd.merge(cat_df_dummies, target, left_index = True, right_index = True)
        print("cleaned_dataset", cleaned_dataset.shape)
        return cleaned_dataset


# df = pd.read_csv("precisely_classified/data/test.csv")
# ## to run the class 
# # data.mergeDf() etc create .... function calls 
# data = featureEngineering(df)
# cat_df = data.createDummies()
# target = data.createTarget()
# cleanedData = data.mergeDf(cat_df,target)
# print(cleanedData.head(3))
