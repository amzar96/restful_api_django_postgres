from django.contrib import admin
from .models import User, Restaurant, Review

addModel = [User, Restaurant, Review]
admin.site.register(addModel)
