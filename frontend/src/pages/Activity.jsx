import Layout from "../components/Layout";
import activityLogs from "../data/activityLogs";

function Activity() {
  return (
    <Layout>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Employee Activity</h2>

        <button className="btn btn-primary">
          Export Activity
        </button>
      </div>

      <input
        type="text"
        className="form-control mb-3"
        placeholder="Search Employee Activity..."
      />

      <table className="table table-dark table-hover table-bordered shadow">

        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Employee</th>
            <th>Activity</th>
            <th>Device</th>
            <th>IP Address</th>
            <th>Time</th>
          </tr>
        </thead>

        <tbody>

          {activityLogs.map((log) => (

            <tr key={log.id}>

              <td>{log.id}</td>

              <td>{log.employee}</td>

              <td>{log.activity}</td>

              <td>{log.device}</td>

              <td>{log.ip}</td>

              <td>{log.time}</td>

            </tr>

          ))}

        </tbody>

      </table>
    </Layout>
  );
}

export default Activity;