from django.db.models import QuerySet
from django.shortcuts import render
from .models import Dish, Category


# Create your views here.

def index(request):
    x = Dish.objects.all()
    context = {'results': x}
    return render(request, 'index.html', context)
