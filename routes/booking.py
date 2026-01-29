from flask import Blueprint

bp = Blueprint("booking", __name__, url_prefix="/booking")


@bp.route("/")
def booking_home():
    return "Booking page working"
