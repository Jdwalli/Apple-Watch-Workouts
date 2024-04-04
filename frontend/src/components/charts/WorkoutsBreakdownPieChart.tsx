import React from "react";
import PieChart from "../common/PieChart";
import { WorkoutBreakdownData } from "../../types/client_types";


interface Props {
  totalRecorded: number
  data: WorkoutBreakdownData[]
}

const WorkoutsBreakdownPieChart: React.FC<Props> = (props: Props) => {
  return (
    <div className="h-[20rem] w-[26rem] p-4 rounded-sm bg-[#1E1F25] border border-gray-200 flex flex-col text-black ">
        <div className="flex justify-between text-white">
            <div>
                <span className="">Workout Breakdowns</span>
            </div>
            <div className="bg-shark-925 rounded text-white"> 
            
            <span className="text-md text-white font-bold p-1"> 
            {props.totalRecorded} 
            </span>
            </div>
        </div>
        <PieChart data={props.data} />
        
    </div>
  );
};

export default WorkoutsBreakdownPieChart;