from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint("booking", __name__, url_prefix="/booking")


@bp.route("/")
@login_required
def booking_home():
    return render_template("booking.html")

@bp.route("/my-bookings")
@login_required
def my_bookings():
    return render_template("my_bookings.html")
