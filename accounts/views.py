from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # user validation
        if not firstname:
            messages.error(request, "First name is required")
        elif not lastname:
            messages.error(request, "Last name is required")
        elif not username:
            messages.error(request, "Username is required")
        elif not email:
            messages.error(request, "Email is required")
        elif not password:
            messages.error(request, "Password is required")
        else:
            if password == confirm_password:
                exists_user = User.objects.filter(username=username).exists()
                exists_email = User.objects.filter(email=email).exists()
                if exists_user:
                    messages.error(request, "Username already exists")
                elif exists_email:
                    messages.error(request, "Email already exists")
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    # if you want to auto login then you can use this code
                    # auth.login(request, user)
                    # messages.success(request, "Login success")
                    # return redirect("dashboard")
                    user.save()
                    messages.success(request, "User registration success")
                    return redirect('login')
            else:
               messages.error(request, "Password and confirm password does not match")

    return render(request, 'auth/register.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'auth/dashboard.html')


def logout_page(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout success')
        return redirect('home-page')
