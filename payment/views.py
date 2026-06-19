from django.http import JsonResponse
from django.shortcuts import render

def payment_list_view(request):

    payments = [
        {
            'id':1,
            'amount':2000,
            'action': 'withdraw'
        },
        {
            'id':2,
            'amount':3000,
            'action': 'deposit'
        }
    ]

    return JsonResponse(payments, safe=False)


def payment_detail_view(request, action):

    payments = [
        {
            'id':1,
            'amount':2000,
            'action': 'withdraw'
        },
        {
            'id':2,
            'amount':3000,
            'action': 'deposit'
        }
    ]

    results = []

    if action.lower() == 'deposit':
        for payment in payments:
            if payment['action'] == 'deposit':
                results.append(payment)
    elif action.lower() == 'withdraw':
        for payment in payments:
            if payment['action'] == 'withdraw':
                results.append(payment)

    return JsonResponse(results, safe=False)


