from predictor import HabitPredictor
from app import app

with app.app_context():
    predictor = HabitPredictor()
    predictor.train_model()
    print("Model trained and saved!")