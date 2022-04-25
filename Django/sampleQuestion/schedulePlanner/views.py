from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
### functions or classes are mapped to urls

def index(request):
    return HttpResponse("Welcome to Snigdha's Schedule Planner")

def monday(request):
    return HttpResponse("Today I am learning Data Science")

def tuesday(request):
    return HttpResponse("Today I am learning Big Data")

def weekly_timetable(request, day):
    text=""
    if day=="monday":
        text="I will learn data science"
    elif day=="tuesday":
        text="I will learn Big data"
    return HttpResponse(text)
