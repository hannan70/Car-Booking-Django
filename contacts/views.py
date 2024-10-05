from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        if form.is_valid():
            if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
                if has_contacted:
                    messages.error(request, "Already send the message")
                    return redirect("/car/car-details/" + car_id)
                else:
                    form.save()
                    send_mail(
                        "New car message",
                        "You have a new message for the car " + car_title + ' Please login your admin panel for more info',
                        "hannan.diuh@gmail.com",
                        [admin_email],
                        fail_silently=False
                    )
                    messages.success(request, "Message Send Successful")
                    return redirect("/car/car-details/" + car_id)
            else:
                messages.error(request, "First you have to login")
                return redirect("/car/car-details/" + car_id)

        else:
            messages.error(request, "Message Send Error !!!")
            return redirect("/car/car-details/" + car_id)