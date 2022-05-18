from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JoueurForm
from .models import JoueurModel
# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = JoueurForm(request)
        if form.is_valid():
            joueur = form.save()
            return HttpResponseRedirect("/bibliotheque/")
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = JoueurForm()
        return render(request,"bibliotheque/ajout.html",{"form" : form})

def traitement(request):
    lform = JoueurForm(request.POST)
    if lform.is_valid():
        joueur = lform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})


def index(request):
    liste = JoueurModel.objects.all()
    return render(request, 'bibliotheque/index.html', {'liste': liste})

def affiche(request, id):
    joueur = JoueurModel.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"joueur" : joueur})

def delete(request, id):
    joueur = JoueurModel.objects.get(pk=id)
    joueur.delete()
    return HttpResponseRedirect("/bibliotheque/")

def update(request, id):
    joueur = JoueurModel.objects.get(pk=id)
    lform = JoueurForm(joueur.dico())
    return render(request, "bibliotheque/update.html", {"form": lform,"id":id})

def traitementupdate(request, id):
    lform = JoueurForm(request.POST)
    if lform.is_valid():
        joueur = lform.save(commit=False)
        joueur.id = id;
        joueur.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})

