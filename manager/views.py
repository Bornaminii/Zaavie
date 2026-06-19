from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def manager_name_view(request):
    return HttpResponse("manager page")
