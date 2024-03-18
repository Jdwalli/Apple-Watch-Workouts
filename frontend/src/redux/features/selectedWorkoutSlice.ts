import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { GetWorkoutDetailsResponse } from '../../types/client_types'


const initialState: GetWorkoutDetailsResponse = {
    workoutStartDate: undefined,
    workoutType: undefined,
    workout: undefined
}

export const selectedWorkoutSlice = createSlice({
    name: 'selectedWorkout',
    initialState: initialState,
    reducers: {
        updateSelectedWorkout: (state, action: PayloadAction<{data: GetWorkoutDetailsResponse}>) => {
            state.workoutStartDate = action.payload.data.workoutStartDate
            state.workoutType = action.payload.data.workoutType
            state.workout = action.payload.data.workout
        },

        resetSelectedWorkout: (state) => {
            state.workoutStartDate = undefined
            state.workoutType = undefined
            state.workout = undefined
        },
        
    }
})

export const { updateSelectedWorkout, resetSelectedWorkout } = selectedWorkoutSlice.actions

export default selectedWorkoutSlice.reducer