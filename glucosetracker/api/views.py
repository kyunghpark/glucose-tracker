from django.http import HttpResponse
from .models import GlucoseReading


def user(request, user_id):
    readings = GlucoseReading.objects.filter(user_id=user_id).order_by('timestamp')
    output = [reading.glucose_level for reading in readings]
    return HttpResponse(output)


def glucose_reading(request, reading_id):
    readings = GlucoseReading.objects.filter(id=reading_id).order_by('timestamp')
    output = [reading.glucose_level for reading in readings]
    return HttpResponse(output)


