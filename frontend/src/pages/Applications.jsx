import Layout from "../components/Layout";
import applicationsData from "../data/applicationsData";

function Applications() {
  return (
    <Layout>

      <div className="d-flex justify-content-between align-items-center mb-4">

        <h2>Application Monitoring</h2>

        <button className="btn btn-primary">
          Export Report
        </button>

      </div>

      <input
        type="text"
        className="form-control mb-3"
        placeholder="Search Application..."
      />

      <table className="table table-dark table-hover table-bordered shadow">

        <thead className="table-dark">

          <tr>
            <th>ID</th>
            <th>Employee</th>
            <th>Application</th>
            <th>Usage Time</th>
            <th>Status</th>
          </tr>

        </thead>

        <tbody>

          {applicationsData.map((app) => (

            <tr key={app.id}>

              <td>{app.id}</td>

              <td>{app.employee}</td>

              <td>{app.application}</td>

              <td>{app.duration}</td>

              <td>

                <span
                  className={
                    app.status === "Active"
                      ? "badge bg-success"
                      : "badge bg-secondary"
                  }
                >
                  {app.status}
                </span>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </Layout>
  );
}

export default Applications;