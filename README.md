# Flask AI Daily Micro-Habit Predictor

A Flask web application that uses TensorFlow to predict which micro-habits a user is most likely to skip today, providing personalized nudges for better habit formation.

## Features

- **Predictive Analytics**: TensorFlow/Keras model predicts skip risk for daily habits
- **Personalized Nudges**: Get actionable reminders for high-risk habits
- **Custom Habits**: Add your own habits and retrain the model
- **Dashboard**: Visualize habit streaks and risk analytics with Chart.js
- **Responsive Design**: Built with Tailwind CSS for mobile-friendly interface

## Tech Stack

- **Backend**: Flask, Python
- **Database**: SQLite with SQLAlchemy
- **ML**: TensorFlow/Keras for habit prediction
- **Frontend**: HTML, Tailwind CSS, Chart.js
- **Deployment**: Vercel

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abhiramavarma/Flask-AI-Daily-Micro-Habit-Predictor.git
cd Flask-AI-Daily-Micro-Habit-Predictor
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Usage

1. **Home Page**: Introduction to the app
2. **Dashboard**: View habit predictions and personalized nudges
3. **Add Custom Habits**: Extend the app with your own habits
4. **Retrain Model**: Update predictions with new data

## Model Details

- **Algorithm**: Dense Neural Network with TensorFlow/Keras
- **Features**: Habit category, time of day, current streak, day of week
- **Target**: Probability of skipping the habit
- **Training Data**: Synthetic data (20 users × 7 habits × 30 days)

## Deployment

This app is configured for deployment on Vercel:

1. Push to GitHub
2. Connect repository to Vercel
3. Deploy automatically

## Project Structure

```
├── app.py                 # Main Flask application
├── models.py              # Database models
├── predictor.py           # ML prediction logic
├── database.py            # Database configuration
├── seed_data.py           # Synthetic data generation
├── train.py               # Model training script
├── test_app.py            # Testing utilities
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   └── dashboard.html
├── static/                # Static files (CSS, JS)
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel deployment config
└── README.md
```

## License

MIT License - feel free to use this project for learning and development.