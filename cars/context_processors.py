from . models import Car


def custom_car_context_processor(request):
    feature_cars = Car.objects.all().order_by('-id').filter(is_featured=True)
    all_cars = Car.objects.all()
    return {
        'feature_cars': feature_cars,
        'all_cars': all_cars
    }
