from config import DATA_DIRECTORY_PATH, USER_DATA_FILE_NAME, APPLE_HEALTH_PROPERTY_MAPPINGS, USER_DATA_CONFIG
import pandas as pd
import os
from utils import file_utils as file_utils
from utils import mapping_utils as mapping_utils
from utils import chart_utils as chart_utils
from handlers import record as record_data_handler
from handlers import workouts as workout_data_handler

USER_FILE = os.path.join(DATA_DIRECTORY_PATH, USER_DATA_FILE_NAME)

def get_user_data():
    """
    Retrieve user data from a CSV file.

    Returns:
        dict: A dictionary containing user data if the file exists,
              otherwise returns None. The dictionary structure includes:
                - 'userData' (dict or None): User data dictionary, if available.
                  This dictionary represents the first row of the DataFrame and contains user-related details.
    """
    response = {
        'userData': {},
        'activityRecords': [],
        'vitalRecords': {},
        'workoutRecords': {
            "totalWorkouts": 0,
            "workoutBreakdown": []
        },
    }
    if (file_utils.file_exist(USER_FILE)):
        df = pd.read_csv(USER_FILE).iloc[0]
        response['userData'] = df.to_dict()
        
        for ACTIVITY_RECORD_NAME in APPLE_HEALTH_PROPERTY_MAPPINGS['ACTIVITY_RECORDS']["SUPPORTED_RECORDS"].keys():
            dataframe = record_data_handler.get_record_by_type(ACTIVITY_RECORD_NAME, False)
            if dataframe is not None:
                response['activityRecords'].append(
                {"record": ACTIVITY_RECORD_NAME, "value": int(dataframe['value'].sum()), "unit": dataframe.iloc[0]['unit'], "display": ACTIVITY_RECORD_NAME in USER_DATA_CONFIG['RECORDS_FOR_DISPLAY'], "iconName": mapping_utils.recordToIcon(ACTIVITY_RECORD_NAME)})



        # heart_rate_dataframe = record_data_handler.get_record_by_type("HeartRate", False)
        # response['vitalRecords']['maxHeartRate'] = int(heart_rate_dataframe['value'].max())
        # response['vitalRecords']['heartRateUnit'] = heart_rate_dataframe.iloc[0]['unit']
        # response['vitalRecords']['minHeartRate'] = int(heart_rate_dataframe['value'].min())

        # respiratory_rate_dataframe = record_data_handler.get_record_by_type("RespiratoryRate", False)
        # response['vitalRecords']['maxRespiratoryRate'] = int(respiratory_rate_dataframe['value'].max())
        # response['vitalRecords']['respiratoryRateUnit'] = respiratory_rate_dataframe.iloc[0]['unit']
        # response['vitalRecords']['minRespiratoryRate'] = int(respiratory_rate_dataframe['value'].min())


        workouts_dataframe = workout_data_handler.get_all_workouts()
        workout_counts = workouts_dataframe.groupby('workoutType').size().reset_index(name='count')
        workout_counts_list = workout_counts.to_dict(orient='records')
        workout_counts_modified = [{'id': entry['workoutType'], 'label': entry['workoutType'], 'value': entry['count'], "color" : chart_utils.random_hsl()} for entry in workout_counts_list]
        response['workoutRecords']['totalWorkouts'] = len(workouts_dataframe)
        response['workoutRecords']['workoutBreakdown'] = workout_counts_modified

    return response
    