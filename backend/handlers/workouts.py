import pandas as pd
import numpy as np
import os
import json
from utils import file_utils as file_utils
from config import DATA_SUBDIRECTORY_PATHS
from utils.data_handling_utils import is_nan, return_first_valid_index
from handlers.record import get_record_by_dates_data

WORKOUT_PATH = DATA_SUBDIRECTORY_PATHS['Workouts']
WORKOUT_CSV_PATH = os.path.join(WORKOUT_PATH, 'Workouts.csv')
WORKOUT_EVENTS_PATH = os.path.join(WORKOUT_PATH, 'WorkoutEvents.json')
WORKOUT_ROUTES_PATH = DATA_SUBDIRECTORY_PATHS['Workout Routes']

def get_all_workouts():
    """
    Returns the dataframe that contains all the workout data extracted.

    Returns:
        Dataframe of all extracted workouts including the workout's metadata
    """
    if (file_utils.file_exist(WORKOUT_CSV_PATH)):
        return pd.read_csv(WORKOUT_CSV_PATH)
    return None

def get_all_workout_types():
    """
    Parses all workouts in the workout dataframe and determines a list of unique workout types.

    Returns:
        dict: A dictionary containing the unique workout types.
            - 'workoutTypes' (list): A list of unique workout types extracted from the dataframe.
    """
    response = {
        'workoutTypes': None
    }
    df = get_all_workouts()
    if "workoutType" in df.columns:
        workout_type_counts = df["workoutType"].value_counts().reset_index()
        workout_type_counts.columns = ["type", "entries"]
        response['workoutTypes'] = workout_type_counts.to_dict(orient="records")
    return response

def calculate_workout_statistics(group_data):
    """
    Calculate statistics for a group of workout data.

    Args:
        group_data (DataFrame): A DataFrame containing workout data for a specific workout type.

    Returns:
        dict: A dictionary containing various workout statistics.
            - 'averageDuration' (float): Average duration of the workouts.
            - 'maximumDuration' (float): Maximum duration among the workouts.
            - 'averageHeartRate' (float): Average maximum heart rate among the workouts.
            - 'maximumHeartRate' (float): Maximum maximum heart rate among the workouts.
            - 'averageBasalEnergyBurned' (float): Average basal energy burned among the workouts.
            - 'maximumBasalEnergyBurned' (float): Maximum basal energy burned among the workouts.
            - 'averageActiveEnergyBurned' (float): Average active energy burned among the workouts.
            - 'maximumActiveEnergyBurned' (float): Maximum active energy burned among the workouts.
            - 'averageDistanceTraveled' (float): Average distance traveled among the workouts.
            - 'maximumDistanceTraveled' (float): Maximum distance traveled among the workouts.
            - 'averageLapLength' (float): Average lap length among the workouts.
            - 'maximumLapLength' (float): Maximum lap length among the workouts.
            - 'averageElevationAscended' (float): Average elevation ascended among the workouts.
            - 'maximumElevationAscended' (float): Maximum elevation ascended among the workouts.
            - 'averageElevationDescended' (float): Average elevation descended among the workouts.
            - 'maximumElevationDescended' (float): Maximum elevation descended among the workouts.
            - 'averageMaximumSpeed' (float): Average maximum speed among the workouts.
            - 'maximumMaximumSpeed' (float): Maximum maximum speed among the workouts.
            - 'averageAverageSpeed' (float): Average average speed among the workouts.
    """

    stats_keys = [
        ('averageDuration', 'duration'),
        ('maximumDuration', 'duration'),
        ('averageHeartRate', 'maxHeartRate'),
        ('maximumHeartRate', 'maxHeartRate'),
        ('averageBasalEnergyBurned', 'basalEnergyBurned'),
        ('maximumBasalEnergyBurned', 'basalEnergyBurned'),
        ('averageActiveEnergyBurned', 'activeEnergyBurned'),
        ('maximumActiveEnergyBurned', 'activeEnergyBurned'),
        ('averageDistanceTraveled', 'distanceTraveled'),
        ('maximumDistanceTraveled', 'distanceTraveled'),
        ('averageLapLength', 'lapLength'),
        ('maximumLapLength', 'lapLength'),
        ('averageElevationAscended', 'elevationAscended'),
        ('maximumElevationAscended', 'elevationAscended'),
        ('averageElevationDescended', 'elevationDescended'),
        ('maximumElevationDescended', 'elevationDescended'),
        ('averageMaximumSpeed', 'maximumSpeed'),
        ('maximumMaximumSpeed', 'maximumSpeed'),
        ('averageAverageSpeed', 'averageSpeed')
    ]

    stats = {}
    
    for key, col in stats_keys:
        if 'average' in key:
            value = group_data[col].mean()
        else:
            value = group_data[col].max()
        
        stats[key] = value if not is_nan(value) else None
    return stats

def calculate_workout_breakdown(df):
    """
    Calculate workout statistics breakdown by workout type.

    Args:
        df (DataFrame): A DataFrame containing workout data.

    Returns:
        list: A list of dictionaries containing workout statistics for each workout type.
            Each dictionary contains keys:
            - 'workoutName' (str): The name of the workout type.
            - Other statistics keys from the 'calculate_workout_statistics' function.
    """
    breakdown_by_workout = []
    grouped = df.groupby('workoutType')
    
    for workout_type, group_data in grouped:
        workout_stats = calculate_workout_statistics(group_data)
        workout_stats['workoutName'] = workout_type
        breakdown_by_workout.append(workout_stats)
    
    return breakdown_by_workout

def get_workouts_breakdown_statistics():
    """
    Get a breakdown of workout statistics for different workout types.

    Returns:
        dict: A dictionary containing workout breakdown statistics.
            - 'workoutBreakdowns' (list): A list of dictionaries containing workout statistics
              for each workout type. Each dictionary contains keys:
                - 'workoutName' (str): The name of the workout type.
                - Other statistics keys from the 'calculate_workout_statistics' function.
    """
    df = get_all_workouts()
    return {'workoutBreakdowns': calculate_workout_breakdown(df)}

def get_workouts_statistics():
    """
    Get aggregated statistics for the collected workout data.

    Returns:
        dict: A dictionary containing aggregated workout statistics.
            - 'workoutStatistics' (dict): A dictionary containing various aggregated statistics:
                - 'totalWorkouts' (int): Total number of workouts in the dataset.
                - 'workoutsByLocation' (dict): A dictionary with workout counts by location.
                - 'shortestDuration' (float): Shortest duration among all workouts.
                - 'longestDuration' (float): Longest duration among all workouts.
                - 'durationUnit' (str): Duration unit of the workouts.
                - 'highestHeartRate' (float): Highest recorded heart rate among all workouts.
                - 'lowestHeartRate' (float): Lowest recorded heart rate among all workouts.
                - 'heartRateUnit' (str): Heart rate unit of the workouts.
                - 'lowestBasalEnergyBurned' (float): Lowest basal energy burned among all workouts.
                - 'highestBasalEnergyBurned' (float): Highest basal energy burned among all workouts.
                - 'basalEnergyBurnedUnit' (str): Basal energy burned unit of the workouts.
                - 'lowestActiveEnergyBurned' (float): Lowest active energy burned among all workouts.
                - 'highestActiveEnergyBurned' (float): Highest active energy burned among all workouts.
                - 'activeEnergyBurnedUnit' (str): Active energy burned unit of the workouts.
                - 'lowestDistanceTraveled' (float): Lowest distance traveled among all workouts.
                - 'highestDistanceTraveled' (float): Highest distance traveled among all workouts.
                - 'distanceTraveledUnit' (str): Distance traveled unit of the workouts.
                - 'highestMaximumSpeed' (float): Highest maximum speed among all workouts.
                - 'speedUnit' (str): Speed unit of the workouts.
                - 'highestAverageMETS' (float): Highest average METS (Metabolic Equivalent of Task) among all workouts.
                - 'averageMETSUnit' (str): METS unit of the workouts.
    """
    response = {
        'workoutStatistics' : None
    }
    df = get_all_workouts()
    response['workoutStatistics'] =  {
            'totalWorkouts': len(df),
            'workoutsByLocation': df['workoutLocation'].value_counts().to_dict(),
            'shortedDuration': df['duration'].min(),
            'longestDuration': df['duration'].max(),
            'durationUnit': df['durationUnit'].to_list()[return_first_valid_index(df, 'durationUnit' )],
            'highestHeartRate': df['maxHeartRate'].max(),
            'lowestHeartRate': df['maxHeartRate'].min(),
            'heartRateUnit': df['heartRateUnit'].to_list()[return_first_valid_index(df, 'heartRateUnit' )],
            'lowestBasalEnergyBurned': df['basalEnergyBurned'].min(),
            'highestBasalEnergyBurned': df['basalEnergyBurned'].max(),
            'basalEnergyBurnedUnit': df['basalEnergyBurnedUnit'].to_list()[return_first_valid_index(df, 'basalEnergyBurnedUnit' )],
            'lowestActiveEnergyBurned': df['activeEnergyBurned'].min(),
            'highestActiveEnergyBurned': df['activeEnergyBurned'].max(),
            'activeEnergyBurnedUnit': df['activeEnergyBurnedUnit'].to_list()[return_first_valid_index(df, 'activeEnergyBurnedUnit' )],
            'lowestDistanceTraveled': df['distanceTraveled'].min(),
            'highestDistanceTraveled': df['distanceTraveled'].max(),
            'distanceTraveledUnit': df['distanceTraveledUnit'].to_list()[return_first_valid_index(df, 'distanceTraveledUnit' )],
            'highestMaximumSpeed': df['maximumSpeed'].max(),
            'speedUnit': df['speedUnit'].to_list()[return_first_valid_index(df, 'speedUnit' )],
            'highestAverageMETS': df['averageMETS'].max(),
            'averageMETSUnit': df['averageMETSUnit'].to_list()[return_first_valid_index(df, 'averageMETSUnit' )]
        }
    return response

def get_all_workout_event_data():
    """
    Retrieve workout event data from a WorkoutEvents JSON file.

    Returns:
        dict or None: A dictionary containing workout event data if the file exists,
                      otherwise returns None.
    """

    if (file_utils.file_exist(WORKOUT_EVENTS_PATH)):
        with open(WORKOUT_EVENTS_PATH, 'r') as json_file:
            return json.load(json_file)
    return None

def get_workout_event_data(data, accessor):
    """
    Get workout event data from a dictionary using the specified accessor.

    Args:
        data (dict): A dictionary containing workout event data.
        accessor (str): The key to access the desired data within the dictionary.

    Returns:
        Event data or None: The data corresponding to the accessor key if it exists in the dictionary,
                     otherwise returns None.
    """
    return data[accessor] if data and accessor in data else None

def get_workout_data(data: pd.DataFrame, workout_type, workout_start_date):
    """
    Retrieve workout data based on workout type and start date.

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

def get_workout_gpx_data(route_link):
    """
    Retrieve workout GPX data from a CSV file.

    Args:
        route_link (str): Link of the workout route.

    Returns:
        dict or None: A dictionary containing the formatted workout GPX data if the route link is valid
                      and the associated file exists, otherwise returns None.
    """
    if not is_nan(route_link):
        root_link, ext = os.path.splitext(route_link)    
        full_route = f'{WORKOUT_PATH}{root_link}.csv'

        if (file_utils.file_exist(full_route)):
            df = pd.read_csv(full_route)
            return format_workout_gpx_data(df)
    return None

def format_workout_gpx_data(df: pd.DataFrame):
    """
    Format raw workout GPX data stored in a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing raw workout GPX data.

    Returns:
        dict: A dictionary containing formatted workout GPX data with keys:
            - 'longitude' (list): List of longitude values.
            - 'latitude' (list): List of latitude values.
            - 'elevation' (list): List of elevation values.
            - 'time' (list): List of time values.
            - 'speed' (list): List of speed values.
            - 'course' (list): List of course values.
            - 'hAcc' (list): List of horizontal accuracy values.
            - 'vAcc' (list): List of vertical accuracy values.
    """
    return {
        'longitude': df['lon'].to_list(),
        'latitude': df['lat'].to_list(),
        'elevation': df['elevation'].to_list(),
        'time': df['time'].to_list(),
        'speed': df['speed'].to_list(),
        'course': df['course'].to_list(),
        'hAcc': df['hAcc'].to_list(),
        'vAcc': df['vAcc'].to_list()
    }

def generate_workout_response(workout_type, workout_start_date, workout_data, workout_event_data, gpx_data, vitals_records, extra_workout_data):
    """
    Generate a structured response for a workout.

    Args:
        workout_type (str): Type of the workout.
        workout_start_date (str): Start date of the workout.
        workout_data (dict): Workout data containing general details.
        workout_event_data (dict): Workout event data.
        gpx_data (dict): GPX data associated with the workout.
        vitals_records (dict): Vitals records related to the workout.
        extra_workout_data (dict): Additional metrics or data related to the workout.

    Returns:
        dict: A dictionary representing the structured response for the workout with keys:
            - 'workoutType' (str): Type of the workout.
            - 'workoutStartDate' (str): Start date of the workout.
            - 'workout' (dict or None): Nested dictionary containing various workout-related data.
                - If both 'workoutEvents' and 'workoutGPX' are None, this key is set to None.
                - Otherwise, contains the following keys: 'workoutEvents', 'workoutGPX',
                  'workoutVitals', 'workoutAdditionalMetrics'.
    """
    workout_object = {**workout_data,
            'workoutEvents': workout_event_data,
            'workoutGPX': gpx_data,
            'workoutVitals': vitals_records,
            'workoutAdditionalMetrics' : extra_workout_data}
    if workout_object["workoutEvents"] is None and workout_object["workoutGPX"] is None:
        workout_object = None

    return {
        'workoutType': workout_type,
        'workoutStartDate': workout_start_date,
        'workout': workout_object
    }

def get_additional_outdoor_running_metrics(start_date, end_date):
    """
    Get additional outdoor running metrics within a specified date range.

    Args:
        start_date (str): Start date of the date range.
        end_date (str): End date of the date range.

    Returns:
        dict: A dictionary containing additional outdoor running metrics:
            - 'runningPower' (dict): Running power metrics with keys:
                - 'time' (list): List of time values.
                - 'value' (list): List of running power values.
                - 'unit' (str): Unit of running power.
            - 'strideLength' (dict): Stride length metrics with keys:
                - 'time' (list): List of time values.
                - 'value' (list): List of stride length values.
                - 'unit' (str): Unit of stride length.
            - 'verticalOscillation' (dict): Vertical oscillation metrics with keys:
                - 'time' (list): List of time values.
                - 'value' (list): List of vertical oscillation values.
                - 'unit' (str): Unit of vertical oscillation.
            - 'groundContactTime' (dict): Ground contact time metrics with keys:
                - 'time' (list): List of time values.
                - 'value' (list): List of ground contact time values.
                - 'unit' (str): Unit of ground contact time.
            - 'runningSpeed' (dict): Running speed metrics with keys:
                - 'time' (list): List of time values.
                - 'value' (list): List of running speed values.
                - 'unit' (str): Unit of running speed.
    """
    running_power_data = get_record_by_dates_data('RunningPower',start_date, end_date )
    stride_length_data = get_record_by_dates_data('RunningStrideLength',start_date, end_date )
    vertical_oscillation_data = get_record_by_dates_data('RunningVerticalOscillation',start_date, end_date )
    ground_contact_time_data = get_record_by_dates_data('RunningGroundContactTime',start_date, end_date )
    running_speed_data = get_record_by_dates_data('RunningSpeed',start_date, end_date )

    outdoor_running_metrics = {
        'runningPower': {
            'time': running_power_data['startDate'].to_list(),
            'value': running_power_data['value'].to_list(),
            'unit': running_power_data['unit'].iloc[0],
        }
    }
    outdoor_running_metrics['strideLength'] = {
                'time' : stride_length_data['startDate'].to_list(),
                'value' : stride_length_data['value'].to_list(),
                'unit' : stride_length_data['unit'].iloc[0],
            }

    outdoor_running_metrics['verticalOscillation'] = {
                'time' : vertical_oscillation_data['startDate'].to_list(),
                'value' : vertical_oscillation_data['value'].to_list(),
                'unit' : vertical_oscillation_data['unit'].iloc[0],
            }

    outdoor_running_metrics['groundContactTime'] = {
                'time' : ground_contact_time_data['startDate'].to_list(),
                'value' : ground_contact_time_data['value'].to_list(),
                'unit' : ground_contact_time_data['unit'].iloc[0],
            }

    outdoor_running_metrics['runningSpeed'] = {
                'time' : running_speed_data['startDate'].to_list(),
                'value' : running_speed_data['value'].to_list(),
                'unit' : running_speed_data['unit'].iloc[0],
            }
    return outdoor_running_metrics

def get_workout_vital_data(start_date, end_date):
    """
    Get workout vital data (heart rate) within the date range of the workout.

    Args:
        start_date (str): Start date of the date range.
        end_date (str): End date of the date range.

    Returns:
        dict: A dictionary containing workout vital data:
            - 'heartRate' (dict): Heart rate data with keys:
                - 'time' (list): List of time values.
                - 'value' (list): List of heart rate values.
                - 'unit' (str): Unit of heart rate.
    """
    heart_rate_data = get_record_by_dates_data('HeartRate', start_date, end_date)
    return {
        'heartRate': {
            'time': heart_rate_data['startDate'].to_list(),
            'value': heart_rate_data['value'].to_list(),
            'unit': heart_rate_data['unit'].iloc[0],
        }
    }

def get_all_workout_details():
    response = {
        'workouts': None
    }
        
    df = get_all_workouts()
    workout_list = []

    for index, row in df.iterrows():
        workout = {
            'index': index,
            'workoutType': row['workoutType'],
            'workoutLocation': row['workoutLocation'] if not is_nan(row['workoutLocation']) else '' ,
            'duration': row['duration'],
            'durationUnit': row['durationUnit'],
            'startTime': row['startDate'],  
            'fileReference': not is_nan(row['fileReference']) if 'fileReference' in df.columns else False
        }
        workout_list.append(workout)

    response['workouts'] = workout_list
    return response

def get_complete_workout_data(workout_type, workout_start_date):
    """
    Get complete workout data for a specified workout type and start date.

    Args:
        workout_type (str): Type of the workout.
        workout_start_date (str): Start date of the workout.

    Returns:
        dict: A dictionary containing complete workout data including details, events, GPX data, vitals records,
              and additional metrics (if applicable).
            The structure of the returned dictionary is described in the docstring of the 'generate_workout_response' function.
            For additional metrics related to outdoor running, it includes:
            - 'extra_workout_data' (dict): Additional metrics specific to outdoor running, if applicable.
                The structure of this dictionary is defined in the 'get_additional_outdoor_running_metrics' function.
    """
    all_workouts = get_all_workouts()
    all_workout_events = get_all_workout_event_data()
    workout_event_accessor = f'{workout_type}_{workout_start_date}'
    workout_events = get_workout_event_data(
        all_workout_events, workout_event_accessor)
    extra_workout_data = None
    
    workout_data = get_workout_data(
        all_workouts, workout_type, workout_start_date)
    if workout_data:
        start_date = workout_data['startDate']
        end_date = workout_data['endDate']

        route_data = get_workout_gpx_data(workout_data['fileReference'])
        vitals_records = get_workout_vital_data(start_date, end_date)

        if workout_type == 'Running' and workout_data['workoutLocation'] == 'Outdoor':
            extra_workout_data = get_additional_outdoor_running_metrics(start_date, end_date)

    else:
        workout_data = {}
        route_data = None

    return (generate_workout_response(workout_type, workout_start_date, workout_data, workout_events, route_data, vitals_records, extra_workout_data))