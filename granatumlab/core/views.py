from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from core.models import Recipes


def show_home(request): # HttpRequest
    menu = ['Сгенерировать блюдо', 'Личный кабинет', 'О проекте']
    variables = {"menu": menu}
    return render(request,"core/home.html", variables)

def show_about(request):
    return render(request,"core/about.html")

def show_hub(request):
    return render(request,"core/hub.html") # позже будет обработка текста чата и галочек

def show_result(request, res_slug):
    recipe = get_object_or_404(Recipes, slug=res_slug)
    data = {
        'recipe': recipe,
    }
    return render(request,"core/result.html", data) # тут позже будет поиск блюда в базе

def show_fridge(request):
    return render(request,"core/fridge.html")

def show_info(request):
    return render(request,"core/info.html")

def show_shops(request):
    return render(request,"core/shops.html")










# Create your views here.
