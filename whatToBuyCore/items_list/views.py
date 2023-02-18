from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import ShoppingList, ShoppingItem

from django.urls import reverse_lazy


class ItemCreateView(CreateView):
    model = ShoppingItem
    fields = '__all__'


class ItemUpdateView(UpdateView):
    model = ShoppingItem
    fields = '__all__'


class ItemDeleteView(DeleteView):
    model = ShoppingItem
    success_url = reverse_lazy('items_lists')


def my_lists(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request, "shopping_lists.html",  context={"shopping_lists": shopping_lists})


def my_list(request, pk):

    shopping_list = ShoppingList.objects.get(id=pk)
    items_list = shopping_list.shoppingitem_set.all()
    return render(request, "shopping_list.html",  context={"shopping_list": items_list})
