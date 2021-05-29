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

# createdb cupcakes / dropdb cupcakes
# python3 seed.py