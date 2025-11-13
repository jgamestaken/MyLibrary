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


## STEP 2 - APP IMPORTS

@app.route('/')
def index():
    return "Hello, world."

