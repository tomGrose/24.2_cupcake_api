"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Model for creating a pet"""

    __tablename__ = "cupcakes"

    def __repr__(self):
        """ Show info about a cupcakes"""
        return f"<Cupcake Flavor {self.flavor} ID: {self.id}>"

    

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                    nullable=False)
    size = db.Column(db.Text,
                    nullable=False)
    rating = db.Column(db.Float,
                    nullable=False)
    image = db.Column(db.Text, 
                    nullable=True, default="https://tinyurl.com/demo-cupcake")

    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
   