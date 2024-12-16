from flask import Flask, request, jsonify
from config import get_db_connection  # Import the connection function
from user_routes import user_bp 

app = Flask(__name__)
# Register the Blueprint for user routes
app.register_blueprint(user_bp)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API! Available endpoints: /users", 200


if __name__ == '__main__':
    app.run(debug=True)
