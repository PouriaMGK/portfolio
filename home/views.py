from django.http import HttpResponse
from django.shortcuts import render
from .models import Data
from datetime import datetime
from zoneinfo import ZoneInfo

def nowaday():
    return datetime.now(ZoneInfo(Asia/Tehran))


def landing_page(request):
    person = Data.objects.all()[0]
    return render (request, "home/index.html" , {'name' : person.name , 'title' : person.title , 'email' : person.email,
    'now' : nowaday})