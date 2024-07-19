from rest_framework import serializers
from .models import Prediction

class PredictionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prediction
    fields = ('text', 'prediction', 'created_at')  # Adjust fields as needed
