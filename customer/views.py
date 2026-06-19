from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def customer_list_view(request):
    customers = [
        {
            "id": 1,
            "username": "borna"
        },
        {
            "id": 2,
            "username": "avin"
        },
        {
            "id": 3,
            "username": "sam"
        }
    ]
    return JsonResponse(customers, safe=False)


def customer_detail_view(request, id):
    customers = [
        {
            "id": 1,
            "username": "borna"
        },
        {
            "id": 2,
            "username": "avin"
        },
        {
            "id": 3,
            "username": "sam"
        }
    ]

    for customer in customers:
        if customer['id'] == id:
            return JsonResponse(customer, safe=False)
