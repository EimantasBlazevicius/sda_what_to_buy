from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_lists),
    path("potato/", views.hello2),
]
