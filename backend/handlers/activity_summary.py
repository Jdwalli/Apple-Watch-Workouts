from utils import file_utils as file_utils
import pandas as pd
import os
from config import DATA_SUBDIRECTORY_PATHS, ACTIVITY_SUMMARY_DATA_FILE_NAME

ACTIVITY_SUMMARY_PATH = os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], ACTIVITY_SUMMARY_DATA_FILE_NAME)

def get_all_activity_summaries():
    """
    Load and return all activity summary data from a CSV file.

    Returns:
        pd.DataFrame or None: A DataFrame containing activity summary data if the file exists,
                              otherwise returns None.
    """
    if (file_utils.file_exist(ACTIVITY_SUMMARY_PATH)):
        return pd.read_csv(ACTIVITY_SUMMARY_PATH)
    return None

def get_activity_summary(date):
    """
    Retrieve activity summary data for a specific date.

    Args:
        date (str): Date for which activity summary is requested.

    Returns:
        dict: A dictionary containing activity summary data for the requested date, if found.
              The dictionary has the following keys:
                - 'activityDate' (str): The requested activity date.
                - 'activity' (dict or None): Activity summary data for the requested date,
                                              if available in the DataFrame.
    """
    response = {
        'activityDate': date,
        'activity' : None
    }
    df = get_all_activity_summaries()
    if df is not None:
        match = df[
            (df["date"] == date)
        ]
        if not match.empty:
            response['activity'] =  match.iloc[0].to_dict()
    return response


def get_activity_summaries():
    """
    Retrieve all activity summaries.

    Returns:
        dict: A dictionary containing a list of activity summary records under the 'activities' key,
              if activity summary data is available in the DataFrame.
              Each activity summary record is represented as a dictionary.
    """
    response = {
        'activities' : None
    }
    df = get_all_activity_summaries()
    if df is not None:
        response['activities'] = df.to_dict(orient='records')
    return response