from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def employee_list_view(request):
    employees = [
        {
            "id": 1,
            "username": "borna emp"
        },
        {
            "id": 2,
            "username": "avin emp"
        },
        {
            "id": 3,
            "username": "sam emp"
        }
    ]
    return JsonResponse(employees, safe=False)


def employee_detail_view(request, id):
    employees = [
        {
            "id": 1,
            "username": "borna emp"
        },
        {
            "id": 2,
            "username": "avin emp"
        },
        {
            "id": 3,
            "username": "sam emp"
        }
    ]
    for employee in employees:
        if employee['id'] == id:
            return JsonResponse(employees['id'], safe=False)
