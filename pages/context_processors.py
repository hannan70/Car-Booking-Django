from . models import Team

def custom_context_processor(request):
    teams = Team.objects.all().order_by("-id")
    return {
        "current_path": request.path,
        "teams": teams,
    }


