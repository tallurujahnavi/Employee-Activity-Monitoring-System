import Layout from "../components/Layout";
import {
  FaUsers,
  FaLaptop,
  FaGlobe,
  FaUsb,
  FaFileAlt,
} from "react-icons/fa";

function Reports() {
  return (
    <Layout>
      <h2 className="mb-4">Reports & Analytics</h2>

      <div className="row">

        <div className="col-md-4 mb-4">
          <div className="card bg-primary text-white shadow">
            <div className="card-body text-center">
              <FaUsers size={35} />
              <h5 className="mt-3">Employees</h5>
              <h2>150</h2>
            </div>
          </div>
        </div>

        <div className="col-md-4 mb-4">
          <div className="card bg-success text-white shadow">
            <div className="card-body text-center">
              <FaLaptop size={35} />
              <h5 className="mt-3">Applications</h5>
              <h2>432</h2>
            </div>
          </div>
        </div>

        <div className="col-md-4 mb-4">
          <div className="card bg-warning shadow">
            <div className="card-body text-center">
              <FaGlobe size={35} />
              <h5 className="mt-3">Website Visits</h5>
              <h2>987</h2>
            </div>
          </div>
        </div>

        <div className="col-md-6 mb-4">
          <div className="card bg-danger text-white shadow">
            <div className="card-body text-center">
              <FaUsb size={35} />
              <h5 className="mt-3">USB Events</h5>
              <h2>25</h2>
            </div>
          </div>
        </div>

        <div className="col-md-6 mb-4">
          <div className="card bg-info text-white shadow">
            <div className="card-body text-center">
              <FaFileAlt size={35} />
              <h5 className="mt-3">File Activities</h5>
              <h2>764</h2>
            </div>
          </div>
        </div>

      </div>

      <div className="card shadow">
        <div className="card-body">
          <h4 className="mb-4">Generate Reports</h4>

          <button className="btn btn-primary me-2">
            Download PDF
          </button>

          <button className="btn btn-success me-2">
            Download Excel
          </button>

          <button className="btn btn-dark">
            Print Report
          </button>
        </div>
      </div>
    </Layout>
  );
}

export default Reports;