from . models import Team
from cars.models import Car


def custom_context_processor(request):
    teams = Team.objects.all().order_by("-id")

    # all search field
    fields = ['car_model', 'city', 'year', 'body_style']

    # get all unique value
    distinct_values = {field: Car.objects.values_list(field, flat=True).distinct() for field in fields}

    model_search = distinct_values["car_model"]
    city_search = distinct_values["city"]
    year_search = distinct_values["year"]
    body_style_search = distinct_values["body_style"]


    return {
        "current_path": request.path,
        "teams": teams,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }


