from django.shortcuts import render
from .forms import clientform
from django.http import HttpResponseRedirect
from . import models
# Create your views here.

def home(request):
    categories = list(models.categories.objects.all())
    return render(request, "drive/index.html", {"liste":categories})

def traitementupdate(request, id):
    lform = clientform(request.POST)
    if lform.is_valid():
        commandes = lform.save(commit=False)
        commandes.id = id;
        commandes.save()
        return HttpResponseRedirect("/drive/")
    else:
        return render(request, "commandes/update.html", {"form": lform, "id": id})

def delete(request, id):
    lieu = models.Lieu.objects.get(pk=id)
    lieu.delete()
    return HttpResponseRedirect("/visite/")

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