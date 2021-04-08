from django.urls import path
from . import views


urlpatterns = [
    path("cars/", views.car, name="cars"),
    path("<int:id>", views.car_detail, name="car_detail"),
]
