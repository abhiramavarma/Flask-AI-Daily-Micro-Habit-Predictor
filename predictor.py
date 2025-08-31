import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
import joblib
from database import db
from models import HabitLog, Habit
from datetime import datetime, timedelta

class HabitPredictor:
    def __init__(self):
        self.model = None
        self.label_encoders = {}
        self.scaler = StandardScaler()

    def load_data(self):
        # Load data from database
        logs = HabitLog.query.all()
        data = []
        for log in logs:
            habit = log.habit
            # Calculate streak
            streak = self.calculate_streak(habit.id, log.date)
            data.append({
                'habit_id': habit.id,
                'category': habit.category,
                'time_of_day': log.time_of_day,
                'streak': streak,
                'day_of_week': log.date.weekday(),
                'completed': 1 if log.completed else 0
            })
        return pd.DataFrame(data)

    def calculate_streak(self, habit_id, date):
        # Calculate consecutive completions before this date
        streak = 0
        current_date = date - timedelta(days=1)
        while True:
            log = HabitLog.query.filter_by(habit_id=habit_id, date=current_date).first()
            if log and log.completed:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break
        return streak

    def preprocess_data(self, df):
        # Encode categorical
        for col in ['category', 'time_of_day']:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
                df[col] = self.label_encoders[col].fit_transform(df[col])
            else:
                df[col] = self.label_encoders[col].transform(df[col])

        # Features
        X = df[['category', 'time_of_day', 'streak', 'day_of_week']]
        y = df['completed']

        # Scale
        X_scaled = self.scaler.fit_transform(X)
        return X_scaled, y

    def train_model(self):
        df = self.load_data()
        X, y = self.preprocess_data(df)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = Sequential([
            Dense(64, activation='relu', input_shape=(X.shape[1],)),
            Dropout(0.2),
            Dense(32, activation='relu'),
            Dropout(0.2),
            Dense(1, activation='sigmoid')
        ])

        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

        # Save model and encoders
        self.model.save('habit_model.h5')
        joblib.dump(self.label_encoders, 'label_encoders.pkl')
        joblib.dump(self.scaler, 'scaler.pkl')

    def predict_risk(self, habit_id):
        if not self.model:
            self.load_model()

        habit = Habit.query.get(habit_id)
        today = datetime.now().date()
        streak = self.calculate_streak(habit_id, today)

        # Assume morning for prediction, can be dynamic
        time_of_day = 'morning'
        day_of_week = today.weekday()

        data = pd.DataFrame([{
            'category': habit.category,
            'time_of_day': time_of_day,
            'streak': streak,
            'day_of_week': day_of_week
        }])

        for col in ['category', 'time_of_day']:
            data[col] = self.label_encoders[col].transform(data[col])

        X = self.scaler.transform(data[['category', 'time_of_day', 'streak', 'day_of_week']])
        prob = self.model.predict(X)[0][0]
        return 1 - prob  # Risk of skipping

    def load_model(self):
        from tensorflow.keras.models import load_model
        self.model = load_model('habit_model.h5')
        self.label_encoders = joblib.load('label_encoders.pkl')
        self.scaler = joblib.load('scaler.pkl')