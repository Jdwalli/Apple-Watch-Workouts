import React from "react";
import Map from "../common/Map";
import { WorkoutGPX } from "../../types/client_types";

interface Props {
    workoutGPXData: WorkoutGPX | undefined 
}

const WorkoutMap: React.FC<Props> = (props: Props) => {
    const calculateCenter = (long: number[], lat: number[]): [number, number] => {
        if (long.length && lat.length !== 0) {
          const maxLong = Math.max(...long);
          const minLong = Math.min(...long);
          const maxLat = Math.max(...lat);
          const minLat = Math.min(...lat);
    
          const centerLong = (maxLong + minLong) / 2;
          const centerLat = (maxLat + minLat) / 2;
    
          return [centerLat, centerLong];
        }
        return [0, 0];
      };
    
      const calculateZoom = (long: number[], lat: number[]): number => {
        if (long.length && lat.length !== 0) {
    
            const latDistance = Math.max(...props.workoutGPXData?.latitude ?? []) - Math.min(...props.workoutGPXData?.latitude?? [] );
            const longDistance = Math.max(...props.workoutGPXData?.longitude ?? []) - Math.min(...props.workoutGPXData?.longitude ?? []);
          
            const distanceToZoomRatio = 1; 
            let zoom = 10 - Math.log(Math.max(latDistance, longDistance) * distanceToZoomRatio);
            return Math.max(3, zoom)
        }
        return 3;
      };
    
      const center = calculateCenter(props.workoutGPXData?.longitude ?? [], props.workoutGPXData?.latitude ?? []);
      const zoom = calculateZoom(props.workoutGPXData?.longitude ?? [], props.workoutGPXData?.latitude ?? []);
    
      return (
        <div className="flex-1 h-full">
          <Map long={props.workoutGPXData?.longitude ?? []} lat={props.workoutGPXData?.latitude ?? []} center={center} zoom={zoom} />
        </div>
      );
};

export default WorkoutMap;