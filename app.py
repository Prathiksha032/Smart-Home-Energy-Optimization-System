from flask import Flask, request, jsonify, redirect, url_for, session
from flask_cors import CORS
import joblib
import mysql.connector
import json
import pandas as pd
import time
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
CORS(app)

model = joblib.load("energy_model.pkl")
price_model = joblib.load("price_predictor.pkl")
COST_PER_UNIT = 8.5

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="smart_home"
    )

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Smart Home Login</title></head>
    <body style="font-family:Poppins,sans-serif;text-align:center;padding-top:100px">
        <h2>Welcome Home 🔦</h2>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <a href="/register">Sign up</a></p>
    </body>
    </html>
    '''

@app.route('/register')
def register():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Register</title></head>
    <body style="font-family:Poppins,sans-serif;text-align:center;padding-top:100px">
        <h2>Register</h2>
        <form method="POST" action="/signup">
            <input type="text" name="name" placeholder="Name" required>
            <input type="text" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Sign up</button>
        </form>
    </body>
    </html>
    '''

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = generate_password_hash(password)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                   (name, email, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['user_id']
        return redirect('/dashboard')
    else:
        return "<script>alert('Login failed!'); window.location.href='/';</script>"

@app.route('/dashboard')
def dashboard():
    return """<h2>Smart Home Dashboard</h2><p>Welcome user!</p><a href='/pay'>Go to Payment</a>"""

@app.route('/pay')
def pay():
    return open("payment.html").read()

@app.route('/process_mock_upi', methods=['POST'])
def process_mock_upi():
    data = request.get_json()
    user_id = session.get('user_id') or 1
    amount = data.get('amount')
    upi_app = data.get('upi_app')
    upi_id = data.get('upi_id')
    payment_status = data.get('payment_status', 'success')
    transaction_ref = "TXN" + str(int(time.time()))

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO payments (user_id, amount, payment_status, transaction_ref, upi_app, upi_id, payment_time)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
        """, (user_id, amount, payment_status, transaction_ref, upi_app, upi_id))
        conn.commit()
        return jsonify({"message": "Payment recorded"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route("/billing", methods=["GET"])
def billing():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(kwh_usage) FROM energy_usage")
        total_kwh = cursor.fetchone()[0] or 0
        total_cost = round(total_kwh * COST_PER_UNIT, 2)
        return jsonify({"total_kwh": total_kwh, "total_cost": total_cost})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        conn.close()

@app.route("/predict_price", methods=["GET"])
def predict_price():
    current_day = datetime.now().strftime("%a")
    current_temp = 30
    usage = 4.5
    hours = list(range(24))
    input_data = [{
        "hour": hour,
        "day": current_day,
        "temperature": current_temp,
        "past_usage": usage
    } for hour in hours]

    input_df = pd.DataFrame(input_data)
    predictions = price_model.predict(input_df)

    return jsonify({
        "hours": hours,
        "prices": [round(p, 2) for p in predictions]
    })

if __name__ == '__main__':
    app.run(debug=True)

