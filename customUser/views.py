from django.shortcuts import render
from django.http import JsonResponse

def user_list_view(request):
    users = [
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

    return JsonResponse(users, safe=False)


def user_detail_view(request, id):
    
    users = [
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

    for user in users:
        if user['id'] == id:
            return JsonResponse(user, safe=False)