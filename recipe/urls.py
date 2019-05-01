# -*- coding: utf-8 -*-

from recipe.models import Author
from recipe.models import Recipes
from django.contrib import admin
from django.urls import path
from recipe.views import index, recipe_stuff, author_stuff

admin.site.register(Author)
admin.site.register(Recipes)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('author/<int:author_id>/', author_stuff),
    path('recipes/<int:recipe_id>/', recipe_stuff)
]
    