PROJECT_ID = 'taxi-fare-prediction-303822'
BUCKET_NAME = 'automl-project'
DATASET_DISPLAY_NAME = 'taxi_fare_dataset'
TRAIN_FILEPATH = 'C:\\Users\\Watabe\\Desktop\\taxi_fare\\train.csv'
TEST_FILEPATH = 'C:\\Users\\Watabe\\Desktop\\taxi_fare\\test.csv'
TARGET_COLUMN = 'fare_amount'
ID_COLUMN = 'key'
MODEL_DISPLAY_NAME = 'taxi_fare_model'
TRAIN_BUDGET = 1000

from automl_tables_wrapper import AutoMLTablesWrapper
amw = AutoMLTablesWrapper(project_id=PROJECT_ID,
                          bucket_name=BUCKET_NAME,
                          dataset_display_name=DATASET_DISPLAY_NAME,
                          train_filepath=TRAIN_FILEPATH,
                          test_filepath=TEST_FILEPATH,
                          target_column=TARGET_COLUMN,
                          id_column=ID_COLUMN,
                          model_display_name=MODEL_DISPLAY_NAME,
                          train_budget=TRAIN_BUDGET)

amw.train_model()
amw.get_predictions()

submission_df = pd.read_csv("C:\\Users\\Watabe\\Desktop\\taxi_fare\\submission.csv")