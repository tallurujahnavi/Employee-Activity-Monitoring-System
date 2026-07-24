import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Employees from "./pages/Employees";
import Attendance from "./pages/Attendance";
import Activity from "./pages/Activity";
import Applications from "./pages/Applications";
import Websites from "./pages/Websites";
import Files from "./pages/Files";
import USB from "./pages/USB";
import Reports from "./pages/Reports";
import Profile from "./pages/Profile";
import NotFound from "./pages/NotFound";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/employees" element={<Employees />} />
                <Route path="/attendance" element={<Attendance />} />
                <Route path="/activity" element={<Activity />} />
                <Route path="/applications" element={<Applications />} />
                <Route path="/websites" element={<Websites />} />
                <Route path="/files" element={<Files />} />
                <Route path="/usb" element={<USB />} />
                <Route path="/reports" element={<Reports />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;