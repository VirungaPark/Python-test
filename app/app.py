from flask import Flask, jsonify
from flask_restful import Api
from models import db
from farmer import FarmerResource, FarmersResource

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev')
api = Api(app)

db.init_app(app)
with app.app_context():
    db.create_all()

api.add_resource(FarmerResource, '/farmer', '/farmer/<int:id>')
api.add_resource(FarmersResource, '/farmers')

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "The requested resource could not be found."}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"message": "An internal server error occurred."}), 500