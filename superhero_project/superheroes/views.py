from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/details.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)

        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def change(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
       'single_hero': single_hero
    } 
    if request.method == 'POST':
        change_name = request.POST.get('change_name')
        change_alter_ego = request.POST.get('change_alter_ego')
        change_primary = request.POST.get('change_primary_ability')
        change_secondary = request.POST.get('change_secondary_ability')
        change_catchphrase = request.POST.get('change_catchphrase')
        hero_id = Superhero(name=change_name, alter_ego=change_alter_ego, primary=change_primary, secondary=change_secondary, catchphrase=change_catchphrase)
        hero_id.save()
        return HttpResponseRedirect(reverse('superheroes:detail', context))
    else:
        return render(request, 'superheroes/change.html', context)