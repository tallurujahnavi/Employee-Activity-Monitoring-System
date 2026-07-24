import Layout from "../components/Layout";
import StatCard from "../components/StatCard";
import Charts from "../components/Charts";
import RecentActivity from "../components/RecentActivity";

import dashboardData from "../data/dashboardData";

import {
  FaUsers,
  FaUserCheck,
  FaDesktop,
  FaGlobe,
  FaFolderOpen,
  FaUsb,
  FaChartLine,
  FaLaptop,
  FaExclamationTriangle,
  FaClipboardCheck,
} from "react-icons/fa";

function Dashboard() {
  return (
    <Layout>
      {/* Header */}

      <div className="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2 className="text-white mb-1">Dashboard</h2>

          <p className="text-secondary mb-0">
            Welcome back, Admin 👋
          </p>
        </div>

        <button className="btn btn-primary">
          Generate Report
        </button>
      </div>

      {/* Quick Statistics */}

      <div className="row mb-4">

        {/* Productivity */}

        <div className="col-md-3 mb-3">
          <div className="card bg-dark text-white shadow border-start border-success border-4">
            <div className="card-body d-flex justify-content-between align-items-center">

              <div>
                <h3>{dashboardData.productivity}</h3>
                <p className="text-secondary mb-0">
                  Productivity
                </p>
              </div>

              <FaChartLine
                size={42}
                color="#22c55e"
              />

            </div>
          </div>
        </div>

        {/* Active Devices */}

        <div className="col-md-3 mb-3">
          <div className="card bg-dark text-white shadow border-start border-warning border-4">
            <div className="card-body d-flex justify-content-between align-items-center">

              <div>
                <h3>{dashboardData.activeDevices}</h3>
                <p className="text-secondary mb-0">
                  Active Devices
                </p>
              </div>

              <FaLaptop
                size={42}
                color="#f59e0b"
              />

            </div>
          </div>
        </div>

        {/* Suspicious Activities */}

        <div className="col-md-3 mb-3">
          <div className="card bg-dark text-white shadow border-start border-danger border-4">
            <div className="card-body d-flex justify-content-between align-items-center">

              <div>
                <h3>{dashboardData.suspiciousActivities}</h3>
                <p className="text-secondary mb-0">
                  Suspicious Activities
                </p>
              </div>

              <FaExclamationTriangle
                size={42}
                color="#ef4444"
              />

            </div>
          </div>
        </div>

        {/* Attendance */}

        <div className="col-md-3 mb-3">
          <div className="card bg-dark text-white shadow border-start border-info border-4">
            <div className="card-body d-flex justify-content-between align-items-center">

              <div>
                <h3>{dashboardData.attendancePercentage}</h3>
                <p className="text-secondary mb-0">
                  Attendance
                </p>
              </div>

              <FaClipboardCheck
                size={42}
                color="#06b6d4"
              />

            </div>
          </div>
        </div>

      </div>

      {/* Main Dashboard Cards */}

      <div className="row g-4">

        <div className="col-md-4">
          <StatCard
            title="Employees"
            value={dashboardData.totalEmployees}
            color="#2563eb"
            icon={<FaUsers />}
          />
        </div>

        <div className="col-md-4">
          <StatCard
            title="Attendance"
            value={dashboardData.attendanceToday}
            color="#16a34a"
            icon={<FaUserCheck />}
          />
        </div>

        <div className="col-md-4">
          <StatCard
            title="Applications"
            value={dashboardData.applications}
            color="#f59e0b"
            icon={<FaDesktop />}
          />
        </div>

        <div className="col-md-4">
          <StatCard
            title="Websites"
            value={dashboardData.websites}
            color="#8b5cf6"
            icon={<FaGlobe />}
          />
        </div>

        <div className="col-md-4">
          <StatCard
            title="Files"
            value={dashboardData.files}
            color="#06b6d4"
            icon={<FaFolderOpen />}
          />
        </div>

        <div className="col-md-4">
          <StatCard
            title="USB"
            value={dashboardData.usb}
            color="#dc2626"
            icon={<FaUsb />}
          />
        </div>

      </div>

      {/* Charts */}

      <Charts />

      {/* Recent Activity */}

      <RecentActivity />

    </Layout>
  );
}

export default Dashboard;