import os

# DATA ROUTES
DATA_DIRECTORY_PATH = os.path.join(os.getcwd(), "backend", "data")
DATA_SUBDIRECTORY_PATHS = {
    "Electrocardiograms": os.path.join(DATA_DIRECTORY_PATH, "Electrocardiograms"),
    "Health Records": os.path.join(DATA_DIRECTORY_PATH, "Health Records"),
    "Workouts": os.path.join(DATA_DIRECTORY_PATH, "Workouts"),
    "Workout Routes": os.path.join(DATA_DIRECTORY_PATH, "Workouts", "workout-routes"),
}

USER_DATA_FILE_NAME = 'User.csv'
ACTIVITY_SUMMARY_DATA_FILE_NAME = 'Activity_Summaries.csv'

DATA_FORMATS = {
    "CSV_HEADERS": {
        "ACTIVITY_SUMMARY": {
            'COLUMNS': [
                "date", 'activeEnergyBurned', 'activeEnergyBurnedGoal', 'activeEnergyBurnedUnit', 'moveTime', 'moveTimeGoal', 'exerciseTime', 'exerciseTimeGoal', 'standHours', 'standHoursGoal'
            ]
        },
        "WORKOUTS": {
            'COLUMNS': 
            ['workoutType', 'workoutLocation', 'duration', 'durationUnit', 'startDate', 'endDate', 'maxHeartRate', 'minHeartRate', 'averageHeartRate', 'heartRateUnit', 'basalEnergyBurned', 'basalEnergyBurnedUnit', 'activeEnergyBurned', 'activeEnergyBurnedUnit', 'distanceTraveled', 'distanceTraveledUnit', 'lapLength', 'lapLengthUnit', 'elevationAscended', 'elevationDescended', 'elevationUnit', 'maximumSpeed', 'averageSpeed', 'speedUnit', 'swimmingLocationType', 'stepCount', 'maximumRunningGroundContact', 'averageRunningGroundContact', 'minimumRunningGroundContact', 'runningGroundContactUnit', 'maximumRunningPower', 'averageRunningPower', 'minimumRunningPower', 'runningPowerUnit', 'maximumRunningVerticalOscillation', 'averageRunningVerticalOscillation', 'minimumRunningVerticalOscillation', 'runningVerticalOscillationUnit', 'maximumRunningSpeed', 'averageRunningSpeed', 'minimumRunningSpeed', 'runningSpeedUnit', 'maximumRunningStrideLength', 'averageRunningStrideLength', 'minimumRunningStrideLength', 'runningStrideLengthUnit', 'timeZone', 'humidity', 'humidityUnit', 'temperature', 'temperatureUnit', 'averageMETS', 'averageMETSUnit', 'swolfScore', 'fileReference']
        },
        "RECORDS": {
            'DEFAULT': {
                'COLUMNS': ["type", "unit", "value", "sourceName", "sourceVersion", "device", "creationDate", 'startDate', "endDate"]
            },
            'HEART_RATE': {
                'COLUMNS': ["type", "unit", "value", "sourceName", "sourceVersion", "device", "creationDate", 'startDate', "endDate", "motionContext"]
            },
            'ElECTROCARDIOGRAM': {
                'COLUMNS': ["type", "unit", "value", "sourceName", "sourceVersion", "device", "creationDate", 'startDate', "endDate", "userEntered"]
            },
            'AUDIO_EVENT': {
                'COLUMNS': ["type", "unit", "value", "sourceName", "sourceVersion", "device", "creationDate", 'startDate', "endDate", "exposureLevel", 'exposureLevelUnit']
            }
        }
    }
}

DEFAULT_COLUMNS = DATA_FORMATS['CSV_HEADERS']['RECORDS']['DEFAULT']['COLUMNS']
HEART_RATE_COLUMNS = DATA_FORMATS['CSV_HEADERS']['RECORDS']['HEART_RATE']['COLUMNS']
# Data Classifications

APPLE_HEALTH_PROPERTY_MAPPINGS = {
    'VITAL_SIGN_RECORDS': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'Vitals'),
        'SUPPORTED_RECORDS': {
            "HeartRate": HEART_RATE_COLUMNS,
            "RestingHeartRate": DEFAULT_COLUMNS,
            "WalkingHeartRateAverage": DEFAULT_COLUMNS,
            "HeartRateVariabilitySDNN": DEFAULT_COLUMNS,
            "HeartRateRecoveryOneMinute": DEFAULT_COLUMNS,
            "AtrialFibrillationBurden": DEFAULT_COLUMNS,
            "OxygenSaturation": DEFAULT_COLUMNS,
            "BodyTemperature": DEFAULT_COLUMNS,
            "BloodPressureDiastolic": DEFAULT_COLUMNS,
            "BloodPressureSystolic": DEFAULT_COLUMNS,
            "RespiratoryRate": DEFAULT_COLUMNS
        }
    },

    'ACTIVITY_RECORDS': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'Activity'),
        'SUPPORTED_RECORDS': {
            "StepCount": DEFAULT_COLUMNS,
            "DistanceWalkingRunning": DEFAULT_COLUMNS,
            "RunningGroundContactTime": DEFAULT_COLUMNS,
            "RunningPower": DEFAULT_COLUMNS,
            "RunningSpeed": DEFAULT_COLUMNS,
            "RunningStrideLength": DEFAULT_COLUMNS,
            "RunningVerticalOscillation": DEFAULT_COLUMNS,
            "DistanceCycling": DEFAULT_COLUMNS,
            "PushCount": DEFAULT_COLUMNS,
            "DistanceWheelchair": DEFAULT_COLUMNS,
            "SwimmingStrokeCount": DEFAULT_COLUMNS,
            "DistanceSwimming": DEFAULT_COLUMNS,
            "DistanceDownhillSnowSports": DEFAULT_COLUMNS,
            "BasalEnergyBurned": DEFAULT_COLUMNS,
            "ActiveEnergyBurned": DEFAULT_COLUMNS,
            "FlightsClimbed": DEFAULT_COLUMNS,
            "NikeFuel": DEFAULT_COLUMNS,
            "AppleExerciseTime": DEFAULT_COLUMNS,
            "AppleMoveTime": DEFAULT_COLUMNS,
            "AppleStandTime": DEFAULT_COLUMNS,
            "VO2Max": DEFAULT_COLUMNS
        }
    },

    'AUDIO_RECORDS': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'Audio'),
        'SUPPORTED_RECORDS': {
            'EnvironmentalAudioExposure': DEFAULT_COLUMNS,
            "HeadphoneAudioExposure": DEFAULT_COLUMNS,
            'EnvironmentalSoundReduction': DEFAULT_COLUMNS,
            'AudioExposureEvent': DEFAULT_COLUMNS,
            'HeadphoneAudioExposureEvent': DEFAULT_COLUMNS
        }
    },

    'MOBILITY_RECORDS': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'Mobility'),
        'SUPPORTED_RECORDS': {
            "AppleWalkingSteadiness": DEFAULT_COLUMNS,
            "SixMinuteWalkTestDistance": DEFAULT_COLUMNS,
            "WalkingSpeed": DEFAULT_COLUMNS,
            "WalkingStepLength": DEFAULT_COLUMNS,
            "WalkingAsymmetryPercentage": DEFAULT_COLUMNS,
            "WalkingDoubleSupportPercentage": DEFAULT_COLUMNS,
            "StairAscentSpeed": DEFAULT_COLUMNS,
            "StairDescentSpeed": DEFAULT_COLUMNS
        }
    },

    'UV_EXPOSURE_RECORDS': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'UV Exposure'),
        'SUPPORTED_RECORDS': {
            "UVExposure": DEFAULT_COLUMNS
        }
    },

    'SLEEP_RECORDS': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'Sleep'),
        'SUPPORTED_RECORDS': {
            "AppleSleepingWristTemperature": DEFAULT_COLUMNS,
            'SleepAnalysis': DEFAULT_COLUMNS
        }
    },

    'DIVING': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'Diving'),
        'SUPPORTED_RECORDS': {
            "UnderwaterDepth": DEFAULT_COLUMNS,
            "WaterTemperature": DEFAULT_COLUMNS
        }
    },

    'SYMPTOM': {
        'DIRECTORY': os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], 'SYMPTOM'),
        'SUPPORTED_RECORDS': {
            "RapidPoundingOrFlutteringHeartbeat": DEFAULT_COLUMNS,
            "AbdominalCramps": DEFAULT_COLUMNS,
            "Bloating": DEFAULT_COLUMNS,
            "Constipation": DEFAULT_COLUMNS,
            "Diarrhea": DEFAULT_COLUMNS,
            "Heartburn": DEFAULT_COLUMNS,
            "Nausea": DEFAULT_COLUMNS,
            "Vomiting": DEFAULT_COLUMNS,
            "AppetiteChanges": DEFAULT_COLUMNS,
            "Chills": DEFAULT_COLUMNS,
            "Dizziness": DEFAULT_COLUMNS,
            "Fainting": DEFAULT_COLUMNS,
            "Fatigue": DEFAULT_COLUMNS,
            "Fever": DEFAULT_COLUMNS,
            "GeneralizedBodyAche": DEFAULT_COLUMNS,
            "HotFlashes": DEFAULT_COLUMNS,
            "ChestTightnessOrPain": DEFAULT_COLUMNS,
            "Coughing": DEFAULT_COLUMNS,
            "ShortnessOfBreath": DEFAULT_COLUMNS,
            "SkippedHeartbeat": DEFAULT_COLUMNS,
            "Wheezing": DEFAULT_COLUMNS,
            "LowerBackPain": DEFAULT_COLUMNS,
            "Headache": DEFAULT_COLUMNS,
            "MemoryLapse": DEFAULT_COLUMNS,
            "MoodChanges": DEFAULT_COLUMNS,
            "LossOfSmell": DEFAULT_COLUMNS,
            "LossOfTaste": DEFAULT_COLUMNS,
            "RunnyNose": DEFAULT_COLUMNS,
            "SoreThroat": DEFAULT_COLUMNS,
            "SinusCongestion": DEFAULT_COLUMNS,
            "BreastPain": DEFAULT_COLUMNS,
            "PelvicPain": DEFAULT_COLUMNS,
            "VaginalDryness": DEFAULT_COLUMNS,
            "Acne": DEFAULT_COLUMNS,
            "DrySkin": DEFAULT_COLUMNS,
            "HairLoss": DEFAULT_COLUMNS,
            "NightSweats": DEFAULT_COLUMNS,
            "SleepChanges": DEFAULT_COLUMNS,
            "BladderIncontinence": DEFAULT_COLUMNS
        }
    },

}

# PREFIXES
CHARACTERISTIC_PREFIX = "HKCharacteristicTypeIdentifier"
WORKOUT_PREFIX = "HKWorkoutActivityType"
WORKOUT_EVENT_PREFIX = "HKWorkoutEventType"
TYPE_IDENTIFIER_PREFIX = "HKQuantityTypeIdentifier"
CATEGORY_IDENTIFIER_PREFIX = 'HKCategoryTypeIdentifier'
HEALTH_KIT_PREFIX = "HK"
METADATA_KEY_PREFIX = "HKMetadataKey"

# Heart Rate Motion Context
HEART_RATE_MOTION_CONTEXT: dict[int, str] = {
    0: "Not Set",
    1: "Sedentary",
    2: "Active"
}

# Swimming Metadata
SWIMMING_LOCATIONS: dict[int, str] = {
    0: "Unknown",
    1: "Pool",
    2: "Open Water"
}

SWIMMING_STROKE_STYLE: dict[int, str] = {
    0: "Unknown",
    1: "Mixed",
    2: "Freestyle",
    3: "Backstroke",
    4: "Breaststroke",
    5: "Butterfly",
    6: "Kick Board"
}

WATER_SALINITY: dict[int, str] = {
    1: "Fresh Water",
    2: "Salt Water"
}

PHYSICAL_EFFORT_ESTIMATION: dict[int, str] = {
    1: "Activity Lookup",
    2: "Device Sensed"
}