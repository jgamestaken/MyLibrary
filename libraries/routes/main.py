from flask import Blueprint, redirect, request, render_template
from flask_login import current_user

main_bp = Blueprint("main-login", __name__)

@main_bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect("/home")
    else:
        return render_template("site/login.html")

