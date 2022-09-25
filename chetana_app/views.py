from django.shortcuts import render
from django.http import HttpResponse

from chetana_app.models import Upcoming_event, Event

# Create your views here.

def home(request):
    return render(request,'home.html')

def team(request):
    return render(request,'team.html')

def upcomingevent(request):
    

    obj = Upcoming_event.objects.all()

    return render(request,'upcomingevent.html', {'obj': obj})

def events(request):

    
    events= Event.objects.all()
    
    return render(request,'events.html', {'events': events})
