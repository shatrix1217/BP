#To-do:import modules
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#To-do:basic variable setup
file_path = "C:\\Users\\Watabe\\Desktop\\ml_competition\\train.csv"
house_data = pd.read_csv(file_path)
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = house_data[features]
y = house_data.SalePrice

#To-do:create model and train it
house_model = RandomForestRegressor(random_state = 1)
house_model.fit(X, y)

#To-do:test the model
test_file_path = "C:\\Users\\Watabe\\Desktop\\ml_competition\\test.csv"
test_data = pd.read_csv(test_file_path)
test_X = test_data[features]
test_pred = house_model.predict(test_X)

#To-do:result output
output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_pred})
output.to_csv('submission.csv', index=False)