from django.contrib import admin
from .models import Upcoming_event, Event

# Register your models here.

admin.site.register(Event)
admin.site.register(Upcoming_event)