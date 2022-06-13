from django.http import HttpResponseRedirect
from .forms import prduitsform
from django.shortcuts import render
from . import models

def ajout(request):
    if request.method == "POST":
        form = LieuForm(request)
        if form.is_valid():
            lieu = form.save()
            return HttpResponseRedirect("/visite/")
        else:
            return render(request,"visite/ajout.html",{"form": form})
    else :
        form = LieuForm()
        return render(request,"visite/ajout.html",{"form" : form})