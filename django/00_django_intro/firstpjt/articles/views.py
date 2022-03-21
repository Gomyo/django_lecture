import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def variables(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }
    return render(request, 'variables.html', context)

def filters(request):
    foods = ['족발', '피자', '햄버거', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'filters.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        "message": message,
    }
    return render(request, 'catch.html', context)

def varRoute(request, name):
    context = {
        'name': name,
    }
    return render(request, 'varRoute.html', context)
