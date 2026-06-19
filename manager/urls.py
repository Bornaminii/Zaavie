from django.urls import path
from manager.views import manager_name_view


urlpatterns = [
    path('manager/', manager_name_view)
]
