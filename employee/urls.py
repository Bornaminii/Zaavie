from django.urls import path
from employee.views import employee_detail_view, employee_list_view

urlpatterns = [
    path('', employee_list_view),
    path('<int:id>', employee_detail_view),
]
