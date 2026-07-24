import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../api/api";

function Employees() {
  const [employees, setEmployees] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = () => {
    api
      .get("/employees/")
      .then((res) => {
        setEmployees(res.data);
      })
      .catch((err) => {
        console.error("Error fetching employees:", err);
      });
  };

  const filteredEmployees = employees.filter((emp) => {
    const fullName = `${emp.first_name} ${emp.last_name}`.toLowerCase();

    return (
      fullName.includes(search.toLowerCase()) ||
      emp.employee_id.toLowerCase().includes(search.toLowerCase()) ||
      emp.email.toLowerCase().includes(search.toLowerCase()) ||
      emp.department.toLowerCase().includes(search.toLowerCase())
    );
  });

  return (
    <Layout>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="text-white mb-4">Employees</h2>

        <button className="btn btn-primary">
          Add Employee
        </button>
      </div>

      <input
        type="text"
        className="form-control mb-3"
        placeholder="Search Employee..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <table className="table table-dark table-hover table-bordered shadow">
        <thead>
          <tr>
            <th>Employee ID</th>
            <th>Employee Name</th>
            <th>Email</th>
            <th>Department</th>
            <th>Designation</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {filteredEmployees.length > 0 ? (
            filteredEmployees.map((emp) => (
              <tr key={emp.id}>
                <td>{emp.employee_id}</td>

                <td>
                  {emp.first_name} {emp.last_name}
                </td>

                <td>{emp.email}</td>

                <td>{emp.department}</td>

                <td>{emp.designation}</td>

                <td>
                  <span
                    className={
                      emp.status === "Active"
                        ? "badge bg-success"
                        : "badge bg-danger"
                    }
                  >
                    {emp.status}
                  </span>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6" className="text-center">
                No employees found.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </Layout>
  );
}

export default Employees;