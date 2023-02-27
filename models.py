from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = 'https://st3.depositphotos.com/4111759/13425/v/600/depositphotos_134255710-stock-illustration-avatar-vector-male-profile-gray.jpg'



class Pet(db.Model):
    """Pet model"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    name = db.Column(db.Text,nullable=False)

    species = db.Column(db.Text,nullable=False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,nullable=False, default = True)

    def image_url(self):
        """Returns picture for pet or default pic"""
        return self.photo_url or DEFAULT_IMG

def connect_db(app):
    """Connects to database"""

    db.app = app
    db.init_app(app)
