from django.shortcuts import render, get_object_or_404
from .models import Car


# Create your views here.
def car_page(request):
    return render(request, 'pages/car.html')


def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)
    context = {
        'single_car': single_car
    }
    return render(request, 'pages/car-details.html', context)


def search(request):
    cars = Car.objects.order_by('-id')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    context = {
        'cars': cars
    }
    return render(request, 'pages/search.html', context)
