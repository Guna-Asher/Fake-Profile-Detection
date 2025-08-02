# 🕵️‍♂️ Fake Profile Detection

A Python-based project aimed at identifying fake profiles on Twitter using machine learning and heuristic analysis. Designed for educational purposes, this tool demonstrates data scraping, preprocessing, model training, and deployment in a real-world context.

## 🚀 Features

- Twitter API integration for live user data
- Pretrained ML model for classifying fake vs. real profiles
- Modular architecture with separate feature extraction and inference layers
- Web interface built with Flask for easy interaction
- Exportable predictions and logs for further analysis

## 🧠 Tech Stack

- **Frontend**: HTML, CSS (via Flask templates)
- **Backend**: Python, Flask
- **ML Tools**: scikit-learn, custom feature engineering
- **Model Storage**: `model.pkl`, `trained_model.pkl`
- **API**: Twitter API via Tweepy

## 📁 Structure

```
├── static/                 # Static files (CSS, JS)
├── templates/              # HTML templates
├── app.py                  # Flask app driver
├── features.py             # Feature extraction logic
├── model.py                # Model loading and prediction
├── model.pkl               # Pretrained ML model
├── trained_model.pkl       # Alternative trained model
├── twitter_api.py          # Twitter data scraping
├── requirements.txt        # Dependencies list
└── README.md               # Project documentation
```

## 🧪 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/Guna-Asher/Fake-Profile-Detection.git
   cd Fake-Profile-Detection
   ```

2. **Set up your virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Twitter API keys**
   Add your credentials inside `twitter_api.py`.

5. **Run the app**
   ```bash
   python app.py
   ```

## 🎯 Usage

Enter a Twitter handle into the web interface, and the model will analyze various metrics including tweet frequency, follower count, profile completeness, and more to predict authenticity.

## ⚠️ Disclaimer

This project is intended for educational use only. It does not guarantee accurate or ethical judgments and should not be used for mass classification or public exposure.

## 💡 Credits

Developed by [Guna Asher](https://github.com/Guna-Asher), with a focus on AI-driven automation, accessible interfaces, and thoughtful user-centric design.
