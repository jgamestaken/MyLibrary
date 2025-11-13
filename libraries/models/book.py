from libraries.extensions import Database

class Book(Database.Model):
    id = Database.Column(Database.Integer, primary_key=True)
    name = Database.Column(Database.String(80), nullable=False, unique=True)
    author = Database.Column(Database.String(80), nullable=False, unique=False)
    genre = Database.Column(Database.String(20), nullable=False, unique=False)
    pages = Database.Column(Database.Integer, nullable=False, unique=False)
    age_rating = Database.Column(Database.Integer, nullable=False, unique=False)

    cover = Database.Column(Database.Text, nullable=True, unique=False)

    def __repr__(self):
        return f"<Book {self.id}>"