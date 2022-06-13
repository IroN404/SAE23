from django.http import HttpResponseRedirect
from .forms import clientform
from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    client = list(models.client.objects.all())
    return render(request, "drive/index.html", {"liste":client})

def traitementupdate(request, id):
    lform = clientform(request.POST)
    if lform.is_valid():
        client = lform.save(commit=False)
        client.id = id;
        client.save()
        return HttpResponseRedirect("/drive/")
    else:
        return render(request, "clients/update.html", {"form": lform, "id": id})

def delete(request, id):
    client = models.cleint.objects.get(pk=id)
    client.delete()
    return HttpResponseRedirect("/drive/")

def ajout(request):
    if request.method == "POST":
        form = clientform(request)
        if form.is_valid():
            client = form.save()
            return HttpResponseRedirect("/drive/")
        else:
            return render(request,"drive/ajoutclient.html",{"form": form})
    else :
        form = clientform()
        return render(request,"drive/ajoutclient.html",{"form" : form})