from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)


def generate_token(identity):
    """
    Generate a JWT access token.
    """
    return create_access_token(identity=identity)


def get_current_user():
    """
    Return the identity stored in the JWT.
    """
    return get_jwt_identity()