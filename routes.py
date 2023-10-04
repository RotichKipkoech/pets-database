from flask import Flask, jsonify, request
from app import app
from flask_cors import CORS
from models import db, User, Services, Veterinary, PetItems, Pets


app = Flask(__name__)
CORS(app)  

# Route to get all users
## Get Method 
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    serialized_users = [{'id': user.id, 'username': user.username, 'email': user.email,
                         'password': user.password, 'phonenumber': user.phonenumber} for user in users]
    return jsonify({'users': serialized_users})

# Route to get all pets
@app.route('/pets', methods=['GET'])
def get_all_pets():
    pets = Pets.query.all()
    serialized_pets = [{'id': pet.id, 'name': pet.name, 'user_id': pet.user_id,
                        'veterinary_id': pet.veterinary_id, 'service_id': pet.service_id} for pet in pets]
    return jsonify({'pets': serialized_pets})

# Route to get all veterinary
@app.route('/veterinary', methods=['GET'])
def get_all_veterinary():
    veterinary = Veterinary.query.all()
    serialized_veterinary = [{'id': vet.id, 'name': vet.name, 'location': vet.location} for vet in veterinary]
    return jsonify({'veterinary': serialized_veterinary})

# Route to get all pet items
@app.route('/petitems', methods=['GET'])
def get_all_pet_items():
    pet_items = PetItems.query.all()
    serialized_pet_items = [{'id': item.id, 'item': item.item, 'price': item.price} for item in pet_items]
    return jsonify({'pet_items': serialized_pet_items})

@app.route('/services')
def get_all_services():
    services = Services.query.all()
    serialized_services = [{'id': service.id,'services_type': service.services_type,'veterinary_id': service.veterinary_id} for service in services]
    return jsonify({'services': serialized_services})

# users patch and get method 


# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()

    # Ensure required data is provided
    if 'username' not in user_data or 'email' not in user_data or 'password' not in user_data:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(email=user_data['email']).first()
    if existing_user:
        return jsonify({'message': 'User with this email already exists'}), 400

    new_user = User(
        username=user_data['username'],
        email=user_data['email'],
        password=user_data['password'],
        phonenumber=user_data.get('phonenumber')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201




@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    user = User.query.get(user_id)

    if user:
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.password = user_data.get('password', user.password)
        user.phonenumber = user_data.get('phonenumber', user.phonenumber)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'})

# Route to partially update a user using PATCH
@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    user_data = request.get_json()
    user = User.query.get(user_id)

    if user:
        if 'username' in user_data:
            user.username = user_data['username']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.password = user_data['password']
        if 'phonenumber' in user_data:
            user.phonenumber = user_data['phonenumber']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'})





if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
