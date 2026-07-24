import "../styles/navbar.css";

function Navbar() {
  const admin = JSON.parse(localStorage.getItem("admin"));

  return (
    <div className="navbar">
      <div className="navbar-title">
        Employee Activity Monitoring System
      </div>

      <div className="navbar-user">
        Welcome,
        <span className="username">
          {admin?.username || "Admin"}
        </span>
      </div>
    </div>
  );
}

export default Navbar;