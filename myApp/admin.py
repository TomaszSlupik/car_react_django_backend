from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["id", "title"]

admin.site.register(Car, CarAdmin)