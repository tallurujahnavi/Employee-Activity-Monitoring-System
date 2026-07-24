import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Bar, Pie } from "react-chartjs-2";
import { chartData, pieData } from "../data/chartData";

// Register Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend
);

function Charts() {
  return (
    <div className="row mt-4">

      <div className="col-lg-8 mb-4">
        <div className="card shadow">
          <div className="card-body">
            <h5 className="text-white mb-3">
              Employee Activity Overview
            </h5>

            <Bar data={chartData} />
          </div>
        </div>
      </div>

      <div className="col-lg-4 mb-4">
        <div className="card shadow">
          <div className="card-body">
            <h5 className="text-white mb-3">
              Activity Distribution
            </h5>

            <Pie data={pieData} />
          </div>
        </div>
      </div>

    </div>
  );
}

export default Charts;