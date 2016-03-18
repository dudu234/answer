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
    loginid = request.GET.get("PersonId", None)
    p = Person(name=loginname, company=logincompany, personId=loginid, score=0, isDelete=0)
    p.save()
    response = HttpResponse(json.dumps({"id": p.id, "name": p.name}))
    response.set_cookie("id", p.id, 3600)
    response.set_cookie("name", p.name, 3600)
    return response