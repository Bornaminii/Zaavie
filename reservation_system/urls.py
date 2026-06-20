from django.urls import path
from reservation_system.views import available_seats_list, seat_availability_view


urlpatterns = [
    path('', available_seats_list),
    path('<str:status>/', seat_availability_view)
]
