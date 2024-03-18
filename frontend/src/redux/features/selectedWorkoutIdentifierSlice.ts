import { createSlice, PayloadAction } from '@reduxjs/toolkit'

export interface SelectedWorkoutIdentifier {
    startDate: string,
    activityType: string
    formattedName: string
}

interface SelectedWorkoutIdentifierState {
    workout: SelectedWorkoutIdentifier
}

const initialState: SelectedWorkoutIdentifierState = {
    workout: {
        startDate: '',
        activityType: '',
        formattedName: ''
    }
}

export const selectedWorkoutIdentifierSlice = createSlice({
    name: 'selectedWorkoutIdentifier',
    initialState: initialState,
    reducers: {
        updateSelectedWorkoutIdentifier: (state, action: PayloadAction<{startDate: string, activityType: string}>) => {
            state.workout.startDate = action.payload.startDate
            state.workout.activityType = action.payload.activityType
        },

        resetSelectedWorkoutIdentifier: (state) => {
            state.workout.startDate = initialState.workout.startDate
            state.workout.activityType = initialState.workout.activityType
            state.workout.formattedName = initialState.workout.formattedName
        },
        
    }
})

export const { updateSelectedWorkoutIdentifier, resetSelectedWorkoutIdentifier } = selectedWorkoutIdentifierSlice.actions

export default selectedWorkoutIdentifierSlice.reducer