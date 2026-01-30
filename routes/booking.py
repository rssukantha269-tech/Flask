from flask import Blueprint, render_template

bp = Blueprint("booking", __name__, url_prefix="/booking")


@bp.route("/equipment")
def equipment():
    return render_template("booking/equipment.html")


@bp.route("/my-bookings")
def my_bookings():
    return render_template("booking/bookings.html")


@bp.route("/book")
def book():
    return render_template("booking/book.html")
