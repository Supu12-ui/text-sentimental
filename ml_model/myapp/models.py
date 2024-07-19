# myapp/models.py
import joblib
import os

class Prediction:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), 'color_classifier.joblib')
        self.model = joblib.load(model_path)