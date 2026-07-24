import activityData from "../data/activityData";

function RecentActivity() {
  return (
    <div className="card shadow mt-4">
      <div className="card-body">

        <h4 className="text-white mb-4">
          Recent Employee Activity
        </h4>

        <div className="table-responsive">

          <table className="table table-dark table-hover align-middle">

            <thead>
              <tr>
                <th>Employee</th>
                <th>Activity</th>
                <th>Device</th>
                <th>Time</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>

              {activityData.map((item) => (

                <tr key={item.id}>

                  <td>{item.employee}</td>

                  <td>{item.activity}</td>

                  <td>{item.device}</td>

                  <td>{item.time}</td>

                  <td>

                    <span
                      className={`badge ${
                        item.status === "Active"
                          ? "bg-success"
                          : "bg-secondary"
                      }`}
                    >
                      {item.status}
                    </span>

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>
    </div>
  );
}

export default RecentActivity;