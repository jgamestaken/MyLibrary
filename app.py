## MyLibrary BETA

## Goals:
# Use flask's built-in sorting system
# Use flask's login system
# Use flask's built-in delivery system
# Use flask's blueprint thingies
# Add an OPTIONAL email verification system(for people with an smtp server)

## Start of script

## STEP 1 - CRUCIAL INITIALIZATION

# Crucial imports(flask, dotenv, etc..)

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

import dotenv
import os

# First initialization steps

dotenv.load_dotenv('.env.default') # First import defaults
dotenv.load_dotenv('.env', override=True) # Then import user preferences

app = Flask(__name__)

# Set up proxy

proxies = int(os.getenv("BEHIND_PROXY")) # Get the environment values

if proxies >= 1: # No WSGI without a proxy indicator.
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=proxies, x_proto=proxies, x_host=proxies, x_port=proxies)


## STEP 2 - FURTHER INITZIALIZATION

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mylibrary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## STEP 3 - INTERNAL IMPORTS

from libraries.extensions import Database, LoginHandler
from libraries.models.user import User, create_default_account
from libraries.models.book import Book

from libraries.routes.login import main_bp
from libraries.routes.home import home_bp

## STEP 4 - SET UP SITES

app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(home_bp, url_prefix="/")

## STEP 5 - SETTING UP AUTHENTICATION

LoginHandler.init_app(app)
LoginHandler.login_view = 'main_bp.index'
LoginHandler.login_message = "Please log in to access this page."

@LoginHandler.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## STEP 6 - SETTING UP DB

Database.init_app(app)

with app.app_context(): # If no db? Make db!
    Database.create_all()

    # Check if the users table is empty, if so, make a default account(how else would you get in?)
    if User.query.count() == 0:
        print("No users in database, creating one admin user")
        create_default_account(app)

## DONE! ALL OTHER MAGIC HAPPENS WITHIN THE JS