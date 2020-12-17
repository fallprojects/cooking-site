from django.http import HttpResponse
from django.shortcuts import render
from .models import Cook
# Create your views here.

def CookView(request):
    cook_list = Cook.objects.all()
    return render(request, 'cook_list.html')



