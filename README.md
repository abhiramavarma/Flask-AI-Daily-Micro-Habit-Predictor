# Flask AI Daily Micro-Habit Predictor

A sophisticated Flask web application that leverages machine learning to predict which daily micro-habits users are most likely to skip, delivering personalized behavioral nudges to improve habit formation and consistency.

## 🚀 Features

- **AI-Powered Predictions**: TensorFlow/Keras neural network predicts skip probability for each habit
- **Personalized Nudges**: Intelligent reminders for high-risk habits with confidence scores
- **Custom Habit Support**: Add personalized habits and retrain the model dynamically
- **Interactive Dashboard**: Real-time analytics with Chart.js visualizations
- **Responsive Design**: Mobile-first UI built with Tailwind CSS
- **Synthetic Dataset**: Pre-populated with 20 users × 7 habits × 30 days of realistic data

## 🛠 Tech Stack

- **Backend**: Flask 2.3+, Python 3.8+
- **Database**: SQLite with SQLAlchemy ORM
- **Machine Learning**: TensorFlow 2.x, Keras, scikit-learn
- **Frontend**: HTML5, Tailwind CSS, Chart.js
- **Deployment**: Vercel (serverless)

## 📊 Model Architecture

### Neural Network Design
- **Input Layer**: 4 features (habit category, time of day, current streak, day of week)
- **Hidden Layers**: 64 neurons → 32 neurons with dropout regularization
- **Output Layer**: Sigmoid activation for binary classification
- **Loss Function**: Binary cross-entropy
- **Optimizer**: Adam with default learning rate

### Feature Engineering
- **Categorical Encoding**: Label encoding for habit categories and time slots
- **Temporal Features**: Day of week, current completion streak
- **Normalization**: Standard scaling for numerical features

### Performance Metrics
- **Accuracy**: ~70% on synthetic dataset
- **Training**: 10 epochs with early stopping
- **Validation**: 20% holdout split

## 🏃 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/abhiramavarma/Flask-AI-Daily-Micro-Habit-Predictor.git
cd Flask-AI-Daily-Micro-Habit-Predictor
```

2. **Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Initialize database and train model**
```bash
python seed_data.py  # Generate synthetic data
python train.py      # Train the ML model
```

5. **Launch the application**
```bash
python app.py
```

6. **Access the app**
Open `http://127.0.0.1:5000` in your browser

## 🎯 Usage Guide

### Dashboard Features
- **Risk Assessment**: View predicted skip probabilities for all habits
- **Priority Nudges**: Get immediate reminders for high-risk habits
- **Progress Tracking**: Monitor completion streaks and patterns
- **Custom Habits**: Add new habits with category classification

### Model Training
- **Automatic Training**: Model retrains when new habits are added
- **Incremental Learning**: Incorporates user behavior patterns
- **Performance Monitoring**: Tracks prediction accuracy over time

## 📁 Project Structure

```
├── app.py                 # Main Flask application with routes
├── models.py              # SQLAlchemy database models
├── predictor.py           # ML prediction engine
├── database.py            # Database configuration
├── seed_data.py           # Synthetic data generation
├── train.py               # Model training script
├── test_app.py            # Comprehensive testing suite
├── templates/             # Jinja2 HTML templates
│   ├── base.html         # Layout template
│   ├── index.html        # Landing page
│   └── dashboard.html    # Main dashboard
├── static/               # Static assets (CSS, JS)
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel deployment config
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🚀 Deployment

### Vercel (Recommended)

1. **Connect Repository**
   - Import project from GitHub to Vercel
   - Vercel auto-detects Python/Flask configuration

2. **Environment Variables** (if needed)
   - Set `PYTHON_VERSION` to `3.9` or higher
   - Configure any custom environment variables

3. **Deploy**
   - Vercel handles build and deployment automatically
   - Access your live app at the generated URL

### Manual Deployment

For other platforms, ensure:
- Python 3.8+ runtime
- All dependencies from `requirements.txt`
- Environment variables configured
- Static file serving enabled

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_app.py
```

Tests cover:
- Database integrity
- Model predictions
- File system checks
- API endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📈 Future Enhancements

- [ ] User authentication and multi-user support
- [ ] Advanced ML models (LSTM for time series)
- [ ] Mobile app companion
- [ ] Integration with habit tracking APIs
- [ ] Advanced analytics and insights
- [ ] Social features and challenges

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- TensorFlow/Keras for the ML framework
- Flask community for the web framework
- Tailwind CSS for the styling framework
- Chart.js for data visualization

---

**Built with ❤️ for habit enthusiasts and data scientists**