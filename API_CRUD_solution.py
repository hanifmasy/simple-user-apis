from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy user data for testing
users = [
    {"user_id": 1, "first_name": "Name1", "last_name": "Last", "email": "name1@gmail.com"},
    {"user_id": 2, "first_name": "Name2", "last_name": "Last", "email": "name2@gmail.com"}
]

# Route for creating a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.json
    if not all(key in new_user for key in ('user_id', 'first_name', 'last_name', 'email')):
        return jsonify({'error': 'Missing user data'}), 400

    users.append(new_user)
    return jsonify({'message': 'User created successfully'}), 201

# Route for retrieving all users
@app.route('/api/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

# Route for retrieving a single user by user_id
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['user_id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Route for updating an existing user by user_id
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['user_id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    for key, value in data.items():
        if key != 'user_id':
            user[key] = value

    return jsonify({'message': 'User updated successfully'})

# Route for deleting a user by user_id
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['user_id'] != user_id]
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
