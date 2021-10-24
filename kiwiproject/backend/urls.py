from django.urls import path
from . import views

urlpatterns = [
    path('kiwi/', views.choose_flight, name="choose_flight"),
    path('kiwi/flight-info/', views.get_flight_info, name="flight_info")
]
