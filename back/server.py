import json
from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_FILE = "data.json"

# פונקציה לטעינת הנתונים מהקובץ
def load_items():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# פונקציה לשמירת הנתונים לקובץ
def save_items(items):
    with open(DATA_FILE, "w") as file:
        json.dump(items, file, indent=4)

# אתחול הרשימה מהקובץ
items = load_items()

# מסלול GET - קבלת כל הפריטים
@app.route('/items', methods=['GET'])
def get_items():
    # return jsonify(items), 200
    pass

# data = {'mac':str,"time":str,'data':str}

# מסלול POST - הוספת פריט חדש ושמירה
@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    new_item = {'id': len(items) + 1, 'name': data['name']}
    items.append(new_item)
    save_items(items)  # שמירת הנתונים לקובץ
    return jsonify(new_item), 201

# מסלול PUT - עדכון פריט ושמירה
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # data = request.json
    # for item in items:
    #     if item['id'] == item_id:
    #         item['name'] = data.get('name', item['name'])
    #         save_items(items)  # שמירת הנתונים
    #         return jsonify(item), 200
    # return jsonify({'error': 'Item not found'}), 404
    pass

# מסלול DELETE - מחיקת פריט ושמירה
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # global items
    # items = [item for item in items if item['id'] != item_id]
    # save_items(items)  # שמירת הנתונים לאחר מחיקה
    # return jsonify({'message': 'Item deleted'}), 200
    pass
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)