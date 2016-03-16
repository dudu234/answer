from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')


def login2(request):
    return render(request, 'login2.html')
