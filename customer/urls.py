from django.urls import path

from customer.views import customer_list_view, customer_detail_view


urlpatterns = [
    path('', customer_list_view),
    path('<int:id>', customer_detail_view),

]
