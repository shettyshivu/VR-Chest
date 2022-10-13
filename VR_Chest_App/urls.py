from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('saveFeedback/',views.saveFeedback, name='saveFeedback'),
    path('book-appointment', views.appointment, name='book-appointment'),
    path('Appointment-confirm', views.appointmentConfirm, name='Appointment-confirm')
]