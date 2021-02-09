import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

#from IBM telecom churn dataset
df = pd.read_csv('C:\\Users\\Watabe\\Desktop\\telecom_dataset\\Telco-Customer-Churn.csv')

#filter the data
df.drop(['Churn Label', 'Churn Score', 'CLTV', 'Churn Reason', 'Customer ID', 'Count', 'Country', 'State', 'Lat Long'],axis = 1, inplace = True)

df.loc[(df['Total_Charges'] == ' '), 'Total_Charges'] = 0
df.['Total_Charges'] = pd.to_numeric(df['Total_Charges'])

#variable settings
X = df.drop(['Churn'], axis = 1).copy()
y = df['Churn'].copy()

X_OneHotEncoded = pd.get_dummies(X, columns = ['City', 'Gender', 'Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 'Multiple_Lines', 'Internet_Service', 'Online_Security', 'Online_Backup', 'Device_Protection', 'Tech_Support', 'Streaming_TV', 'Streaming_Movies', 'Contract', 'Paperless_Billing', 'Payment_Method']

X_train, X_test, y_train, y_test = train_test_split(X_OneHotEncoded, y, random_state = 0, stratify = True)

#try to find out the ideal parameter
param_grid = {
    'max_depth' : [3, 4, 5],
    'learning_rate' : [0.1, 0.01, 0.05],
    'gamma' : [0, 0.25, 1.0],
    'reg_lambda' : [0, 1.0, 10.0],
    'scale_pos_weight' : [3]
}

optimal_params = GridSearchCV(
    estimator = xgb.XGBClassifier(objective = 'binary:logistic', seed = 42, subsample = 0.9, colsample_bytree = 0.5),
    param_grid = param_grid,
    scoring = 'roc_auc',
    verbose = 0,
    n_jobs = 10,
    cv = 3
    )
)

optimal_params.fit(
    X_train,
    y_train,
    early_stopping_rounds = 10,
    eval_metric = 'auc',
    eval_set = [(X_test, y_test)],
    verbose = False
)

print(optimal_params.best_params)

clf_xgb = xgb.XGBClassifier(objective = 'binary:logistic', missing = None, seed = 42, gamma = 0.25, learn_rate = 0.1, max_depth = 4, reg_lamda = 10, scale_pos_weight = 3, subsample = 0.9, colsample_bytree = 0.5)

clf_xgb.fit(
    X_train,
    y_train,
    verbose = True
    early_stopping_rounds = 10,
    eval_metric = 'aucpr'
    eval_set = [(X_test, y_test)]
)

plot_confusion_matrix(
    clf_xgb,
    X_test,
    y_test,
    values_format='d',
    display_labels = ["Did not leave", "Left"]
)