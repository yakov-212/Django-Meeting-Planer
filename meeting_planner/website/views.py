from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    return render(request,"Website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(requests):
    return HttpResponse(f"The current date is {datetime.now()}")

def about(requests):
    return HttpResponse("about abouts is about abouts")

