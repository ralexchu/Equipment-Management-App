from flask import request, jsonify
from config import app, db
from models import User, Checkout, Checkin

@app.route("/users", methods=['GET'])
def get_users():
    users = User.query.all()
    json_users = list(map(lambda x: x.to_json(), users))
    return jsonify({'users': json_users})

@app.route('/create_user/<int:user_id>', methods=['POST'])
def create_user():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']

    if not first_name or not last_name or not email:
        return jsonify({'message': 'Please provide all fields'}), 400
    
    new_user = User(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/update_user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    data = request.json 
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)
    
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
    return jsonify({'message': 'User deleted successfully'}), 200



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)