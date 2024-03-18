import { SelectedWorkoutIdentifier } from "./features/selectedWorkoutIdentifierSlice";
import { GetWorkoutDetailsResponse } from '../types/client_types'

export interface RootState {
  selectedWorkoutIdentifier: SelectedWorkoutIdentifier
  selectedWorkout: GetWorkoutDetailsResponse
  
}

export interface Action {
  type: string;
  payload: any;
}
