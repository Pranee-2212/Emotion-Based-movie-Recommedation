from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

import os


from test_modedel import predict_emotion
from api_addressData import emotion_recommendations,movie_genres_id
from dotenv import load_dotenv
import datetime
import joblib
from API import get_movie_recommendation,get_emotion_index

load_dotenv()    


app = Flask(__name__)
loaded_model = joblib.load("model/emotion_detector_model.pkl")

def index():
    return "Welcome to the Emotion Detection API!"

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
    else:
        data =request.form
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    prediction =predict_emotion(text)
    index=get_emotion_index(prediction)
    movie_recommendation=get_movie_recommendation(index)
    json_data=jsonify({'emotion': prediction,'items_count':len(movie_recommendation),'movies':movie_recommendation})
    return render_template('result.html',emotion=prediction,item_count=len(movie_recommendation),movies=movie_recommendation)


if __name__ == '__main__':
    app.run(debug=True)
