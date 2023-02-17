from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList


def my_lists(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request, "shopping_lists.html",  context={"shopping_lists": shopping_lists})


def items_list(request, id):
    shopping_list = ShoppingList.objects.get(id=id)
    # shoppingitem_set is derived from modelname_set
    items_list = shopping_list.shoppingitem_set.all()
    return render(request, "shopping_list.html",  context={"shopping_list": items_list})
