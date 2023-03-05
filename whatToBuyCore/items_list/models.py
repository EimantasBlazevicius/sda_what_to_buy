from django.db.models import (
    CASCADE, CharField, ForeignKey, Model, BooleanField)
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.admin import ModelAdmin


# class ItemsAdmin(ModelAdmin):

#     @staticmethod
#     def released_year(obj):
#         return obj.released.year

#     @staticmethod
#     def cleanup_description(modeladmin, request, queryset):
#         queryset.update(description=None)

#     ordering = ['id']
#     list_display = ['id', 'name', 'description', 'is_completed']
#     list_display_links = ['id', 'name']
#     list_per_page = 3
#     list_filter = ['description']
#     search_fields = ['name']
#     actions = ['cleanup_description']


class ShoppingList(Model):
    title = CharField('Shopping list name', max_length=100)
    user = ForeignKey(User, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class ShoppingItem(Model):
    name = CharField("Shopping list item name", max_length=100)
    description = CharField("Shopping list item description",
                            max_length=300, null=True, blank=True)
    is_completed = BooleanField(default=False)
    shopping_list = ForeignKey(ShoppingList, on_delete=CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items-list', kwargs={'pk': self.shopping_list.pk})
