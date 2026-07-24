import "./StatCard.css";

function StatCard({ title, value, color, icon }) {
  return (
    <div
      className="stat-card"
      style={{
        borderLeft: `6px solid ${color}`,
      }}
    >
      <div className="stat-card-content">
        <div>
          <h6>{title}</h6>
          <h2>{value}</h2>
        </div>

        <div
          className="stat-icon"
          style={{
            color: color,
          }}
        >
          {icon}
        </div>
      </div>
    </div>
  );
}

export default StatCard;
