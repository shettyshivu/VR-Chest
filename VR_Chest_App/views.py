from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback, Appointment
# import googlemaps
# import pandas as pd

# Create your views here.
def home(request):
    # gmaps = googlemaps.Client(key='AIzaSyBm-YWWx-RNETQ6bX_LDm2eARqaxQ63g3Y')
    # place_id = 'ChIJMZTIbdkXrjsRb5gaMwqs7QM'
    # place = gmaps.place(place_id=place_id)
    # print(place ['result']['reviews'])
    return render(request,'home.html')

def saveFeedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        obj = Feedback (Name = name, Email=email, Messege=msg)
        obj.save()
    return render(request,'home.html')

def appointment(request):
    return render(request, 'appointment.html')

def appointmentConfirm(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('mobileno')
        email=request.POST.get('email')
        date=request.POST.get('date')
        time=request.POST.get('time')
        doctor=request.POST.get('doctor')
        obj= Appointment(Name=name,Mobileno=contact, Email=email, Date=date, Time=time, Doctor=doctor)
        obj.save()
    return render(request, 'home.html')
