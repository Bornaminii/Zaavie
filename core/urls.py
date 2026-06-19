from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customer.urls')),
    path('manager/', include('manager.urls')),
    path('employees/', include('employee.urls')),
    path('reservation-system/', include('reservation_system.urls')),
    path('users/', include('customUser.urls')),
    path('payment/', include('payment.urls')),
]
