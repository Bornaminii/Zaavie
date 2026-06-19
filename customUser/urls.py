from django.urls import path, include
from .views import user_list_view, user_detail_view

urlpatterns = [
    path('', user_list_view),
    path('<int:id>', user_detail_view)
]
