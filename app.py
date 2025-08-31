from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db.init_app(app)

# Import models after db is defined
from models import User, Habit, HabitLog
from predictor import HabitPredictor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    user_id = 1  # Assume user1
    habits = Habit.query.filter_by(user_id=user_id).all()
    predictor = HabitPredictor()
    risks = []
    for habit in habits:
        risk = predictor.predict_risk(habit.id)
        risks.append({'habit': habit, 'risk': risk})
    risks.sort(key=lambda x: x['risk'], reverse=True)
    top_nudge = risks[0] if risks else None
    return render_template('dashboard.html', risks=risks, top_nudge=top_nudge)

@app.route('/add_habit', methods=['POST'])
def add_habit():
    name = request.form['name']
    category = request.form['category']
    user_id = 1
    habit = Habit(name=name, category=category, user_id=user_id, is_default=False)
    db.session.add(habit)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/retrain')
def retrain():
    predictor = HabitPredictor()
    predictor.train_model()
    return redirect(url_for('dashboard'))

# For Vercel deployment
application = app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)