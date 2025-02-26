שם הפרויקט: 

flask
flask_cors
dotenv
requests
keyboard
getmac

pip install flask flask-cors python-dotenv requests keyboard getmac



server requests: - בקשות שרת

    POST requests: - בקשות העלאה
        /api/upload - העלאת מידע מהמחשב שבמעקב
        /api/login - כניסת משתמש

    GET requests: - בקשות הורדה: קבלת נתונים
        /api/get_machines_names - קבלת שמות המחשבים שבמעקב
        /api/get_dates_by_name/<name> - קבלת שמות הקבצים (קובץ לכל יום מעקב) של מחשב מסוים
        /api/get_keystrokes_by_name_and_date/<name>/<date> - קבלת ההקלדות של מחשב מסוים ביום מסוים


.env file: - הגדרת משתנים הנצרכת בקובץ נסתר

    DECRYPTION_KEY = "" - מפתח ההצפנה לצורך פענוח, חובה
    BASE_DIR = "" - optional (else: "data") - נתיב לתיקיית הבסיס ששם מאוחסן המידע שנאסף



.env file: - הגדרת משתנים הנצרכת בקובץ נסתר

    URL = "" - url :כתובת של השרת
    encryption_key = "" - מפתח ההצפנה