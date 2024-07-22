from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import joblib
import numpy as np

loaded_pipeline = joblib.load('myapp/color_classifier.joblib')

@csrf_exempt
def predict_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            texts = data.get('text', '')

            if texts:
                predictions = []
                for text in texts:
                    X_new = [text]
                    output = loaded_pipeline.predict(X_new)
                    predicted_output = int(output)  
                    if predicted_output == 2:
                        color = 'white'
                    elif predicted_output == 3:
                        color = 'yellow'
                    elif predicted_output == 4:
                        color = 'orange'
                    elif predicted_output == 5:
                        color = 'red'
                    else:
                        color = 'saffron'

                    predictions.append({'color_id': predicted_output,'prediction': color})

                return JsonResponse({'predictions': predictions}, status=200)
            else:
                return JsonResponse({'error': 'Text field is empty'}, status=400)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
