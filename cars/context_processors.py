from . models import Car
from django.core.paginator import Paginator

def custom_car_context_processor(request):
    feature_cars = Car.objects.order_by('-id').filter(is_featured=True)
    all_cars = Car.objects.all()
    paginator = Paginator(all_cars, 4)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)

    return {
        'feature_cars': feature_cars,
        'all_cars': page_cars
    }
