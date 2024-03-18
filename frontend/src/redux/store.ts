import { configureStore } from "@reduxjs/toolkit";

// Slices
import selectedWorkoutSlice from "./features/selectedWorkoutIdentifierSlice";
import selectedWorkoutIdentifierSlice from "./features/selectedWorkoutIdentifierSlice";

export const store = configureStore({
  reducer: {
    selectedWorkout: selectedWorkoutSlice,
    selectedWorkoutIdentifier: selectedWorkoutIdentifierSlice
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
