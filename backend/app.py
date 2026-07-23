from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from routes.auth_routes import auth_bp
from config import Config
from utils.database import init_db
from routes.employee_routes import employee_bp
from routes.attendance_routes import attendance_bp
from routes.activity_routes import activity_bp
from routes.application_routes import application_bp
from routes.website_routes import website_bp
from routes.file_routes import file_bp
from routes.usb_routes import usb_bp

import models
# Create Flask application
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize JWT
jwt = JWTManager(app)

# Initialize Socket.IO
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize Database
init_db(app)
app.register_blueprint(auth_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(activity_bp)
app.register_blueprint(application_bp)
app.register_blueprint(website_bp)
app.register_blueprint(file_bp)
app.register_blueprint(usb_bp)


# Home Route
@app.route("/")
def home():
    return {
        "message": "Employee Activity Monitoring System Backend Running Successfully!"
    }

# Run Server
if __name__ == "__main__":
    print("======================================")
    print("🚀 Employee Activity Monitoring System")
    print("======================================")
    print("✅ Flask Server Started")
    print("✅ PostgreSQL Connected")
    print("======================================")

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True
    )