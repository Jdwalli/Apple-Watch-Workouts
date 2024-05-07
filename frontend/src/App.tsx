import { Routes, Route } from "react-router-dom";


// Pages
import HomePage from "./pages/home/HomePage";
import WorkoutsPage from "./pages/workouts/WorkoutsPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />}/>
      <Route path="/workouts" element={<WorkoutsPage />} />
    </Routes>
  );
}

export default App;
