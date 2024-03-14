from config import DATA_DIRECTORY_PATH, USER_DATA_FILE_NAME
import pandas as pd
import os
from utils import file_utils as file_utils
from handlers import record as record_data_handler

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
        'activityRecords': {},
        'vitalRecords': {},
        'workoutRecords': {},
    }
    if (file_utils.file_exist(USER_FILE)):
        df = pd.read_csv(USER_FILE).iloc[0]
        response['userData'] = df.to_dict()
        
        step_dataframe = record_data_handler.get_record_by_type("StepCount", False)
        response['activityRecords']['totalSteps'] = int(step_dataframe['value'].sum())
        response['activityRecords']['totalStepsUnit'] = step_dataframe.iloc[0]['unit']

        flights_dataframe = record_data_handler.get_record_by_type("FlightsClimbed", False)
        response['activityRecords']['flightsClimbed'] = int(flights_dataframe['value'].sum())
        response['activityRecords']['flightsClimbedUnit'] = flights_dataframe.iloc[0]['unit']

        exercise_time_dataframe = record_data_handler.get_record_by_type("AppleExerciseTime", False)
        response['activityRecords']['exerciseTime'] = int(exercise_time_dataframe['value'].sum())
        response['activityRecords']['exerciseTimeUnit'] = exercise_time_dataframe.iloc[0]['unit']

        exercise_time_dataframe = record_data_handler.get_record_by_type("AppleStandTime", False)
        response['activityRecords']['standTime'] = int(exercise_time_dataframe['value'].sum())
        response['activityRecords']['standTimeUnit'] = exercise_time_dataframe.iloc[0]['unit']

        heart_rate_dataframe = record_data_handler.get_record_by_type("HeartRate", False)
        response['vitalRecords']['maxHeartRate'] = int(heart_rate_dataframe['value'].max())
        response['vitalRecords']['heartRateUnit'] = heart_rate_dataframe.iloc[0]['unit']
        response['vitalRecords']['minHeartRate'] = int(heart_rate_dataframe['value'].min())

        respiratory_rate_dataframe = record_data_handler.get_record_by_type("RespiratoryRate", False)
        response['vitalRecords']['maxRespiratoryRate'] = int(respiratory_rate_dataframe['value'].max())
        response['vitalRecords']['respiratoryRateUnit'] = respiratory_rate_dataframe.iloc[0]['unit']
        response['vitalRecords']['minRespiratoryRate'] = int(respiratory_rate_dataframe['value'].min())
        
    return response
    