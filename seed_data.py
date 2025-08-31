from database import db
from app import app
from models import User, Habit, HabitLog
from datetime import datetime, timedelta
import random

DEFAULT_HABITS = [
    {'name': 'Drink Water', 'category': 'water'},
    {'name': 'Stretch', 'category': 'exercise'},
    {'name': 'Take a Walk', 'category': 'exercise'},
    {'name': 'Read 5 Minutes', 'category': 'reading'},
    {'name': 'Meditate', 'category': 'mindfulness'},
    {'name': 'Journal', 'category': 'writing'},
    {'name': 'Eat Healthy', 'category': 'nutrition'}
]

def create_synthetic_data():
    with app.app_context():
        db.create_all()

        for i in range(1, 21):
            user = User(username=f'user{i}')
            db.session.add(user)
            db.session.commit()

            for habit_data in DEFAULT_HABITS:
                habit = Habit(name=habit_data['name'], category=habit_data['category'], user_id=user.id)
                db.session.add(habit)
            db.session.commit()

            start_date = datetime.now().date() - timedelta(days=30)
            for day in range(30):
                current_date = start_date + timedelta(days=day)
                for habit in user.habits:
                    completed = random.random() < 0.7
                    time_of_day = random.choice(['morning', 'afternoon', 'evening'])
                    log = HabitLog(habit_id=habit.id, date=current_date, completed=completed, time_of_day=time_of_day)
                    db.session.add(log)
            db.session.commit()

if __name__ == '__main__':
    create_synthetic_data()
    print("Synthetic data created successfully!")