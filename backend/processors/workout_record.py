import xml.etree.cElementTree as ET
from collections import OrderedDict
from utils import name_utils as name_utils
from utils import file_utils as file_utils
from config import SWIMMING_LOCATIONS, SWIMMING_STROKE_STYLE

class WorkoutRecord:
    def __init__(self, record: ET.Element):
        self.record = record
        self.workout_data = self._generate_workout_ordered_dict()
        self._parse_workout_records()
        self.workout_statistics = self.record.findall('WorkoutStatistics')
        self._parse_workout_statistics()
        self.workout_route = self.record.find('WorkoutRoute')
        self._parse_workout_file_reference()
        self.workout_event = self.record.findall('WorkoutEvent')
        self.workout_metadata = self.record.findall('MetadataEntry')
        self._parse_workout_events()
        self._parse_workout_metadata()

    def _generate_workout_ordered_dict(self):
        return OrderedDict([
            ('WorkoutType', ''),
            ('WorkoutLocation', ''),
            ('Duration', ''),
            ('DurationUnit', ''),
            ('StartDate', ''),
            ('EndDate', ''),
            ('MaxHeartRate', ''),
            ('MinHeartRate', ''),
            ('AverageHeartRate', ''),
            ('HeartRateUnit', ''),
            ('BasalEnergyBurned', ''),
            ('BasalEnergyBurnedUnit', ''),
            ('ActiveEnergyBurned', ''),
            ('ActiveEnergyBurnedUnit', ''),
            ('DistanceTraveled', ''),
            ('DistanceTraveledUnit', ''),
            ('LapLength', ''),
            ('LapLengthUnit', ''),
            ('ElevationAscended', ''),
            ('ElevationDescended', ''),
            ('ElevationUnit', ''),
            ('MaximumSpeed', ''),
            ('AverageSpeed', ''),
            ('SpeedUnit', ''),
            ('SwimmingLocationType', ''),
            ('StepCount', ''),
            ('MaximumRunningGroundContact', ''),
            ('AverageRunningGroundContact', ''),
            ('MinimumRunningGroundContact', ''),
            ('RunningGroundContactUnit', ''),
            ('MaximumRunningPower', ''),
            ('AverageRunningPower', ''),
            ('MinimumRunningPower', ''),
            ('RunningPowerUnit', ''),
            ('MaximumRunningVerticalOscillation', ''),
            ('AverageRunningVerticalOscillation', ''),
            ('MinimumRunningVerticalOscillation', ''),
            ('RunningVerticalOscillationUnit', ''),
            ('MaximumRunningSpeed', ''),
            ('AverageRunningSpeed', ''),
            ('MinimumRunningSpeed', ''),
            ('RunningSpeedUnit', ''),
            ('MaximumRunningStrideLength', ''),
            ('AverageRunningStrideLength', ''),
            ('MinimumRunningStrideLength', ''),
            ('RunningStrideLengthUnit', ''),
            ('TimeZone', ''),
            ('Humidity', ''),
            ('HumidityUnit', ''),
            ('Temperature', ''),
            ('TemperatureUnit', ''),
            ('AverageMETS', ''),
            ('AverageMETSUnit', ''),
            ('SWOLFScore', ''),
            ('FileReference', '')
        ])

    def _parse_workout_records(self):
        self.workout_data['WorkoutType'] = name_utils.workoutToName(
            self.record.get('workoutActivityType'))
        self.workout_data['Duration'] = self.record.get('duration')
        self.workout_data['DurationUnit'] = self.record.get('durationUnit')
        self.workout_data['StartDate'] = self.record.get('startDate')
        self.workout_data['EndDate'] = self.record.get('endDate')

    def _parse_workout_statistics(self):
        for statistic in self.workout_statistics:
            match statistic.get('type'):
                case 'HKQuantityTypeIdentifierDistanceWalkingRunning':
                    self.workout_data['DistanceTraveled'] = statistic.get(
                        'sum')
                    self.workout_data['DistanceTraveledUnit'] = statistic.get(
                        'unit')
                case 'HKQuantityTypeIdentifierBasalEnergyBurned':
                    self.workout_data['BasalEnergyBurned'] = statistic.get(
                        'sum')
                    self.workout_data['BasalEnergyBurnedUnit'] = statistic.get(
                        'unit')
                case 'HKQuantityTypeIdentifierHeartRate':
                    self.workout_data['MaxHeartRate'] = statistic.get(
                        'maximum')
                    self.workout_data['MinHeartRate'] = statistic.get(
                        'minimum')
                    self.workout_data['AverageHeartRate'] = statistic.get(
                        'average')
                    self.workout_data['HeartRateUnit'] = statistic.get('unit')
                case 'HKQuantityTypeIdentifierActiveEnergyBurned':
                    self.workout_data['ActiveEnergyBurned'] = statistic.get(
                        'sum')
                    self.workout_data['ActiveEnergyBurnedUnit'] = statistic.get(
                        'unit')
                case 'HKQuantityTypeIdentifierRunningGroundContactTime':
                    self.workout_data['MaximumRunningGroundContact'] = statistic.get(
                        'maximum')
                    self.workout_data['MinimumRunningGroundContact'] = statistic.get(
                        'minimum')
                    self.workout_data['AverageRunningGroundContact'] = statistic.get(
                        'average')
                    self.workout_data['RunningGroundContactUnit'] = statistic.get('unit')
                case 'HKQuantityTypeIdentifierRunningPower':
                    self.workout_data['MaximumRunningPower'] = statistic.get(
                        'maximum')
                    self.workout_data['MinimumRunningPower'] = statistic.get(
                        'minimum')
                    self.workout_data['AverageRunningPower'] = statistic.get(
                        'average')
                    self.workout_data['RunningPowerUnit'] = statistic.get('unit')
                case 'HKQuantityTypeIdentifierRunningVerticalOscillation':
                    self.workout_data['MaximumRunningVerticalOscillation'] = statistic.get(
                        'maximum')
                    self.workout_data['MinimumRunningVerticalOscillation'] = statistic.get(
                        'minimum')
                    self.workout_data['AverageRunningVerticalOscillation'] = statistic.get(
                        'average')
                    self.workout_data['RunningVerticalOscillationUnit'] = statistic.get('unit')
                case 'HKQuantityTypeIdentifierRunningSpeed':
                    self.workout_data['MaximumRunningSpeed'] = statistic.get(
                        'maximum')
                    self.workout_data['MinimumRunningSpeed'] = statistic.get(
                        'minimum')
                    self.workout_data['AverageRunningSpeed'] = statistic.get(
                        'average')
                    self.workout_data['RunningSpeedUnit'] = statistic.get('unit')
                case 'HKQuantityTypeIdentifierRunningStrideLength':
                    self.workout_data['MaximumRunningStrideLength'] = statistic.get(
                        'maximum')
                    self.workout_data['MinimumRunningStrideLength'] = statistic.get(
                        'minimum')
                    self.workout_data['AverageRunningStrideLength'] = statistic.get(
                        'average')
                    self.workout_data['RunningStrideLengthUnit'] = statistic.get('unit')
                case 'HKQuantityTypeIdentifierStepCount':
                    self.workout_data['StepCount'] = statistic.get('sum')
                case _:
                    return

    def _parse_workout_events(self):
        workout_event_data = {}

        name = name_utils.workoutToName(self.record.get('workoutActivityType'))
        start_date = self.record.get('startDate')
        event_key = f"{name}_{start_date}"

        workout_event_data[event_key] = []
        for event in self.workout_event:
            event_data = {
                "type": event.attrib.get("type"),
                "date": event.attrib.get("date"),
                "duration": event.attrib.get("duration"),
                "durationUnit": event.attrib.get("durationUnit"),
            }

            metadata_entries = event.findall('MetadataEntry')
            if metadata_entries:
                event_data["metadata"] = []
                for metadata in metadata_entries:
                    key = metadata.attrib.get("key")
                    value = metadata.attrib.get("value")

                    if (key == 'HKSwimmingStrokeStyle'):
                        value = SWIMMING_STROKE_STYLE[int(
                            metadata.attrib.get('value'))]

                    metadata_entry = {
                        "key": key,
                        "value": value
                    }
                    event_data["metadata"].append(metadata_entry)
            workout_event_data[event_key].append(event_data)

        return workout_event_data

    def _parse_workout_metadata(self):
        for metadata in self.workout_metadata:
            match metadata.get('key'):
                case 'HKIndoorWorkout':
                    self.workout_data['WorkoutLocation'] = name_utils.workoutLocationFromValue(
                        metadata.get('value'))
                case 'HKElevationAscended':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['ElevationAscended'] = value
                    self.workout_data['ElevationUnit'] = unit
                case 'HKElevationDescended':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['ElevationDescended'] = value
                case 'HKTimeZone':
                    self.workout_data['TimeZone'] = metadata.get('value')
                case 'HKWeatherHumidity':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['Humidity'] = value
                    self.workout_data['HumidityUnit'] = unit
                case 'HKWeatherTemperature':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['Temperature'] = value
                    self.workout_data['TemperatureUnit'] = unit
                case 'HKAverageMETs':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['AverageMETS'] = value
                    self.workout_data['AverageMETSUnit'] = unit
                case 'HKLapLength':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['LapLength'] = value
                    self.workout_data['LapLengthUnit'] = unit
                case 'HKSwimmingLocationType':
                    self.workout_data['SwimmingLocationType'] = SWIMMING_LOCATIONS[int(
                        metadata.get('value'))]
                case 'HKSWOLFScore':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['SWOLFScore'] = metadata.get('value')
                case 'HKMaximumSpeed':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['MaximumSpeed'] = value
                    self.workout_data['SpeedUnit'] = unit
                case 'HKAverageSpeed':
                    value, unit = metadata.get('value').split(' ')
                    self.workout_data['AverageSpeed'] = value
                case _:
                    return

    def _parse_workout_file_reference(self):
        if (self.workout_route):
            file_path = self.workout_route.find('FileReference')
            if 'path' in file_path.attrib.keys():
                self.workout_data['FileReference'] = file_path.attrib["path"]
                return
        self.workout_data['FileReference'] = ""

    def to_csv_row(self):
        return tuple(self.workout_data.values())

    def to_json_entry(self):
        workout_data = self._parse_workout_events()
        key, value = next(iter(workout_data.items()))
        return key, value

class WorkoutRoute:
    def __init__(self, track_point):
        self.ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
        self.track_point = track_point

    def to_csv_row(self):
        elevation = self.track_point.find('gpx:ele', self.ns).text
        time = self.track_point.find('gpx:time', self.ns).text
        extension = self.track_point.find('gpx:extensions', self.ns)
        lon = self.track_point.get("lon")
        lat = self.track_point.get("lat")
        speed = extension.find('gpx:speed', self.ns).text
        course = extension.find('gpx:course', self.ns).text
        hAcc = extension.find('gpx:hAcc', self.ns).text
        vAcc = extension.find('gpx:vAcc', self.ns).text

        return (lon, lat, elevation, time, speed, course, hAcc, vAcc)