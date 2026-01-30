from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from app import mongo, User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = mongo.db.users.find_one({"email": request.form["email"]})
        if user and check_password_hash(user["password"], request.form["password"]):
            login_user(User(user))
            return redirect(url_for("booking.booking_home"))
    return render_template("login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        mongo.db.users.insert_one({
            "username": request.form["username"],
            "email": request.form["email"],
            "password": generate_password_hash(request.form["password"])
        })
        return redirect(url_for("auth.login"))
    return render_template("register.html")
