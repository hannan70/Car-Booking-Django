from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_page, name="car-page"),
    path('car-details/<int:id>', views.car_details, name="car-details"),
    path('search/', views.search, name="search")
]
