import re
from config import * 

def biologicalSexToName(sex: str) -> str:
  ''' Removes HKBiologicalSex prefix from Biological Sex type objects '''
  return sex.replace("HKBiologicalSex", "")

def bloodTypeToName(bloodType: str) -> str:
  ''' Removes HKBloodType prefix from Blood Type type objects '''
  return bloodType.replace("HKBloodType", "")

def fitzpatrickSkinTypeToName(fitzpatrickSkinType: str) -> str:
  ''' Removes HKFitzpatrickSkinType prefix from Skin Type type objects '''
  return fitzpatrickSkinType.replace("HKFitzpatrickSkinType", "")

def characteristicToName(characteristic : str) -> str:
  ''' Removes HKCharacteristicTypeIdentifier prefix from characteristic type objects '''
  return characteristic.replace(CHARACTERISTIC_PREFIX, "")

def categoryToName(characteristic : str) -> str:
  ''' Removes HKCategoryTypeIdentifier prefix from category type objects '''
  return characteristic.replace(CATEGORY_IDENTIFIER_PREFIX, "")

def workoutToName(workout: str) -> str:
  ''' Removes workoutActivityType prefix from workoutActivityType field '''
  return workout.replace(WORKOUT_PREFIX, '')

def workoutEventToName(workoutEvent: str) -> str:
  ''' Removes HKWorkoutEventType prefix from HKWorkoutEventType field '''
  return workoutEvent.replace(WORKOUT_EVENT_PREFIX, '')

def typeIdentifierToName(name: str) -> str:
  ''' Removes HKQuantityTypeIdentifier prefix from HKQuantityTypeIdentifier field '''
  return name.replace(TYPE_IDENTIFIER_PREFIX, "")

def deviceToName(device: str) -> str:
  ''' Uses regex to parse name field from device string '''
  pattern = r"name:([^,]+)"
  return match[1] if (match := re.search(pattern, device)) else ''

def metadataKeyToName(name: str) -> str:
  ''' Removes HK or HKMetadataKey prefix from metadata field '''
  if (name[:2] == HEALTH_KIT_PREFIX):
    return name.replace(HEALTH_KIT_PREFIX, "")
  return name.replace(METADATA_KEY_PREFIX, "")

def workoutLocationFromValue(value: str) -> str:
  ''' Determines if workout is indoor or outdoor based on value'''
  return 'Outdoor' if int(value) == 0 else 'Indoor'

def remove_prefixes(value: str) -> str:
  val = categoryToName(value)
  return typeIdentifierToName(val)

def format_category_name(category_name):
  category_name = category_name.replace('_RECORDS', '')
  words = category_name.split('_')

  return ' '.join(word.capitalize() for word in words)

def format_record_name(record_name):
  if record_name != 'VO2Max':
    words = [word.capitalize() for word in re.findall('[A-Z][a-z]*', record_name)]
    record_name = ' '.join(words)

  return record_name