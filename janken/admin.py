from django.contrib import admin

# Register your models here.

from .models import Janken

admin.site.register(Janken)