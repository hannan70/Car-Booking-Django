from django.shortcuts import render, get_object_or_404
from .models import Car


# Create your views here.
def car_page(request):
    context = {
         'title': "| Car Inventory"
    }
    return render(request, 'pages/car.html', context)


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

    if 'car_model' in request.GET:
        car_model = request.GET['car_model']
        if car_model:
             cars = cars.filter(car_model__iexact=car_model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
             cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
             cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
             cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if min_price:
             cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars': cars
    }
    return render(request, 'pages/search.html', context)
