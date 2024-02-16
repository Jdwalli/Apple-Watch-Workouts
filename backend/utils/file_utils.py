from config import DATA_DIRECTORY_PATH, DATA_SUBDIRECTORY_PATHS, APPLE_HEALTH_PROPERTY_MAPPINGS
import os, shutil
import xml.etree.cElementTree as ET


def file_exist(file_path):
    if os.path.exists(file_path):
        try:
            file = open(file_path, 'r')
            return True
        except Exception as e:
            print(f"Error opening file '{file_path}': {e}")
            return False
    return False

def get_filenames(path: str):
    filenames = os.listdir(path)
    filenames = [f for f in filenames if os.path.isfile(
        os.path.join(path, f)) and not f.startswith(".")]
    return filenames

def load_gpx_path(path):
    return ET.fromstring(path)

class DataFile:
    def __init__(self):
        pass

    def _data_directory_exist(self, path):
        return os.path.isdir(path)

    def _create_data_directory(self, path):
        if not self._data_directory_exist(path):
            os.mkdir(path)

    def create_data_directories(self):
        self._create_data_directory(DATA_DIRECTORY_PATH)
        for name, path  in DATA_SUBDIRECTORY_PATHS.items():
            self._create_data_directory(path)
        for record_name, record_path in APPLE_HEALTH_PROPERTY_MAPPINGS.items():
            self._create_data_directory(record_path['DIRECTORY'])

    def purge_data_directories(self):
        if self._data_directory_exist(DATA_DIRECTORY_PATH):
            shutil.rmtree(DATA_DIRECTORY_PATH)
    
    def containsData(self):
        if self._data_directory_exist(DATA_DIRECTORY_PATH):
            files = [f for f in os.listdir(DATA_DIRECTORY_PATH) if os.path.isfile(os.path.join(DATA_DIRECTORY_PATH, f))]
            if files:
                return True
        return False