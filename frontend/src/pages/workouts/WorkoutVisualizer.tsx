import React from "react";

import WorkoutGraphs from "../../components/workouts/WorkoutGraphs";
import WorkoutMap from "../../components/workouts/WorkoutMap";

interface Props {}

const WorkoutVisualizer: React.FC<Props> = (props: Props) => {
  return (
    <div className="flex-1 h-full">
      <WorkoutMap />
      <WorkoutGraphs />
    </div>
  );
};

export default WorkoutVisualizer;