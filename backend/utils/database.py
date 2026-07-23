from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy object
db = SQLAlchemy()


def init_db(app):
    """
    Initialize the database with the Flask application.
    """
    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("✅ PostgreSQL Database Connected Successfully!")