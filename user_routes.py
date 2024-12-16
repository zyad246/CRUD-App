from flask import Blueprint, request, jsonify
import pyodbc
from config import DATABASE_CONNECTION_STRING

# Create Blueprint for user routes
user_bp = Blueprint('users', __name__)

# Helper: Establish database connection
def get_db_connection():
    return pyodbc.connect(DATABASE_CONNECTION_STRING)

# CRUD Routes
@user_bp.route('/', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route('/', methods=['GET'])
def get_users():
    """Retrieve all users."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM Users")
        users = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's name."""
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Users SET name = ? WHERE id = ?", (name, user_id))
        conn.commit()
        conn.close()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({"message": "User updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({"message": "User deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
