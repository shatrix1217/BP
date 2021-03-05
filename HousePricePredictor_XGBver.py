#To-do:import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
import xgboost as xgb
from hyperopt import hp, tpe, fmin

pd.set_option('display.max_columns', None)

train_df = pd.read_csv('C:\\Users\\Watabe\\Desktop\\kaggle_datasets\\kaggle_HousePrice_advanced\\train.csv')
test_df = pd.read_csv('C:\\Users\\Watabe\\Desktop\\kaggle_datasets\\kaggle_HousePrice_advanced\\test.csv')

#exploring the data
list_of_numerics = train_df.select_dtypes(include = ['float', 'int']).columns
types = train_df.dtypes

#percentage of missing data in each column
missing = round((train_df.isnull().sum() / train_df.shape[0]), 3)*100

overview = train_df.apply(
    lambda x : [
        round(x.min()),
        round(x.max()),
        round(x.mean()),
        round(x.quantile(0.5))
    ] if x.name in list_of_numerics else x.unique()
)

#count how many outliers are there in each column
outliers= train_df.apply(lambda x: sum(
                                 (x<(x.quantile(0.25)-1.5*(x.quantile(0.75)-x.quantile(0.25))))|
                                 (x>(x.quantile(0.75)+1.5*(x.quantile(0.75)-x.quantile(0.25))))
                                 if x.name in list_of_numerics else ''))

data_explore = pd.DataFrame({
    'Types' : types,
    'Missing %' : missing,
    'Overview' : overview,
    'Outliers' : outliers}).sort_values(by = ['Missing %', 'Types'], ascending = False)

data_explore.transpose()

#result output
#output = pd.DataFrame({'Id': test_data.Id,
                       #'SalePrice': test_pred})
#output.to_csv('submission.csv', index=False)