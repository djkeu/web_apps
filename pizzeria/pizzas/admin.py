from django.contrib import admin

from .models import Pizza

admin.site.register(Pizza)
admin.site.register(Topping)
