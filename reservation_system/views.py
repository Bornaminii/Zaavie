from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def available_seats_list(request):

    seats = [
        {
            'id': 1,
            'status': False
        },
        {
            'id': 2,
            'status': True
        },
        {
            'id': 3,
            'status': True
        },
    ]

    return JsonResponse(seats, safe=False)


def seat_availability_view(request, status):

    seats = [
        {
            'id': 1,
            'status': False
        },
        {
            'id': 2,
            'status': True
        },
        {
            'id': 3,
            'status': True
        },
    ]

    results = []

    if status.lower() == "available":
        for seat in seats:
            if seat['status'] == True:
                results.append(seat)
    elif status.lower() == "unavailable":
        for seat in seats:
            if seat['status'] == False:
                results.append(seat)

    return JsonResponse(results, safe=False)
