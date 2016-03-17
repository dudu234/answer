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
    loginname = request.GET.get("name", None)
    logincompany = request.GET.get("company", None)
    loginid = request.POST.get("PersonId", None)
    p = Person(addTime=now(), updateTime=now(), name='name', company='hha', personId='123', score=10, isDelete=0)
    p.save()
    return HttpResponse(json.dumps({"msg": "success"}))