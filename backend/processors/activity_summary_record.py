import xml.etree.cElementTree as ET

class ActivitySummary:
    def __init__(self, summary: ET.Element):
        self.summary = summary
        self.date = self.summary.get("dateComponents")
        self.active_energy_burned = self.summary.get("activeEnergyBurned")
        self.active_energy_burned_goal = self.summary.get(
            'activeEnergyBurnedGoal')
        self.active_energy_burned_unit = self.summary.get(
            'activeEnergyBurnedUnit')
        self.move_time = self.summary.get('appleMoveTime')
        self.move_time_goal = self.summary.get("appleMoveTimeGoal")
        self.exercise_time = self.summary.get('appleExerciseTime')
        self.exercise_time_goal = self.summary.get('appleExerciseTimeGoal')
        self.stand_hours = self.summary.get('appleStandHours')
        self.stand_hours_goal = self.summary.get('appleStandHoursGoal')

    def to_csv_row(self):
        return ((
            self.date,
            self.active_energy_burned,
            self.active_energy_burned_goal,
            self.active_energy_burned_unit,
            self.move_time,
            self.move_time_goal,
            self.exercise_time,
            self.exercise_time_goal,
            self.stand_hours,
            self.stand_hours_goal
        ))