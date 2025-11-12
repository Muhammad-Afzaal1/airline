from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Airport, Flight, Passenger
# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
        "flights":Flight.objects.all()
    })

def flight(request, flight_id):
    flight = get_object_or_404(Flight, id = flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html",{
        "flight":flight,
        "passengers":passengers,
        "non_passengers":Passenger.objects.exclude(flights = flight).all()
    })

def book(request, flight_id):
    
    if request.method == "POST":
        flight = Flight.objects.get(id = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=[flight_id]))
