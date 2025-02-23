import json
from flask import Flask, jsonify, request
import os
from computers_names import Computers
from datetime import datetime

computers = Computers()

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    """הוספת מידע למאגר"""

    data = request.get_json()

    # בדיקת תקינות הנתונים
    if (not data) or ('mac' not in data) or ('time' not in data) or ('data' not in data):
        return jsonify({'error': 'Invalid payload'}), 400
    if not isinstance(data['mac'], str) or not isinstance(data['time'], str) or not isinstance(data['data'], dict):
        return jsonify({'error': 'Invalid data format'}), 400

    # בדיקה שהזמן בפורמט הנדרש
    try:
        timestamp = datetime.strptime(data['time'], "%d-%m-%Y %H:%M:%S")
        file_name = timestamp.strftime("%d-%m-%Y")
    except ValueError:
        return jsonify({'error': 'Invalid time format'}), 400

    # בירור שם המשתמש של המחשב
    machine = computers.get_name(data['mac'])
    if not machine:
        computers.add(data['mac'])
        machine = computers.get_name(data['mac'])

    # הגדרת שם התיקייה ויצירתה במידת הצורך
    machine_folder = os.path.join('data', machine) # ?????????????????????????????????/
    os.makedirs(machine_folder, exist_ok=True)

    # עיצוב המידע והכנסתו לקובץ המתאים
    new_data = json.dumps({data['time']:data['data']})
    file_path = os.path.join(machine_folder, f'{file_name}.txt')
    try:
        with open(file_path, 'a', encoding="utf-8") as file:
            file.write(new_data + '\n')
        return jsonify({"status": "success", "file": file_name}), 200
    except Exception as e:
        return jsonify({'error': f'Error writing to file: {e}'}), 500

@app.route('/api/error', methods=['POST'])
def error():
    pass

if __name__ == '__main__':
    app.run(debug=True)


