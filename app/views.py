from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def insert_topic(request):
    form=Topicform()
    d={'form':form}
    if request.method=="POST":
        form_data=Topicform(request.POST)
        if form_data.is_valid:
            form_data.save()
            return HttpResponse('model is saved by modelform')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    form=(Webpageform)
    d={'form':form}
    if request.method=="POST":
        form_data=Webpageform(request.POST)
        if form_data.is_valid:
            form_data.save()
            return HttpResponse('model is saved by modelform')
    return render(request,'insert_webpage.html',d)

def insert_AccessRecords(request):
    form=(AccessRecordsform)
    d={'form':form}
    if request.method=="POST":
        form_data=AccessRecordsform(request.POST)
        if form_data.is_valid:
            form_data.save()
            return HttpResponse('model is saved by modelform')
    return render(request,'insert_AccessRecords.html',d)

 
