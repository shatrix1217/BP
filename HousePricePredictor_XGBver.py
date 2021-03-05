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

for col in ('Alley','Utilities','MasVnrType','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1',
            'BsmtFinType2','FireplaceQu','GarageType','GarageFinish','GarageQual','GarageCond',
           'PoolQC','Fence','MiscFeature'):
    train_df[col]=train_df[col].fillna('None')
    test_df[col]=test_df[col].fillna('None')

for col in ('Electrical','MSZoning','Exterior1st','Exterior2nd','KitchenQual','SaleType','Functional'):
    train_df[col]=train_df[col].fillna(train_df[col].mode()[0])
    test_df[col]=test_df[col].fillna(train_df[col].mode()[0])

for col in ('MasVnrArea','BsmtFinSF1','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF','BsmtFullBath','BsmtHalfBath',
            'GarageYrBlt','GarageCars','GarageArea'):
    train_df[col]=train_df[col].fillna(0)
    test_df[col]=test_df[col].fillna(0)

train_df['LotFrontage']=train_df['LotFrontage'].fillna(train_df['LotFrontage'].mean())
test_df['LotFrontage']=test_df['LotFrontage'].fillna(train_df['LotFrontage'].mean())

#outliers visualized.
fig, axes = plt.subplots(1,2, figsize=(12,5))
ax1= sns.scatterplot(x='GrLivArea', y='SalePrice', data= train_df,ax=axes[0])
ax2= sns.boxplot(x='GrLivArea', data= train_df,ax=axes[1])
#removing outliers mentioned by author
train_df= train_df[train_df['GrLivArea']<4000]

#keep record of the length of the train dataset
len_train_df=train_df.shape[0]
houses= pd.concat([train_df, test_df], sort=False)
# turning some ordered categorical variables into ordered numerical
for col in ["ExterQual", "ExterCond", "BsmtQual", "BsmtCond", "HeatingQC", "KitchenQual",
            "FireplaceQu","GarageQual","GarageCond","PoolQC"]:
    houses[col]= houses[col].map({"Gd": 4 , "TA": 3, "Ex": 5, "Fa":2, "Po":1})

# OneHotEncoding
houses= pd.get_dummies(houses)

# separate it again
train_df= houses[:len_train_df]
test_df= houses[len_train_df:]

x_train= train_df.drop('SalePrice', axis=1)
y_train= train_df['SalePrice']
x_test= test_df.drop('SalePrice', axis=1)

#use hyperopt for parameters optimizing
space = {'n_estimators':hp.quniform('n_estimators', 1000, 4000, 100),
         'gamma':hp.uniform('gamma', 0.01, 0.05),
         'learning_rate':hp.uniform('learning_rate', 0.00001, 0.025),
         'max_depth':hp.quniform('max_depth', 3,7,1),
         'subsample':hp.uniform('subsample', 0.60, 0.95),
         'colsample_bytree':hp.uniform('colsample_bytree', 0.60, 0.98),
         'colsample_bylevel':hp.uniform('colsample_bylevel', 0.60, 0.98),
         'reg_lambda': hp.uniform('reg_lambda', 1, 20)
        }

def objective(params):
    params = {'n_estimators': int(params['n_estimators']),
             'gamma': params['gamma'],
             'learning_rate': params['learning_rate'],
             'max_depth': int(params['max_depth']),
             'subsample': params['subsample'],
             'colsample_bytree': params['colsample_bytree'],
             'colsample_bylevel': params['colsample_bylevel'],
             'reg_lambda': params['reg_lambda']}
    
    xb_a= xgb.XGBRegressor(**params)
    score = cross_val_score(xb_a, x_train, y_train, scoring='neg_mean_squared_error', cv=5, n_jobs=-1).mean()
    return -score

best = fmin(fn= objective, space= space, max_evals=20, rstate=np.random.RandomState(1), algo=tpe.suggest)

xb_b = xgb.XGBRegressor(random_state=0,
                        n_estimators=int(best['n_estimators']), 
                        colsample_bytree= best['colsample_bytree'],
                        gamma= best['gamma'],
                        learning_rate= best['learning_rate'],
                        max_depth= int(best['max_depth']),
                        subsample= best['subsample'],
                        colsample_bylevel= best['colsample_bylevel'],
                        reg_lambda= best['reg_lambda']
                       )

xb_b.fit(x_train, y_train)

preds= xb_b.predict(x_test)

#result output
output = pd.DataFrame({'Id': test_df.Id,'SalePrice': preds})
output.to_csv('submission.csv', index=False)