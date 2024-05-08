import React from "react";

// Workout components
import WorkoutControl from "./WorkoutControl";
import WorkoutVisualizer from "./WorkoutVisualizer";

interface Props {}

const WorkoutsPage: React.FC<Props> = (props: Props) => {
  return (
    <div>
      <WorkoutControl />
      <WorkoutVisualizer />
    </div>
  );
};

export default WorkoutsPage;