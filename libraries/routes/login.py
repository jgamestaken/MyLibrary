from flask import Blueprint, redirect, request, render_template
from flask_login import current_user
from libraries.languages import Language
from libraries.environhelper import get_safe_env

main_bp = Blueprint("main-login", __name__)

@main_bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect("/home")
    else:
        return render_template("login.html", Language=Language, env=get_safe_env())
