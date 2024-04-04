import React from "react";
import { HealthRecordApiClient } from "../../clients/health_record_client";
import { ReturnedActivityRecords, WorkoutBreakdownData } from "../../types/client_types";
import RecordsStatisticsGrid from "./RecordsStatisticsGrid";
import WorkoutsBreakdownPieChart from "../../components/charts/WorkoutsBreakdownPieChart";

// Pie Chart (Total Workouts) 
// Vitals
// Highest HR, Lowest HR, Heart Rate Variabilitu, Wallimg Hr, Average, Cardio Fitness, ECGs taken, Notifications given, Resp Rate, Blood 02


interface Props {}

const HomePage: React.FC<Props> = (props: Props) => {
  const healthRecordClient = new HealthRecordApiClient();
  const [recordStatisticsData, setRecordStatisticsData] = React.useState<ReturnedActivityRecords[]>([])
  const [totalWorkouts, setTotalWorkouts] = React.useState<number>(0);
  const [workoutBreakdownData, setWorkoutBreakdownData] = React.useState<WorkoutBreakdownData[]>([]);

  React.useEffect(() => {
    healthRecordClient.getUserRecord().then((data) => {
      setRecordStatisticsData(data.activityRecords);
      setTotalWorkouts(data.workoutRecords.totalWorkouts);
      setWorkoutBreakdownData(data.workoutRecords.workoutBreakdown);
    });

  }, []);

  return (
    <div className="flex flex-col gap-4">
      <RecordsStatisticsGrid recordsData={recordStatisticsData} />
      <div className="flex flex-row gap-4 w-full">
        {/* <ThirtyDayActivityLineChart /> */}
        <WorkoutsBreakdownPieChart totalRecorded={totalWorkouts} data={workoutBreakdownData} />
      </div>
      <div className="flex flex-row gap-4 w-full"></div>
      <div className="flex flex-row gap-4 w-full"></div>
    </div>
  );
};

export default HomePage;