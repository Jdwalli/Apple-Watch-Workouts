import pandas as pd
import numpy as np
import os
from utils import file_utils as file_utils
from utils import name_utils as name_utils
from config import DATA_SUBDIRECTORY_PATHS, APPLE_HEALTH_PROPERTY_MAPPINGS

HEALTH_RECORDS_PATH = DATA_SUBDIRECTORY_PATHS['Health Records']

def get_directory_for_record(record_name):
    """
    Get the directory path for a specific record type.

    Args:
        record_name (str): Name of the record type.

    Returns:
        str or None: The directory path associated with the specified record type,
                     or None if the record type is not found in the mappings.
    """
    for category, record_data in APPLE_HEALTH_PROPERTY_MAPPINGS.items():
        supported_records = record_data['SUPPORTED_RECORDS']
        if record_name in supported_records:
            return record_data['DIRECTORY']
    return None 

def get_supported_types():
    """
    Get a dictionary of supported record types categorized by their respective categories.

    Returns:
        dict: A dictionary containing supported record types categorized by their respective categories.
            The dictionary structure is:
                {
                    'Category 1': ['Record Type 1', 'Record Type 2', ...],
                    'Category 2': ['Record Type 3', 'Record Type 4', ...],
                    ...
                }
    """
    SUPPORTED_RECORD_TYPES = {}

    for category in APPLE_HEALTH_PROPERTY_MAPPINGS.keys():
        supported_records = APPLE_HEALTH_PROPERTY_MAPPINGS[category]['SUPPORTED_RECORDS']
        category_name = name_utils.format_category_name(category)
        converted_record_names = sorted([name_utils.format_record_name(record_name) for record_name in supported_records.keys()])

        SUPPORTED_RECORD_TYPES[category_name] = converted_record_names
    """
    Get a dictionary of supported record types categorized by their respective categories.

    Returns:
        dict: A dictionary containing supported record types categorized by their respective categories.
            The dictionary structure is:
                {
                    'Category 1': ['Record Type 1', 'Record Type 2', ...],
                    'Category 2': ['Record Type 3', 'Record Type 4', ...],
                    ...
                }
    """
    return SUPPORTED_RECORD_TYPES

def get_available_types():
    """
    Get available record types categorized by their respective categories.

    Returns:
        dict or None: A dictionary containing available record types categorized by their respective categories,
                      if the health records directory exists. The dictionary structure is:
                        {
                            'Category 1': ['Record Type 1', 'Record Type 2', ...],
                            'Category 2': ['Record Type 3', 'Record Type 4', ...],
                            ...
                        }
                      Returns None if the health records directory doesn't exist.
    """
    results = {}
    if (os.path.isdir(HEALTH_RECORDS_PATH)):
        for element in os.listdir(HEALTH_RECORDS_PATH):
            full_path = os.path.join(HEALTH_RECORDS_PATH, element)
            if os.path.isdir(full_path):
                category_name = name_utils.format_category_name(element)
                converted_record_names = sorted([name_utils.format_record_name(record_name) for record_name in os.listdir(full_path)])
                results[category_name] = converted_record_names
        return results
    return None

def get_record_data(path):
    """
    Load record data from a CSV file.

    Args:
        path (str): Path to the CSV file containing the record data.

    Returns:
        pd.DataFrame or None: A DataFrame containing record data if the file exists,
                              otherwise returns None.
    """
    return pd.read_csv(path) if (file_utils.file_exist(path)) else None

def get_record_by_type(type, return_dict=True):
    """
    Retrieve record data of a specific type.

    Args:
        type (str): Type of the record.
        return_dict (bool, optional): Whether to return the record data as a dictionary (default is True).

    Returns:
        dict or pd.DataFrame or None: A dictionary containing record data if return_dict is True and the file exists,
                                      otherwise returns None.
                                      If return_dict is False, returns a DataFrame containing record data if the file exists,
                                      otherwise returns None.
                                      The dictionary structure includes:
                                        - 'type' (str): The requested record type.
                                        - 'record' (list of dict or None): List of record data dictionaries if available,
                                                                          otherwise None.
    """
    response = {
        'type': type,
        'record' : None
    }
    path = get_directory_for_record(type)
    if path is not None:
        final_path = os.path.join(path, f'{type}.csv')
        data = get_record_data(final_path)
        if return_dict:
            response['record'] = data.to_dict(orient='records')
            return response
        return data

def get_health_records():
    """
    Get information about supported and available health record types.

    Returns:
        dict: A dictionary containing information about supported and available health record types:
            - 'supportedRecordTypes' (dict): Dictionary of supported record types categorized by categories.
                The structure of this dictionary is described in the docstring of the 'get_supported_types' function.
            - 'presentRecordTypes' (dict or None): Dictionary of available record types categorized by categories,
                                                    if the health records directory exists.
                The structure of this dictionary is described in the docstring of the 'get_available_types' function.
                Returns None if the health records directory doesn't exist.
    """
    return {
        "supportedRecordTypes" : get_supported_types(),
        "presentRecordTypes" : get_available_types()
    }

def get_workout_data(data: pd.DataFrame, workout_type, workout_start_date):
    """
    Retrieve workout data based on workout type and start date from a DataFrame.

    Args:
        data (pd.DataFrame): DataFrame containing workout data.
        workout_type (str): Type of the workout.
        workout_start_date (str): Start date of the workout.

    Returns:
        dict or None: A dictionary containing the first matching workout data row as key-value pairs
                      if a matching workout is found, otherwise returns None.
    """
    if not data.empty:
        data = data.replace(np.nan,'',regex=True)

        match = data[
            (data["workoutType"] == workout_type) &
            (data["startDate"] == workout_start_date)
        ]

        if not match.empty:
            return match.iloc[0].to_dict()

    return None

def get_record_by_dates_data(type, startDate, endDate):
    """
    Retrieve record data of a specific type within a date range.

    Args:
        type (str): Type of the record.
        startDate (str): Start date of the date range.
        endDate (str): End date of the date range.

    Returns:
        pd.DataFrame or None: A DataFrame containing record data if the file exists and records within the date range are found,
                              otherwise returns None.
    """
    df = get_record_by_type(type, return_dict=False)
    return df[
            (df["startDate"] >= startDate) &
            (df["endDate"] <= endDate)
    ]
