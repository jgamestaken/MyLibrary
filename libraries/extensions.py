# Shared variables(like Database). To be run after initial app initialization.

## IMPORT & INITIALIZE DATABASE

from flask_sqlalchemy import SQLAlchemy
Database = SQLAlchemy()

## IMPORT LOGIN MANAGER

from flask_login import LoginManager
LoginHandler = LoginManager()