import xml.etree.cElementTree as ET
from config import HEART_RATE_MOTION_CONTEXT
from utils import name_utils as name_utils


class HealthRecord:
    def __init__(self, record:  ET.Element):
        self.record = record
        self.record_type = name_utils.remove_prefixes(self.record.get("type"))
        self.record_unit = self.record.get("unit")
        self.record_value = self.record.get("value")
        self.record_source_name = self.record.get("sourceName")
        self.record_source_version = self.record.get("sourceVersion")
        self.record_device = self.record.get("device")
        self.record_creation_date = self.record.get("creationDate")
        self.record_start_date = self.record.get("startDate")
        self.record_end_date = self.record.get("endDate")

    def __get_motion_context(self):
        context = self.record.find('MetadataEntry')
        try:
            return HEART_RATE_MOTION_CONTEXT[int(context.get('value'))]
        except Exception:
            return ''

    def __get_heart_rate_record_data(self):
        return ((
                self.record_type,
                self.record_unit,
                self.record_value,
                self.record_source_name,
                self.record_source_version,
                self.record_device,
                self.record_creation_date,
                self.record_start_date,
                self.record_end_date,
                self.__get_motion_context()
                ))

    def __get_default_record_data(self):
        return ((
                self.record_type,
                self.record_unit,
                self.record_value,
                self.record_source_name,
                self.record_source_version,
                self.record_device,
                self.record_creation_date,
                self.record_start_date,
                self.record_end_date,
                ))

    def to_csv(self):
        match self.record_type:
            case 'HeartRate':
                return self.__get_heart_rate_record_data()
            case _:
                return self.__get_default_record_data()
