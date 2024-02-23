import xml.etree.cElementTree as ET
import pandas as pd
import os, json
from zipfile import ZipFile
from collections import OrderedDict
from utils import name_utils as name_utils
from utils import file_utils as file_utils
from processors.workout_record import WorkoutRecord, WorkoutRoute
from processors.activity_summary_record import ActivitySummary
from processors.health_record import HealthRecord
from config import DATA_FORMATS, DATA_DIRECTORY_PATH, DATA_SUBDIRECTORY_PATHS,APPLE_HEALTH_PROPERTY_MAPPINGS, USER_DATA_FILE_NAME

class AppleHealthExport:
    def __init__(self, healthExport, export_path: str):
        self.healthExport = healthExport
        self.zipFile = ZipFile(self.healthExport, 'r')
        self.export_path = export_path

        # Export paths
        self.xml_export = os.path.join(self.export_path, 'export.xml')
        self.workout_routes = os.path.join(self.export_path, 'workout-routes')
        self.electrocardiograms = os.path.join(self.export_path, 'electrocardiograms')

        # Export data
        self.export_root = self._generate_root()
        self.activity_summaries = self.export_root.findall('ActivitySummary')
        self.workouts = self.export_root.findall('Workout')
        self.records = self.export_root.findall('Record')
        self.user = self.export_root.find('Me')

        # File names
        self.workouts_file = 'Workouts.csv'
        self.workout_event_file = 'WorkoutEvents.json'
        self.activity_summaries_file = 'Activity Summaries.csv'
        
    def _generate_root(self):
        try:
            return ET.fromstring(self.zipFile.read(self.xml_export))
        except Exception as e:
            print(f"Exception occurred when trying to return tree root.\n{e}")
    
    def _parse_activity_summaries(self):
        COLUMNS = DATA_FORMATS['CSV_HEADERS']['ACTIVITY_SUMMARY']['COLUMNS']
        data = {'Summary': [] for _ in self.activity_summaries}
        for summary in self.activity_summaries:
            data['Summary'].append(ActivitySummary(summary).to_csv_row())
        for key in data:
            data[key] = pd.DataFrame(data[key], columns=COLUMNS)
            df = pd.DataFrame.from_dict(data[key]) 
            df.to_csv(os.path.join(DATA_SUBDIRECTORY_PATHS['Health Records'], self.activity_summaries_file), index = False, header=True)

    def _parse_workouts(self):
        COLUMNS = DATA_FORMATS['CSV_HEADERS']['WORKOUTS']['COLUMNS']
        data = {'Workout': [] for _ in self.workouts}
        workout_event_data = {}
        for workout in self.workouts:
            parsed_workout = WorkoutRecord(workout)
            data['Workout'].append(parsed_workout.to_csv_row())
            event_key, event_data = parsed_workout.to_json_entry()
            if (len(event_data) > 0):
                workout_event_data[event_key] = event_data

        for key in data:
            data[key] = pd.DataFrame(data[key], columns=COLUMNS)
            df = pd.DataFrame.from_dict(data[key]) 
            df.to_csv(os.path.join(DATA_SUBDIRECTORY_PATHS['Workouts'], self.workouts_file), index = False, header=True)

        with open(os.path.join(DATA_SUBDIRECTORY_PATHS['Workouts'], self.workout_event_file), 'w') as json_file:
            json.dump(workout_event_data, json_file, indent=4)
    
    def _parse_health_records(self):
        unsupported_records = []
        records_data = {name_utils.remove_prefixes(record.get("type")): [] for record in self.records}

        for record in self.records:
            current_record = HealthRecord(record)
            record_name = current_record.record_type
            record_data = current_record.to_csv()

            try:
                records_data[record_name].append(record_data)
            except Exception:
                unsupported_records.append(record_name)

        if len(unsupported_records) > 0:
            print(f"Unsupported records: {set(unsupported_records)}")

        for category, category_info in APPLE_HEALTH_PROPERTY_MAPPINGS.items():
            category_directory = category_info['DIRECTORY']
            supported_records = category_info['SUPPORTED_RECORDS']

            for record in records_data:
                if record in supported_records:
                    record_directory = category_directory
                    column_type = supported_records[record]
                    
                    records_data[record] = pd.DataFrame(records_data[record], columns=column_type)
                    df = pd.DataFrame.from_dict(records_data[record])

                    df.to_csv(os.path.join(record_directory, f"{record}.csv"), index=False, header=True)

    def _parse_user_data(self):
        locale = self.export_root.attrib['locale']
        export_date = self.export_root.find('ExportDate').attrib['value']
        date_of_birth = self.user.attrib['HKCharacteristicTypeIdentifierDateOfBirth']
        sex = name_utils.biologicalSexToName(self.user.attrib['HKCharacteristicTypeIdentifierBiologicalSex'])
        blood_type = name_utils.bloodTypeToName(self.user.attrib['HKCharacteristicTypeIdentifierBloodType'])
        skin_type = name_utils.fitzpatrickSkinTypeToName(self.user.attrib['HKCharacteristicTypeIdentifierFitzpatrickSkinType'])

        ordered_dict_data = OrderedDict({
            'locale': [locale],
            'exportDate': [export_date],
            'dateOfBirth': [date_of_birth],
            'sex': [sex],
            'bloodType': [blood_type],
            'skinType': [skin_type]
        })

        df = pd.DataFrame.from_dict(ordered_dict_data)
        df.to_csv(os.path.join(DATA_DIRECTORY_PATH, USER_DATA_FILE_NAME), index=False, header=True)
        
    def _parse_gpx_data(self) -> dict:
        data = {file.filename: [] for file in self.zipFile.infolist() if file.filename.startswith(self.workout_routes)}
        valid_files = [
            file.filename
            for file in self.zipFile.infolist()
            if file.filename.startswith(self.workout_routes)
        ]

        for path in valid_files:
            ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
            # workout_data_path = os.path.join(self.workout_routes, path)
            tracks = file_utils.load_gpx_path(self.zipFile.read(path)).findall('gpx:trk', ns)

            for track in tracks:
                track_segments = track.findall('gpx:trkseg', ns)
                for track_segment in track_segments:
                    track_points = track_segment.findall('gpx:trkpt', ns)
                    for track_point in track_points:
                        try:
                            data[path].append(WorkoutRoute(track_point).to_csv_row())
                        except KeyError:
                            print("error")

        for key in data:
            data[key] = pd.DataFrame(data[key], columns=['lon', 'lat', 'elevation', 'time', 'speed', 'course', 'hAcc', 'vAcc'])
            df = pd.DataFrame.from_dict(data[key]) 
            filename_without_extension, _ = os.path.splitext(os.path.basename(key))
            df.to_csv(os.path.join(DATA_SUBDIRECTORY_PATHS['Workouts'], 'workout-routes', f"{filename_without_extension}.csv"), index = False, header=True)      

    def parse_health_data(self):
        self._parse_gpx_data()
        self._parse_health_records()
        self._parse_user_data()
        self._parse_activity_summaries()
        self._parse_workouts()