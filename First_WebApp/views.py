from django.http import HttpResponse
from django.shortcuts import render
from . import ML_Model


def home(request):
    name = "Mohammad"
    return render(request, 'index.html', {'name': {name}})


def result(request):
    age = request.GET['user_age']
    name = request.GET['user_name']
    user_input = ML_Model.ML(age)
    message = f'Hi, {name}, you are now {user_input}, years old'
    return render(request, 'result.html', {'message': message})