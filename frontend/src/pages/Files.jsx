import Layout from "../components/Layout";
import filesData from "../data/filesData";

function Files() {
  const getBadge = (action) => {
    switch (action) {
      case "Opened":
        return "bg-primary";
      case "Modified":
        return "bg-warning text-dark";
      case "Deleted":
        return "bg-danger";
      case "Copied":
        return "bg-info text-dark";
      case "Created":
        return "bg-success";
      default:
        return "bg-secondary";
    }
  };

  return (
    <Layout>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>File Monitoring</h2>

        <button className="btn btn-primary">
          Export Report
        </button>
      </div>

      <input
        className="form-control mb-3"
        placeholder="Search File..."
      />

      <table className="table table-dark table-hover table-bordered shadow">

        <thead className="table-dark">

          <tr>
            <th>ID</th>
            <th>Employee</th>
            <th>File Name</th>
            <th>Action</th>
            <th>Location</th>
            <th>Time</th>
          </tr>

        </thead>

        <tbody>

          {filesData.map((file) => (

            <tr key={file.id}>

              <td>{file.id}</td>

              <td>{file.employee}</td>

              <td>{file.fileName}</td>

              <td>
                <span className={`badge ${getBadge(file.action)}`}>
                  {file.action}
                </span>
              </td>

              <td>{file.location}</td>

              <td>{file.time}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </Layout>
  );
}

export default Files;