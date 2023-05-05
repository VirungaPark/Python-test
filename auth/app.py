from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, decode_token
import os
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev')
jwt = JWTManager(app)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')

    if not username or not password or not role:
        return jsonify({'message': 'Invalid user creation'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        user = User(username=username, password=password, role=role)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 200
    else:
        return jsonify({'message': 'Username already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Invalid credentials'}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        if user.verify_password(password):
            access_token = create_access_token(identity=username)
            return jsonify({'access_token': access_token}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    else:
        return jsonify({'message': 'User not found'}), 401

@app.route('/verify-token')
def verify_token():
    json_data = request.get_json()
    try:
        access_token = json_data['access_token']
    except:
        return jsonify({'error': 'no access token sent'})
    decoded_token = decode_token(access_token)
    username = decoded_token['sub']
    app.logger.info(f"Access Token for user {username} is valid")
    return jsonify({'valid': True, 'username': username})

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')