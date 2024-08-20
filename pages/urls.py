from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('about-page/', views.about_page, name="about-page"),
    path('service-page/', views.service_page, name="service-page"),
    path('contact-page/', views.contact_page, name="contact-page"),
]
