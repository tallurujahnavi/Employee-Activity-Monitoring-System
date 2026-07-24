import Layout from "../components/Layout";
import usbData from "../data/usbData";

function USB() {

  return (
    <Layout>

      <div className="d-flex justify-content-between align-items-center mb-4">

        <h2>USB Device Monitoring</h2>

        <button className="btn btn-primary">
          Export Report
        </button>

      </div>

      <input
        className="form-control mb-3"
        placeholder="Search USB Device..."
      />

      <table className="table table-dark table-hover table-bordered shadow">

        <thead className="table-dark">

          <tr>

            <th>ID</th>
            <th>Employee</th>
            <th>USB Device</th>
            <th>Action</th>
            <th>Serial No.</th>
            <th>Time</th>

          </tr>

        </thead>

        <tbody>

          {usbData.map((usb) => (

            <tr key={usb.id}>

              <td>{usb.id}</td>

              <td>{usb.employee}</td>

              <td>{usb.device}</td>

              <td>

                <span
                  className={
                    usb.action === "Connected"
                      ? "badge bg-success"
                      : "badge bg-danger"
                  }
                >
                  {usb.action}
                </span>

              </td>

              <td>{usb.serial}</td>

              <td>{usb.time}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </Layout>
  );
}

export default USB;