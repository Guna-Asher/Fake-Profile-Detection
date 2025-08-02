# 🕵️‍♀️ Fake Profile Detection

**Detect suspicious Twitter accounts using AI-powered heuristics and live data streams.**

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://choosealicense.com/licenses/mit/)
[![Issues](https://img.shields.io/github/issues/Guna-Asher/Fake-Profile-Detection)](https://github.com/Guna-Asher/Fake-Profile-Detection/issues)
[![Stars](https://img.shields.io/github/stars/Guna-Asher/Fake-Profile-Detection?style=social)](https://github.com/Guna-Asher/Fake-Profile-Detection)

---

## 🧠 Overview

This educational project leverages machine learning and Twitter's API to analyze public profile data and predict the likelihood of a profile being fake. Built with Flask for a simple frontend, it showcases practical AI integration, environment security, and modular architecture.

---

## 🚀 Features

- 🔍 Real-time Twitter data scraping
- 🧠 ML-based heuristic profile evaluation
- 📦 Pretrained and switchable model architecture (`model.pkl` / `trained_model.pkl`)
- 🌐 Clean Flask-powered web interface
- 📄 Exportable prediction logs

---

## 📁 Project Structure

```
├── app.py
├── features.py
├── model.py
├── twitter_api.py
├── templates/
├── static/
├── requirements.txt
├── model.pkl
├── trained_model.pkl
├── .env (user-created)
└── README.md
```

---

## 🔐 Environment Setup

Environment variables are handled securely using a `.env` file. The project already supports `.env` loading via `python-dotenv`. To replicate:

1. **Create `.env` file** in root with your Twitter API keys:

   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

2. **Load variables** using:

   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()
   ```

3. **Ensure `.env` is ignored** in version control via `.gitignore`.

---

## 🧪 Usage

1. Clone and set up the project:
   ```bash
   git clone https://github.com/Guna-Asher/Fake-Profile-Detection.git
   cd Fake-Profile-Detection
   python -m venv venv
   source venv/bin/activate  # or venv\\Scripts\\activate on Windows
   pip install -r requirements.txt
   ```

2. Configure your `.env` file.

3. Launch:
   ```bash
   python app.py
   ```

4. Enter a Twitter username via the web interface to receive a prediction.

---

## 🤝 Contribution Guidelines

- Fork the repo and create a new feature branch
- Follow existing modular structure and clean code practices
- Submit pull requests with clear descriptions
- Open issues if bugs or enhancement ideas pop up

---

## 📢 Acknowledgments

Developed by [Guna Asher](https://github.com/Guna-Asher), blending ethical automation with user-centric design and AI/ML experimentation.
> “AI-powered tool to detect suspicious Twitter profiles using live data and heuristic modeling.”

Let me know if you want to add visual examples, installation GIFs, or even deployment instructions for Render or Railway!
