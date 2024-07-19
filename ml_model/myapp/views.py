from django.http import JsonResponse
import joblib
from django.views.decorators.csrf import ensure_csrf_cookie

loaded_pipeline = joblib.load('myapp/color_classifier.joblib')


@ensure_csrf_cookie
def predict_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        X_new = [text]
        predicted_output = loaded_pipeline.predict(X_new)
        return JsonResponse({'predicted_output': predicted_output[0]})
    return JsonResponse({'error': 'Invalid request'})