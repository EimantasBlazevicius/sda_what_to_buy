from django.urls import path
from .views import my_lists, items_list, home
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", home, name="index"),
    path("my_lists/", login_required(my_lists), name="lists-list"),
    path("my_lists/<pk>/", login_required(items_list), name='items-list'),
]
