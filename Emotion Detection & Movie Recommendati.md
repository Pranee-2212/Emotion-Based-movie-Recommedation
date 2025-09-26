# Emotion Detection & Movie Recommendation Flask App

## Project Description

This project is a Flask-based web application that detects the emotion from user input text and recommends movies based on the detected emotion. The app uses a pre-trained machine learning model to analyze the input and leverages movie data to provide personalized recommendations.

### Features

- **Emotion Detection:** Enter any text, and the app predicts the underlying emotion.
- **Movie Recommendations:** Based on the detected emotion, the app suggests a curated list of movies.
- **User-Friendly Interface:** Simple web interface for input and displaying results.
- **Dynamic Results:** Movie details including title, release date, overview, and poster are shown.

### How It Works

1. The user enters text on the homepage.
2. The backend predicts the emotion using a trained model.
3. The app fetches movies related to the emotion and displays them on a results page.

### Technologies Used

- Python 3
- Flask
- joblib (for loading ML models)
- HTML/CSS (for frontend)
- dotenv (for environment variables)

### Getting Started

1. **Clone the repository**
2. **Create a virtual environment**
   ```
   python -m venv venv
   ```
3. **Activate the virtual environment**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
5. **Run the app**
   ```
   python app.py
   ```
6. **Open your browser and go to**
   ```
   http://127.0.0.1:5000/
   ```

### Folder Structure

- `app.py` - Main Flask application
- `templates/` - HTML templates (`home.html`, `result.html`)
- `model/` - Pre-trained emotion detection model
- `API.py`, `test_modedel.py`, etc. - Supporting modules

### License

This project is for educational purposes.
