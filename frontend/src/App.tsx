import React from "react";
import { Routes, Route } from "react-router-dom";

// Navigation
import VerticalNavigation from "./components/navigation/VerticalNavigation";
import TopHeader from "./components/navigation/TopHeader";

// Pages
import HomePage from "./pages/home/HomePage";
import ActivityPage from "./pages/activity/ActivityPage";
import VitalsPage from "./pages/vitals/VitalsPage";
import WorkoutsPage from "./pages/workouts/WorkoutsPage";
import SleepPage from "./pages/sleep/SleepPage";

function App() {
  return (
    <div className="bg-black">
      <VerticalNavigation />
      <TopHeader />
      <div className="ml-16">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/activity" element={<ActivityPage />} />
        <Route path="/vitals" element={<VitalsPage />} />
        <Route path="/workouts" element={<WorkoutsPage />} />
        <Route path="/sleep" element={<SleepPage />} />
      </Routes>
      </div>
      
    </div>
  );
}

export default App;
