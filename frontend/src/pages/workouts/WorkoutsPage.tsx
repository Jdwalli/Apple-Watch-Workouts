import React from "react";

// Workout components
import WorkoutControl from "./WorkoutControl";
import WorkoutVisualizer from "./WorkoutVisualizer";

// Client
import { WorkoutApiClient } from "../../clients/workout_client";

// Types
import {
  WorkoutBreakdown,
  Workout,
  GetWorkoutDetailsParameters,
} from "../../types/client_types";


interface Props {}

const WorkoutsPage: React.FC<Props> = (props: Props) => {
  const workoutClient = new WorkoutApiClient();
  const [workoutTypes, setWorkoutTypes] = React.useState<[string]>();
  const [workoutDetails, setWorkoutDetails] = React.useState<WorkoutBreakdown[]>();
  const [workout, setWorkout] = React.useState<Workout | undefined>();


  React.useEffect(() => {
    workoutClient.getWorkoutTypes().then((data) => {
      setWorkoutTypes(data.workoutTypes);
    });

    workoutClient.getAllWorkoutDetails().then((data) => {
      setWorkoutDetails(data.workouts);
    });
  }, []);

  React.useEffect(() => {
    
  });



  return (
    <div className="flex w-full h-full">
      <WorkoutControl />
      <WorkoutVisualizer />
    </div>
  );
};

export default WorkoutsPage;