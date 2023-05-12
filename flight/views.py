from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from flight.flightAPI import generate_flight

def intro_view(request):
    return render(request, 'intro.html')

def main_view(request):
    return render(request, 'main.html')

def get_flight(request):
    data = generate_flight()
    return JsonResponse(data)
