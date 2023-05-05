from flask_restful import Resource, reqparse
from models import db, Farmer

class FarmersResource(Resource):
    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        farmers = Farmer.query.all()
        result = []
        for farmer in farmers:
            result.append({"id": farmer.id, "first_name": farmer.first_name, "last_name": farmer.last_name})
        return {"farmers": result}, 200

class FarmerResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str, required=True, help="First name cannot be blank!")
    parser.add_argument('middle_name', type=str)
    parser.add_argument('last_name', type=str, required=True, help="Last name cannot be blank!")
    parser.add_argument('gender', type=str, choices=["M","F","U"])
    parser.add_argument('phone', type=str)
    parser.add_argument('address', type=str)
    parser.add_argument('cooperative_name', type=str)
    parser.add_argument('certification', type=str, choices=["organic", "fairtrade", "rain forest standard"])

    def __init__(self) -> None:
        super().__init__()
    
    def get(self, id):
        farmer = Farmer.query.filter_by(id=id).first()
        if not farmer:
            return {"message": f"Farmer with id {id} not found."}, 404
        return {"id": farmer.id, "first_name": farmer.first_name, "last_name": farmer.last_name}, 200
    
    def put(self, id):
        farmer = Farmer.query.filter_by(id=id).first()
        if not farmer:
            return {"message": f"Farmer with id {id} not found."}, 404
        data = FarmerResource.parser.parse_args()
        farmer.first_name = data['first_name']
        farmer.last_name = data['last_name']
        db.session.commit()
        return {"message": "Updated farmer successfully."}, 201
    
    def post(self):
        data = FarmerResource.parser.parse_args()
        farmer = Farmer(**data)
        db.session.add(farmer)
        db.session.commit()
        return {"message": "Added farmer successfully."}, 201
    
    def delete(self, id):      
        farmer = Farmer.query.filter_by(id=id).first()
        if not farmer:
            return {"message": f"Farmer with id {id} not found."}, 404
        db.session.delete(farmer)
        db.session.commit()
        return {"message": "Farmer with id {id} deleted successfully."}, 200  