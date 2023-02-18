from django.urls import path
from .views import ItemCreateView, ItemUpdateView, ItemDeleteView, my_lists, SingleListView

urlpatterns = [
    path("my_lists/", my_lists, name="items_lists"),
    path("my_lists/<int:pk>/", SingleListView.as_view(), name="items_list"),
    path('items/add/', ItemCreateView.as_view(), name='item_add'),
    path('items/<int:pk>/update', ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/',
         ItemDeleteView.as_view(), name='item_delete'),
]
