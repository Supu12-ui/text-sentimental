# myapp/models.py
from django.db import models

class Prediction(models.Model):
    text = models.TextField()
    predicted_output = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
