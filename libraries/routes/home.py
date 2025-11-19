## HOMEPAGE & AUTHENTICATION PAGES

from flask import Blueprint, redirect, request, render_template
from flask_login import login_required, current_user

from libraries.languages import Language
from libraries.models.user import User
from libraries.environhelper import get_safe_env
from libraries.extensions import Database

home_bp = Blueprint("home", __name__) # Set blueprint

@login_required
@home_bp.route("/home", methods=["GET"])
def home(): # Homepage
    return render_template("home.html", Language=Language, env=get_safe_env())


@login_required
@home_bp.route("/account", methods=["GET"])
def account(): # Account page
    return render_template("account.html", Language=Language, env=get_safe_env(), username=current_user.username)

