from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

def Insert_Topic(request):
    tn = input('Enter Topic_name : ')
    to = Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    return HttpResponse('Data Inserted')

def Insert_Webpage(request):
    tn = input('Enter Topic_name : ')
    to = Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    n = input('Enter Name : ')
    u = input('Enter url : ')
    wo = Webpage.objects.get_or_create(Topic_name = to, Name = n, url = u)[0]
    wo.save()
    return HttpResponse('Data Inserted')

def Insert_AC(request):
    tn = input('Enter Topic_name : ')
    to = Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    n = input('Enter Name : ')
    u = input('Enter url : ')
    wo = Webpage.objects.get_or_create(Topic_name = to, Name = n, url = u)[0]
    wo.save()
    d = input('Enter Date : ')
    a = input('Enter Author : ')
    e = input('Enter email : ')
    ao = AccessRecord.objects.get_or_create(Name=wo, Date=d, Author=a, email=e)[0]
    ao.save()
    return HttpResponse('Data Inserted')