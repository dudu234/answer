from django.shortcuts import render
from django.http.response import HttpResponse
from ans.models import Person
# Create your views here.
import json


def login(request):
    return render(request, 'login.html')


def login2(request):
    return render(request, 'login2.html')


def insert_person(request):
    loginname = request.POST.get("loginname", None)
    logincompany = request.POST.get("logincompany", None)
    loginid = request.POST.get("PersonId",None)
 #   p = Person(name=loginname, company=logincompany, personId=loginid)
 #   p.save()
    return success