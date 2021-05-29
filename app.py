from flask import Flask, request, jsonify, render_template 
from models import db, connect_db, Cupcake 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'oh-so-super-very-secret'

connect_db(app) 
# db.create_all()