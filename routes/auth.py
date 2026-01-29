from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    return "Login page working"


@bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")
