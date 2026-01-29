from flask import Blueprint

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/book")
def book():
    return "Booking page working"
