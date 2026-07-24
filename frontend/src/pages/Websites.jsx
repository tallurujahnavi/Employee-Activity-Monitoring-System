import Layout from "../components/Layout";
import websitesData from "../data/websitesData";

function Websites() {
  return (
    <Layout>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Website Monitoring</h2>

        <button className="btn btn-primary">
          Export Report
        </button>
      </div>

      <input
        type="text"
        className="form-control mb-3"
        placeholder="Search Website..."
      />

     <table className="table table-dark table-hover table-bordered shadow">

        <thead className="table-dark">

          <tr>
            <th>ID</th>
            <th>Employee</th>
            <th>Website</th>
            <th>Category</th>
            <th>Duration</th>
            <th>Status</th>
          </tr>

        </thead>

        <tbody>

          {websitesData.map((site) => (

            <tr key={site.id}>

              <td>{site.id}</td>

              <td>{site.employee}</td>

              <td>{site.website}</td>

              <td>{site.category}</td>

              <td>{site.duration}</td>

              <td>

                <span
                  className={
                    site.status === "Allowed"
                      ? "badge bg-success"
                      : "badge bg-danger"
                  }
                >
                  {site.status}
                </span>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </Layout>
  );
}

export default Websites;