## ALL LOGIN ROUTES

from flask import Blueprint, redirect, request, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user, login_user
from libraries.languages import Language
from libraries.models.user import User
from libraries.environhelper import get_safe_env
from libraries.extensions import Database

main_bp = Blueprint("main-login", __name__) # Set blueprint

@main_bp.route("/") # Main route
def index():
    if current_user.is_authenticated:
        return redirect("/home")
    else:
        return render_template("login.html", Language=Language, env=get_safe_env())
    

@main_bp.route('/login', methods=["POST"]) # Post login? Handle login.
def login():
    if current_user.is_authenticated:
        return redirect("/home")
    else:
        username = request.form.get("username").lower() # usernames are case insensitive
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/")
        else:
            return redirect("?s=0")

@main_bp.route('/register', methods=["POST"]) # Post registration? Handle registration.
def register():
    if current_user.is_authenticated: # Check if user is authenticated.
        if current_user.isadmin == "1":
            username = request.form.username
            password = request.form.password
            isadmin = request.form.admin

            if User.query.filter_by(username=username).first(): # Check if account exists already
                return redirect("?s=0")
            
             # Authentication setup

            hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

            if isadmin:
                isadmin = "1"
            else:
                isadmin = "0"

            new_user = User(username=username, password=hashed_password, isadmin=isadmin)
            Database.session.add(new_user)
            Database.session.commit()
            
            return redirect("?s=1")
        


