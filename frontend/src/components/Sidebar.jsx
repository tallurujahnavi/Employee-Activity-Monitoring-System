import { Link, useLocation } from "react-router-dom";
import {
  FaTachometerAlt,
  FaUsers,
  FaCalendarCheck,
  FaChartLine,
  FaLaptop,
  FaGlobe,
  FaFolderOpen,
  FaUsb,
  FaFileAlt,
  FaSignOutAlt,
} from "react-icons/fa";

import "../styles/sidebar.css";

function Sidebar() {
  const location = useLocation();

  const menuItems = [
    {
      path: "/dashboard",
      icon: <FaTachometerAlt />,
      label: "Dashboard",
    },
    {
      path: "/employees",
      icon: <FaUsers />,
      label: "Employees",
    },
    {
      path: "/attendance",
      icon: <FaCalendarCheck />,
      label: "Attendance",
    },
    {
      path: "/activity",
      icon: <FaChartLine />,
      label: "Activity",
    },
    {
      path: "/applications",
      icon: <FaLaptop />,
      label: "Applications",
    },
    {
      path: "/websites",
      icon: <FaGlobe />,
      label: "Websites",
    },
    {
      path: "/files",
      icon: <FaFolderOpen />,
      label: "Files",
    },
    {
      path: "/usb",
      icon: <FaUsb />,
      label: "USB",
    },
    {
      path: "/reports",
      icon: <FaFileAlt />,
      label: "Reports",
    },
  ];

  return (
    <div className="sidebar">

      <div className="sidebar-logo">
        <h2>EAMS</h2>
        <p>Employee Activity Monitoring</p>
      </div>

      <div className="sidebar-menu">
        {menuItems.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            className={
              location.pathname === item.path
                ? "sidebar-link active"
                : "sidebar-link"
            }
          >
            <span className="icon">{item.icon}</span>
            <span>{item.label}</span>
          </Link>
        ))}
      </div>

      <div className="sidebar-footer">
        <Link to="/" className="sidebar-link logout">
          <span className="icon">
            <FaSignOutAlt />
          </span>
          <span>Logout</span>
        </Link>
      </div>

    </div>
  );
}

export default Sidebar;