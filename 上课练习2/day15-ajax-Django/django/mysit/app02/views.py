from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(requset):

    return HttpResponse('app02.home')