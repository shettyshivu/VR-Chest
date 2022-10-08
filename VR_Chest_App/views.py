from django.shortcuts import render
from django.http import HttpResponse
# import googlemaps
# import pandas as pd

# Create your views here.
def home(request):
    # gmaps = googlemaps.Client(key='AIzaSyBm-YWWx-RNETQ6bX_LDm2eARqaxQ63g3Y')
    # place_id = 'ChIJMZTIbdkXrjsRb5gaMwqs7QM'
    # place = gmaps.place(place_id=place_id)
    # print(place ['result']['reviews'])
    return render(request,'home.html')