import Layout from "../components/Layout";
import attendanceData from "../data/attendanceData";

function Attendance() {
  return (
    <Layout>

      <div className="d-flex justify-content-between align-items-center mb-4">

        <h2>Attendance</h2>

        <button className="btn btn-success">
          Download Report
        </button>

      </div>

      <table className="table table-dark table-hover table-bordered shadow">

        <thead className="table-dark">

          <tr>

            <th>ID</th>
            <th>Employee</th>
            <th>Date</th>
            <th>Check In</th>
            <th>Check Out</th>
            <th>Status</th>

          </tr>

        </thead>

        <tbody>

          {attendanceData.map((item) => (

            <tr key={item.id}>

              <td>{item.id}</td>

              <td>{item.employee}</td>

              <td>{item.date}</td>

              <td>{item.checkIn}</td>

              <td>{item.checkOut}</td>

              <td>

                <span
                  className={
                    item.status === "Present"
                      ? "badge bg-success"
                      : "badge bg-danger"
                  }
                >
                  {item.status}
                </span>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </Layout>
  );
}

export default Attendance;