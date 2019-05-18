from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .forms import ImageForm

# Create your views here.
def welcome(request):
    return render(request,'')