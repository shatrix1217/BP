#To-do:import modules
import pandas as pd
import numpy as np



#remove data the missing target value, separate predictors and target.
#Break off validation set from training data.
#Select categorical columns with relatively low cardinality.
#Select numeric columns
#Keep selected columns only
#One-hot encode the data (pandas)




#result output
output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_pred})
output.to_csv('submission.csv', index=False)