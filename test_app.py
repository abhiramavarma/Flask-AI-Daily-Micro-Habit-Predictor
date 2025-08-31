from app import app, db
from models import User, Habit, HabitLog
from predictor import HabitPredictor
import os

def test_database():
    with app.app_context():
        print("=== Database Test ===")
        users = User.query.all()
        print(f"Total users: {len(users)}")
        for user in users[:3]:  # Show first 3
            print(f"User: {user.username}, Habits: {len(user.habits)}")

        habits = Habit.query.filter_by(user_id=1).all()
        print(f"\nUser 1 habits: {len(habits)}")
        for habit in habits:
            print(f"- {habit.name} ({habit.category})")

        logs = HabitLog.query.filter_by(habit_id=habits[0].id).order_by(HabitLog.date).all()
        print(f"\nSample logs for {habits[0].name}: {len(logs)} entries")
        for log in logs[:5]:
            print(f"  {log.date}: {log.completed} ({log.time_of_day})")

def test_predictions():
    with app.app_context():
        print("\n=== Prediction Test ===")
        predictor = HabitPredictor()
        habits = Habit.query.filter_by(user_id=1).all()
        for habit in habits[:3]:  # Test first 3
            try:
                risk = predictor.predict_risk(habit.id)
                print(".1f")
            except Exception as e:
                print(f"Error predicting for {habit.name}: {e}")

def test_model_files():
    print("\n=== Model Files Test ===")
    files = ['habit_model.h5', 'label_encoders.pkl', 'scaler.pkl']
    for file in files:
        exists = os.path.exists(file)
        print(f"{file}: {'Exists' if exists else 'Missing'}")

if __name__ == '__main__':
    test_database()
    test_predictions()
    test_model_files()
    print("\n=== All Tests Completed ===")