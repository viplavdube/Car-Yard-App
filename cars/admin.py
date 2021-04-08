from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.


class CarAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "car_title",
        "city",
        "model",
        "price",
        "miles",
        "fuel_type",
        "is_featured",
    )


admin.site.register(Car, CarAdmin)
