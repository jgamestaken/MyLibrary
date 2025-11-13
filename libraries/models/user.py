from flask_login import UserMixin
from libraries.extensions import Database

class User(UserMixin, Database.Model):
    id = Database.Column(Database.Integer, primary_key=True)
    username = Database.Column(Database.String(80), nullable=False, unique=True)
    email = Database.Column(Database.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.username}>"