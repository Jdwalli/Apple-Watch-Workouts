
iconMap = {
    "StepCount" : "FaPersonWalking",
    "ActiveEnergyBurned" : "FaFireFlameSimple",
    "FlightsClimbed" : "FaStairs",
    "AppleExerciseTime" : "FaPersonRunning",
    "AppleStandTime" : "FaPerson",
}

def recordToIcon(recordName: str) -> str:
    if recordName not in iconMap.keys():
        return "FaCircleQuestion"
    else:
        return iconMap[recordName]