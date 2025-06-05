from django.contrib import admin
from .models import Recipe, Ingredient, Have

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Have)