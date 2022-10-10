from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def generator(request):
    return render(request, 'home.html')

def password(request):
    generated_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 8))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    for i in range(length):
        generated_password+=random.choice(characters)
    context = {'password': generated_password}
    return render(request, 'password.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)