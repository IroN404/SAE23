from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    categories = list(models.categories.objects.all())
    return render(request, "drive/index.html", {"liste":categories})