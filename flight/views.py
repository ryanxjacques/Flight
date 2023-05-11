from django.http import HttpResponse
from django.http import JsonResponse
from flight.flightAPI import generate_flight

def index(request):
    return HttpResponse('Hello There')

def get_flight(request):
    data = generate_flight()
    return HttpResponse(data)
