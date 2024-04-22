from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from .models import Tache
def index(request):
    return render(request,'TODO/index.html',locals())

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user != None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Le nom ou le mot de passe incorrect")
    form = AuthenticationForm()
    return render(request,'TODO/login.html',locals())

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm()
    return render(request,'TODO/register.html',locals())

from .forms import AjouteTache

@login_required
def ajoutTache(request,id):
    if request.method == 'POST':
        form = AjouteTache(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            statut = form.cleaned_data['finish']
            description = form.cleaned_data['description']
            Tache.objects.create(nom=nom,finish=statut,description=description,user_id = id)
            return redirect('tache',id)
    form = AjouteTache()
    return render(request,'TODO/ajout.html',locals())


@login_required
def Taches(request,id):
    taches = Tache.objects.filter(user_id = id)
    return render(request,'TODO/tache.html',locals())

@login_required
def affiche(request,id):
    tache = Tache.objects.get(pk = id)
    if not tache.finish :
        etat = "En cours"
    else:
        etat = "Terminer"
    return render (request,'TODO/affiche.html',locals())

@login_required
def supprimer(request,id):
    tache = Tache.objects.get(pk = id)
    tache.delete()
    return redirect('index')

@login_required
def modifier(request,id):
    tache = Tache.objects.get(pk = id)
    if tache.finish:
        tache.finish = False
    else:
        tache.finish = True
    tache.save()
    return redirect('index')