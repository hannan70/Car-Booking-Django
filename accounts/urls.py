from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_page, name="login"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout_page, name="logout"),
]
