# simple-user-apis

### API Application User CRUD
I have designed a simple API using Python and Flask framework. Below is the implementation in `API_CRUD_solution.py`:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy user data for testing
users = [
    {"user_id": 1, "first_name": "Name1", "last_name": "Last1", "email": "name1@gmail.com"},
    {"user_id": 2, "first_name": "Name2", "last_name": "Last2", "email": "name2@gmail.com"}
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
```

Explanation:

- I've created a Flask application and defined routes for various CRUD operations on user data.
- The `/api/users` endpoint supports POST for creating a new user and GET for retrieving all users.
- The `/api/users/<int:user_id>` endpoint supports GET for retrieving a single user, PUT for updating an existing user, and DELETE for deleting a user.
- Proper error handling is implemented to handle cases such as missing data or user not found.
- Input validation is performed to ensure required fields are present for creating a new user.
- The application runs in debug mode to facilitate development and debugging.




#### Setting Up and Running the User Management API

This guide will walk you through the process of setting up and running the User Management API using Python and Flask.

##### Prerequisites

- Python installed on your machine
- pip package manager
- Flask framework

##### Installation

1. **Clone the Repository:**

   Copy and paste the source code `API_CRUD_solution.py` to your local project directory.


2. **Install Dependencies:**

   Navigate to your project directory and install the required dependencies using pip.

   ```bash
   cd your-project-directory
   pip install flask
   ```

##### Running the API

1. **Start the Flask Application:**

   Run the following command to start the Flask application.

   ```bash
   python API_CRUD_solution.py
   ```

   This will start the Flask development server, and you should see output indicating that the server is running.

2. **Accessing the API:**

   Once the server is running, you can access the API endpoints using tools like cURL, Postman, or your web browser.

   - **Creating a new user:** Send a POST request to `/api/users` with JSON data containing the user details.
   - **Retrieving all users:** Send a GET request to `/api/users`.
   - **Retrieving a single user:** Send a GET request to `/api/users/{user_id}`, replacing `{user_id}` with the ID of the user you want to retrieve.
   - **Updating a user:** Send a PUT request to `/api/users/{user_id}` with JSON data containing the updated user details.
   - **Deleting a user:** Send a DELETE request to `/api/users/{user_id}` to delete the user with the specified ID.

##### Example Usage

- **Creating a new user:**

  ```bash
  curl -X POST http://localhost:5000/api/users -H "Content-Type: application/json" -d '{"user_id":3,"first_name":"Hanif","last_name": "Masykuri", "email": "hanif@gmail.com"}'
  ```

- **Retrieving all users:**

  ```bash
  curl http://localhost:5000/api/users
  ```

- **Retrieving a single user:**

  ```bash
  curl http://localhost:5000/api/users/3
  ```

- **Updating a user:**

  ```bash
  curl -X PUT http://localhost:5000/api/users/3 -H "Content-Type: application/json" -d '{"first_name": "Budi", "last_name": "Satya"}'
  ```

- **Deleting a user:**

  ```bash
  curl -X DELETE http://localhost:5000/api/users/3
  ```

