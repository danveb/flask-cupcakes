from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = "https://tinyurl.com/demo-cupcake"

# Models 
class Cupcake(db.Model):
    """Cupcake Model"""
    __tablename__ = 'cupcakes' 
    # Flask SQLAlchemy Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMG_URL) 

    # serialize method (instance method: self) 
    def serialize(self):
        """Return dict representation of cupcake to turn into JSON""" 
        return {
            'id': self.id, 
            'flavor': self.flavor, 
            'size': self.size, 
            'rating': self.rating, 
            'image': self.image
        }

# createdb cupcakes / dropdb cupcakes
# python3 seed.py