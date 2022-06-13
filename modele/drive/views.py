from django.http import HttpResponseRedirect
from .forms import clientform
from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    return render(request, "drive/index.html")