# 🏠 Smart Home Energy Optimization System

A Machine Learning-powered Smart Home Energy Optimization System that predicts energy consumption, estimates electricity prices, and helps users monitor household energy usage through an interactive web dashboard.

---

## 🚀 Features

- 🔐 User Authentication (Login & Signup)
- 📊 Smart Energy Monitoring Dashboard
- ⚡ Electricity Usage Analysis
- 💰 Billing Management
- 💳 Mock UPI Payment Integration
- 📈 Electricity Price Prediction using Machine Learning
- 🧠 Energy Consumption Prediction
- 📜 Usage History Tracking
- 🗄️ MySQL Database Integration

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning
- Scikit-learn
- Pandas
- Joblib

### Database
- MySQL

---

## 📂 Project Structure

```
Smart-Home-Energy-Optimization-System
│
├── app.py
├── requirements.txt
├── energy_data.csv
├── energy_model.pkl
├── price_data.csv
├── price_predictor.pkl
├── train_model.py
├── train_price_model.py
│
├── static
│   ├── style.css
│   ├── billing.css
│   ├── stl.css
│   ├── billing.js
│   └── dashboard.js
│
└── templates
    ├── index.html
    ├── dashboard.html
    ├── billing.html
    ├── history.html
    ├── payment.html
    └── register.html
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Prathiksha032/Smart-Home-Energy-Optimization-System.git
```

Move into the project

```bash
cd Smart-Home-Energy-Optimization-System
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning

The system uses trained machine learning models to

- Predict household energy consumption
- Estimate electricity prices
- Improve energy efficiency recommendations

Models included

- `energy_model.pkl`
- `price_predictor.pkl`

---

## 🗃️ Database

Create a MySQL database

```sql
CREATE DATABASE smart_home;
```

Update the database credentials inside `app.py`

```python
host="localhost"
user="root"
password=""
database="smart_home"
```

---

## 📌 Future Enhancements

- IoT Sensor Integration
- Real-time Energy Monitoring
- AI-based Energy Saving Suggestions
- Cloud Deployment
- Mobile Responsive UI
- Admin Dashboard
- Email Notifications

---

## 👩‍💻 Author

**Prathiksha B**

Computer Science Engineering Student

GitHub

https://github.com/Prathiksha032

---

## ⭐ If you found this project useful, consider giving it a Star!
