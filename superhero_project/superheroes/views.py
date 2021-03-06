# from typing_extensions import ParamSpecKwargs
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse

# Create your views here.

def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request,'superheroes/index.html',context)

def detail(request,hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)   
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html',context)

def update(request,hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    context = {
        'hero': hero
    }
    if request.method == "POST":
        hero.name = request.POST.get('name')
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary_ability')
        hero.secondary_ability = request.POST.get('secondary_ability')
        hero.catch_phrase = request.POST.get('catch_phrase')
        #new_hero = Superhero(name=name,alter_ego=alter_ego,primary_ability=primary,secondary_ability=secondary,catch_phrase=catch_phrase)
        hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request,'superheroes/update.html',context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary_ability')
        secondary = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name=name,alter_ego=alter_ego,primary_ability=primary,secondary_ability=secondary,catch_phrase=catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request,'superheroes/create.html')

def delete(request,hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    hero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))
