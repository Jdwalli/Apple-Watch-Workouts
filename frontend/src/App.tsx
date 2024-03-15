import React from "react";
import { Routes, Route } from "react-router-dom";

// Pages
import HomePage from "./pages/home/HomePage";
import ActivityPage from "./pages/activity/ActivityPage";
import VitalsPage from "./pages/vitals/VitalsPage";
import WorkoutsPage from "./pages/workouts/WorkoutsPage";
import SleepPage from "./pages/sleep/SleepPage";

import DateTime from "./components/common/DateTime";

function App() {
  return (
    <DateTime timestamp="2024-02-21 01:43:05 -0500" />
  );
}

export default App;
