from django.shortcuts import render
from app.models import *
# Create your views here.
def topic(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'topic.html',d)

def web(request):
    QSW=Webpage.objects.all()
    d={'webs':QSW}
    return render(request,'web.html',d)

def access(request):
    QSA=AcessRecords.objects.all()
    d={'acces':QSA}
    return render(request,'access.html',d)