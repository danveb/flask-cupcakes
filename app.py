from flask import Flask, request, jsonify, render_template 
from models import db, connect_db, Cupcake 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'oh-so-super-very-secret'

connect_db(app) 

# GET Route (data of all cupcakes) 
# http://127.0.0.1:5000/api/cupcakes
@app.route('/api/cupcakes')
def list_cupcakes():
    """List all cupcakes""" 
    # lilst comprehenseion -> returns a list of dictionaries 
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    # serialize each cupcake, set key for all_cupcakes 
    return jsonify(cupcakes=all_cupcakes) 

# GET Route (data of a single cupcake) 
# http://127.0.0.1:5000/api/cupcakes/1
@app.route('/api/cupcakes/<int:id>') 
def get_cupcake(id):
    """Get ID of cupcake"""
    # sqlalchemy primary key (id) 
    cupcake = Cupcake.query.get_or_404(id) 
    # serialize and return json 
    return jsonify(cupcake=cupcake.serialize()) 

# POST Route (create a cupcake) 
@app.route('/api/cupcakes', methods=["POST"]) 
def create_cupcake():
    """Create a new cupcake""" 
    # get from json (request.json[''])
    new_cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit() 
    # respond with json with status 201 CREATED (default for POST) 
    response_json = jsonify(cupcake=new_cupcake.serialize()) 
    return (response_json, 201) 

    # TEST with Insomnia (use JSON)
    # http://localhost:5000/api/cupcakes
    # {
    # 	"flavor" : "vanilla", 
    # 	"size" : "medium",
    # 	"rating" : 5.0, 
    # 	"image" : "https://tinyurl.com/demo-cupcake"
    # }

# TEST all routes (unittest) 
# createdb cupcakes_test
# (venv) $ python -m unittest -v tests