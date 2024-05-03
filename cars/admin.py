from django.contrib import admin
from cars.models import CarModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'author']
