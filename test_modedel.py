import joblib

# The loaded model is a pipeline that includes the vectorizer.

def predict_emotion(text):
    model = joblib.load('model/emotion_detector_model.pkl')
    """Predicts the emotion for a given text."""
    # The model's predict method expects an iterable (like a list) of documents.
    prediction = model.predict([text])[0]
    return prediction

# It's better to handle user input and validation outside the prediction function.

