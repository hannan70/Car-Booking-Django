from lib2to3.btm_utils import reduce_tree

from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home_page(request):
    cars = Car.objects.all()

    # search_fields = Car.objects.values('car_model', 'city', 'year', 'body_style')

    # model_search = Car.objects.values_list("car_model", flat=True).distinct()
    # city_search = Car.objects.values_list("city", flat=True).distinct()
    # year_search = Car.objects.values_list("year", flat=True).distinct()
    # body_style_search = Car.objects.values_list("body_style", flat=True).distinct()

    # all search field
    fields = ['car_model', 'city', 'year', 'body_style']

    context = {
        'cars': cars,
        'title': "| Home"
    }
    return render(request, 'pages/home.html', context)


def about_page(request):
    context = {
         'title': "| About"
    }
    return render(request, 'pages/about.html', context)


def service_page(request):
    context = {
         'title': "| Service"
    }
    return render(request, 'pages/service.html', context)


def contact_page(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        text_message = request.POST['text_message']

        message = f"Name: {name}\n Email: {email}\n Phone: {phone}\n Message: {text_message}\n"

        # form validation
        if not name:
            messages.error(request, "Name field is required !")
        elif not email:
            messages.error(request, "Email field is required !")
        elif not subject:
            messages.error(request, "Subject field is required")
        elif not phone:
            messages.error(request, "Phone field is required")
        elif not text_message:
            messages.error(request, "Message field is required")
        else:
            send_mail(
                subject,
                message,
                "hannan.diuh@gmail.com",
                ["hannan728070@gmail.com"],
                fail_silently=False
            )
            messages.success(request, "Contact Message Send Successful")
            return redirect("contact-page")

    context = {
         'title': "| Contact"
    }
    return render(request, 'pages/contact.html', context)
