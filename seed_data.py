from database import db
from app import app
from models import User, Habit, HabitLog
from datetime import datetime, timedelta
import random

def create_synthetic_data():
    with app.app_context():
        db.create_all()

        # Default habits
        default_habits = [
            {'name': 'Drink Water', 'category': 'water'},
            {'name': 'Stretch', 'category': 'exercise'},
            {'name': 'Take a Walk', 'category': 'exercise'},
            {'name': 'Read 5 Minutes', 'category': 'reading'},
            {'name': 'Meditate', 'category': 'mindfulness'},
            {'name': 'Journal', 'category': 'writing'},
            {'name': 'Eat Healthy', 'category': 'nutrition'}
        ]

        # Create 20 users
        for i in range(1, 21):
            user = User(username=f'user{i}')
            db.session.add(user)
            db.session.commit()  # Commit to get user.id

            # Create habits for user
            for habit_data in default_habits:
                habit = Habit(name=habit_data['name'], category=habit_data['category'], user_id=user.id)
                db.session.add(habit)
            db.session.commit()

            # Generate logs for 30 days
            start_date = datetime.now().date() - timedelta(days=30)
            for day in range(30):
                current_date = start_date + timedelta(days=day)
                for habit in user.habits:
                    # Random completion: 70% chance
                    completed = random.random() < 0.7
                    time_of_day = random.choice(['morning', 'afternoon', 'evening'])
                    log = HabitLog(habit_id=habit.id, date=current_date, completed=completed, time_of_day=time_of_day)
                    db.session.add(log)
            db.session.commit()

if __name__ == '__main__':
    create_synthetic_data()
    print("Synthetic data created successfully!")