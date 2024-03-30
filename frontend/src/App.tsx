import React from "react";
import { Routes, Route } from "react-router-dom";

//Layout 
import Layout from "./components/shared/Layout";

// Pages
import HomePage from "./pages/home/HomePage";
import ActivityPage from "./pages/activity/ActivityPage";
import VitalsPage from "./pages/vitals/VitalsPage";
import WorkoutsPage from "./pages/workouts/WorkoutsPage";
import SleepPage from "./pages/sleep/SleepPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
      </Route>
    </Routes>
  );
}

export default App;
