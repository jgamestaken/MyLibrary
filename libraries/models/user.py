from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from libraries.extensions import Database

import secrets
import os

class User(UserMixin, Database.Model):
    id = Database.Column(Database.Integer, primary_key=True)
    username = Database.Column(Database.String(80), nullable=False, unique=True)
    password = Database.Column(Database.String, nullable=False)
    isadmin = Database.Column(Database.Integer, nullable=True)

    def __repr__(self):
        return f"<User {self.username}>"
    
def create_default_account(app): # Create a default account for if the database is empty.
    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    username = "MyLibrary"
    password = secrets.token_urlsafe(16)  # random secure password

    # Save credentials to instance/credentials.py
    cred_path = os.path.join(app.instance_path, "credentials.txt")
    with open(cred_path, "w") as f:
        f.write(f'USERNAME = "{username}"\n')
        f.write(f'PASSWORD = "{password}"\n')

    print(f"Generated credentials saved to {cred_path}")

    # Create user in database
    user = User(username=username, password=generate_password_hash(password, method="pbkdf2:sha256"), isadmin="1")
    Database.session.add(user)
    Database.session.commit()

    print(f"Default account created: username={username}, password={password}")
