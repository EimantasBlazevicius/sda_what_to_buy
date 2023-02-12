from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList


def my_lists(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request, "shopping_list.html",  context={"shopping_lists": shopping_lists})


def hello2(request):
    anything = request.GET.get("situation")
    return HttpResponse(f'<h1>Potato Wars are {anything}?</h1>')
