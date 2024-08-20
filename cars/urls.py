from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_page, name="car-page"),
]
